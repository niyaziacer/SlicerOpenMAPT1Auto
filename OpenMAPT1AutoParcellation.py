# OpenMAPT1AutoParcellation.py
# ScriptedLoadableModule for 3D Slicer

import os
import qt
import ctk
import slicer
import vtk
import torch
import nibabel as nib
import numpy as np
import pandas as pd

# Attempt to import OpenMAP utils
try:
    from utils.cropping import cropping
    from utils.hemisphere import hemisphere
    from utils.load_model import load_model
    from utils.parcellation import parcellation
    from utils.preprocessing import preprocessing
    from utils.stripping import stripping
    from utils.postprocessing import postprocessing
except Exception as e:
    utils_import_error = str(e)
else:
    utils_import_error = None

class OpenMAPT1AutoParcellation(slicer.ScriptedLoadableModule.ScriptedLoadableModule):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title = "OpenMAP-T1 Auto Parcellation"
        parent.categories = ["Segmentation"]
        parent.contributors = ["Adapted for Slicer"]
        parent.helpText = "Run OpenMAP-T1 pipeline on a T1 MRI volume and load aligned labelmap."
        parent.acknowledgementText = "OpenMAP-T1"

class OpenMAPT1AutoParcellationWidget(slicer.ScriptedLoadableModule.ScriptedLoadableModuleWidget):
    def setup(self):
        super().setup()
        self.moduleDir = os.path.dirname(__file__)
        self.layout = self.parent.layout()

        # Info
        info = qt.QLabel("OpenMAP-T1 Auto Parcellation\nSelect a T1 volume and press Run.")
        info.setWordWrap(True)
        self.layout.addWidget(info)

        # Volume selector
        self.inputSelector = slicer.qMRMLNodeComboBox()
        self.inputSelector.nodeTypes = ["vtkMRMLScalarVolumeNode"]
        self.inputSelector.selectNodeUponCreation = True
        self.inputSelector.setMRMLScene(slicer.mrmlScene)
        self.inputSelector.setToolTip("Select the T1 volume to segment")
        self.layout.addWidget(qt.QLabel("Input T1 Volume:"))
        self.layout.addWidget(self.inputSelector)

        # Run button
        self.runButton = qt.QPushButton("Run OpenMAP-T1")
        self.runButton.toolTip = "Save T1, run pipeline, load aligned labelmap"
        self.runButton.enabled = True
        self.runButton.clicked.connect(self.onRunClicked)
        self.layout.addWidget(self.runButton)

        # Log
        self.log = qt.QTextEdit()
        self.log.setReadOnly(True)
        self.log.setMaximumHeight(160)
        self.layout.addWidget(qt.QLabel("Log:"))
        self.layout.addWidget(self.log)
        self.layout.addStretch(1)

    def logMessage(self, text):
        self.log.append(text)
        slicer.app.processEvents()

    def onRunClicked(self):
        try:
            self.runPipeline()
        except Exception as e:
            self.logMessage(f"ERROR: {e}")
            import traceback
            self.logMessage(traceback.format_exc())

    def runPipeline(self):
        if utils_import_error:
            raise RuntimeError("OpenMAP utils import failed: " + utils_import_error)

        # Force working directory to moduleDir to find split_map.pkl
        os.chdir(self.moduleDir)

        volumeNode = self.inputSelector.currentNode()
        if not volumeNode:
            raise RuntimeError("No T1 volume selected.")

        self.logMessage("Starting pipeline...")

        output_folder = os.path.join(self.moduleDir, "output")
        os.makedirs(output_folder, exist_ok=True)

        tmp_t1_path = os.path.join(output_folder, "T1_tmp.nii.gz")
        self.logMessage(f"T1 saved: {tmp_t1_path}")
        slicer.util.saveNode(volumeNode, tmp_t1_path)

        # Load models
        model_folder = os.path.join(self.moduleDir, "MODEL_FOLDER")
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.logMessage(f"Loading models from {model_folder}...")
        class Opt: m = model_folder
        cnet, ssnet, pnet_c, pnet_s, pnet_a, hnet_c, hnet_a = load_model(Opt(), device)
        self.logMessage("Models loaded.")

        # Preprocess
        self.logMessage("Running preprocessing...")
        odata, data = preprocessing(tmp_t1_path, output_folder, "T1")
        self.logMessage(f"Preprocessing done. data shape: {getattr(data,'shape', 'unknown')}")

        # Crop, strip, parcellate, hemisphere
        self.logMessage("Cropping...")
        cropped = cropping(data, cnet, device)
        self.logMessage("Stripping...")
        stripped, shift = stripping(cropped, data, ssnet, device)
        self.logMessage("Parcellating...")
        parcellated = parcellation(stripped, pnet_c, pnet_s, pnet_a, device)
        self.logMessage("Hemisphere separation...")
        separated = hemisphere(stripped, hnet_c, hnet_a, device)

        # Postprocessing
        self.logMessage("Postprocessing...")
        aligned_output = postprocessing(parcellated, separated, shift, device)

        # === Load label names from Untitled.txt ===
        label_dict = {}
        txt_path = os.path.join(output_folder, "Untitled.txt")
        if os.path.exists(txt_path):
            try:
                self.logMessage(f"Loading labels from {txt_path}...")
                with open(txt_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip()
                        if not line or line.startswith('#'):
                            continue
                        parts = line.split()
                        try:
                            idx = int(parts[0])
                            name = ' '.join(parts[7:]).strip('"').strip("'")
                            if name:
                                label_dict[idx] = name
                        except:
                            pass
                self.logMessage(f"Loaded {len(label_dict)} labels")
            except Exception as e:
                self.logMessage(f"Warning: Could not load labels: {e}")
        else:
            self.logMessage(f"Warning: Label file not found: {txt_path}")

        # === Calculate volumes ===
        self.logMessage("Calculating region volumes...")
        voxel_volume = np.prod(data.header.get_zooms())
        unique_labels, counts = np.unique(aligned_output, return_counts=True)
        mask = unique_labels != 0
        unique_labels = unique_labels[mask]
        counts = counts[mask]
        volumes_mm3 = counts * voxel_volume

        df = pd.DataFrame({
            "LabelID": unique_labels.astype(int),
            "Volume_mm3": volumes_mm3
        })
        
        if label_dict:
            df['LabelName'] = df['LabelID'].map(label_dict).fillna("")
        else:
            df['LabelName'] = ""

        # Save CSV
        csv_path = os.path.join(output_folder, "T1_280_volumes.csv")
        df.to_csv(csv_path, index=False)
        self.logMessage(f"Volume table saved: {csv_path}")
        
        # === EXCEL EXPORT ===
        try:
            excel_path = os.path.join(output_folder, "T1_280_volumes.xlsx")
            df.to_excel(excel_path, index=False, sheet_name="Brain_Volumes")
            self.logMessage(f"Excel file saved: {excel_path}")
        except Exception as e:
            self.logMessage(f"Warning: Excel export failed: {e}")
            self.logMessage("  Install: pip install openpyxl")

        # Save labelmap
        nii = nib.Nifti1Image(aligned_output.astype(np.uint16), affine=data.affine)
        out_label = os.path.join(output_folder, "T1_280_segment.nii.gz")
        nib.save(nii, out_label)
        self.logMessage(f"Final labelmap saved: {out_label}")

        # Load labelmap into Slicer (2D)
        labelNode = slicer.util.loadLabelVolume(out_label)
        labelNode.SetName("OpenMAP_T1_Labelmap")
        labelNode.SetAndObserveTransformNodeID(None)
        labelNode.GetDisplayNode().SetOpacity(0.4)
        slicer.util.setSliceViewerLayers(background=volumeNode, foreground=labelNode, foregroundOpacity=0.4)
        self.logMessage("2D labelmap loaded")

        # === CREATE 3D SEGMENTATION ===
        try:
            self.logMessage("Creating 3D segmentation (may take 1-2 minutes)...")
            
            # Create segmentation node
            segNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLSegmentationNode")
            segNode.SetName("OpenMAP_T1_Segmentation")
            
            # Import labelmap to segmentation
            segLogic = slicer.modules.segmentations.logic()
            segLogic.ImportLabelmapToSegmentationNode(labelNode, segNode)
            segNode.SetReferenceImageGeometryParameterFromVolumeNode(volumeNode)
            
            # Create 3D surfaces
            segNode.CreateClosedSurfaceRepresentation()
            
            # === RENAME SEGMENTS WITH LABELS ===
            if label_dict:
                segmentation = segNode.GetSegmentation()
                segmentIds = vtk.vtkStringArray()
                segmentation.GetSegmentIDs(segmentIds)
                
                renamed = 0
                for i in range(segmentIds.GetNumberOfValues()):
                    segId = segmentIds.GetValue(i)
                    segment = segmentation.GetSegment(segId)
                    if segment:
                        # Get current name
                        segName = segment.GetName()
                        
                        # Extract label ID from name (e.g., "Segment_1_75" -> 75)
                        try:
                            # Try parsing last number
                            parts = segName.split('_')
                            label_id = int(parts[-1])
                            
                            # Apply new name if exists
                            if label_id in label_dict:
                                segment.SetName(label_dict[label_id])
                                renamed += 1
                        except:
                            pass
                
                self.logMessage(f"Renamed {renamed} segments")
            
            # Set display properties
            displayNode = segNode.GetDisplayNode()
            if displayNode:
                displayNode.SetVisibility3D(True)
                displayNode.SetOpacity3D(0.6)
                displayNode.SetVisibility2DFill(True)
                displayNode.SetVisibility2DOutline(True)
            
            # Center 3D view
            layoutManager = slicer.app.layoutManager()
            if layoutManager:
                threeDWidget = layoutManager.threeDWidget(0)
                if threeDWidget:
                    threeDView = threeDWidget.threeDView()
                    threeDView.resetFocalPoint()
                    threeDView.resetCamera()
            
            self.logMessage("✓ 3D segmentation created and visible in Segment Editor")
            
        except Exception as e:
            self.logMessage(f"Warning: 3D segmentation failed: {e}")
            import traceback
            self.logMessage(traceback.format_exc())

        self.logMessage("="*50)
        self.logMessage("✅ PIPELINE COMPLETED")
        self.logMessage("="*50)
        self.logMessage(f"Total regions: {len(unique_labels)}")
        self.logMessage(f"Output folder: {output_folder}")
        self.logMessage("Files:")
        self.logMessage(f"  • T1_280_volumes.csv")
        self.logMessage(f"  • T1_280_volumes.xlsx")
        self.logMessage(f"  • T1_280_segment.nii.gz")
        self.logMessage("")
        self.logMessage("View in Segment Editor module to see all regions!")
        self.logMessage("="*50)