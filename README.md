# OpenMAPT1Auto - 3D Slicer Extension

Automated brain MRI parcellation into **280 anatomical regions** using [OpenMAP-T1](https://github.com/OishiLab/OpenMAP-T1) deep learning model.

![3D Visualization](Screenshots/Screenshot2.png)

---

⚠️ License
Extension codeMITOpenMAP-T1 modelsJHU Research Software License — Non-Commercial

✅ Non-commercial research use only
❌ No commercial use without separate agreement
✅ Attribution required in publications


🚀 Installation
Prerequisites

3D Slicer Nightly (5.11 or later)
NVIDIA GPU recommended (CPU also supported, slower)
Internet connection for model download (~1.5 GB)

Step 1 — Install from Extension Manager

Download and install 3D Slicer Nightly from https://download.slicer.org
Open Slicer → View → Extension Manager
Search for OpenMAPT1Auto → Install → Restart Slicer

Step 2 — Copy library files (required until automated)

This step is currently required. It will be automated in a future build.


Download the repository zip:

   https://github.com/niyaziacer/SlicerOpenMAPT1Auto/archive/refs/heads/main.zip

Extract the zip and locate this folder:

   SlicerOpenMAPT1Auto-main/OpenMAPT1AutoParcellation/OpenMAPT1AutoParcellationLib

Copy the OpenMAPT1AutoParcellationLib folder to:
Windows:

   C:\Users\[YourUsername]\AppData\Local\slicer.org\3D Slicer 5.11.0-[date]\slicer.org\Extensions-[no]\OpenMAPT1Auto\lib\Slicer-5.11\qt-scripted-modules\
Mac:
   /Users/[YourUsername]/Library/Application Support/slicer.org/3D Slicer 5.11.0-[date]/slicer.org/Extensions-[no]/OpenMAPT1Auto/lib/Slicer-5.11/qt-scripted-modules/

Also copy labeled.txt from OpenMAPT1AutoParcellation/ to the same folder.
Restart Slicer.

Step 3 — Download models

Open Modules → Segmentation → OpenMAP-T1 Auto Parcellation
Click Download Models from Google Drive
Accept the license agreement
Wait for download (~1.5 GB, 10–15 minutes)

Manual download (if automatic fails):
Download from Google Drive, extract, and place MODEL_FOLDER/ inside the extension's qt-scripted-modules/ directory.

📖 Usage

Load your T1-weighted MRI: File → Add Data
Go to Modules → Segmentation → OpenMAP-T1 Auto Parcellation
Select your T1 volume from the dropdown
Click Run OpenMAP-T1 Pipeline
Wait for processing:

NVIDIA GPU: ~2–5 minutes
CPU only: ~15–45 minutes


Results appear automatically in 2D slices and 3D view


📂 Output Files
All outputs are saved in the output/ folder inside the extension directory:
FileDescriptionT1_280_volumes.csvVolume measurements per region (CSV)T1_280_volumes.xlsxVolume measurements per region (Excel)T1_280_segment.nii.gzSegmentation labelmap (NIfTI)
You can also export results to Excel directly using the Export Results button in the extension panel.

🔬 Features

Automated brain parcellation into 280 anatomical regions
Automatic dependency installation on first load
Automatic model download from Google Drive (~1.5 GB)
Non-commercial license agreement dialog
Volume calculation for all regions
Export results to CSV and Excel
3D visualization with labeled segments in Segment Editor
Named segment labels from labeled.txt


🏗️ Pipeline Stages
StageDescriptionPreprocessingStandardize T1 volumeCroppingExtract brain regionSkull strippingRemove non-brain tissueParcellationSegment into 280 regionsHemisphere separationLeft/Right classificationPostprocessingAlign and refine segmentation

🐛 Troubleshooting
ProblemSolution"Models not found"Click Download Models button in the extensionDownload failsUse the manual download link above"No module named utils"Make sure OpenMAPT1AutoParcellationLib is copied to the qt-scripted-modules folderLabels not showingMake sure labeled.txt is copied to the qt-scripted-modules folderSlow processingNormal on CPU — wait 15–45 minutes. NVIDIA GPU recommended.Alignment issuesMake sure you select the correct T1 volume from the dropdown

🔬 Citation
If you use this extension in your research, please cite both:
This extension:
bibtex@software{openmapt1auto,
  title={OpenMAPT1Auto: 3D Slicer Extension for Automated Brain Parcellation},
  author={Acer, Niyazi},
  year={2025},
  url={https://github.com/niyaziacer/SlicerOpenMAPT1Auto}
}
Original OpenMAP-T1 (required):
bibtex@article{nishimaki2024openmap,
  title={OpenMAP-T1: A Rapid Deep Learning Approach to Parcellation of 280 Anatomical Regions to Cover the Whole Brain},
  author={Nishimaki, Taiki and others},
  year={2024}
}

🤝 Acknowledgments
Built upon OpenMAP-T1 by Taiki Nishimaki and Johns Hopkins University.
License: JHU Research Software License

📧 Contact

Extension: acerniyazi@gmail.com
OpenMAP-T1 models/license: OishiLab GitHub
