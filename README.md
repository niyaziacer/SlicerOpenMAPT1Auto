# OpenMAP-T1 Auto Parcellation for 3D Slicer

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![3D Slicer](https://img.shields.io/badge/3D%20Slicer-5.2+-blue)](https://www.slicer.org)

Automatic whole-brain parcellation into **280 anatomical regions** using the OpenMAP-T1 deep learning model.

⚡ **Fast:** ~90 seconds with GPU | ~10 minutes with CPU  
🧠 **Comprehensive:** 280 brain regions including subcortical, white matter, and cortical structures  
📊 **Outputs:** 3D segmentation, CSV/Excel volume tables, and Segment Editor integration

---

## ⚖️ License & Citation

### Extension Code
This 3D Slicer extension wrapper is licensed under **MIT License** (see [LICENSE](LICENSE)).

### OpenMAP-T1 Model
The underlying deep learning model is developed by **Taiki Nishimaki et al.** (Johns Hopkins University) and distributed under **JHU Research Software License**.

**Original Repository:** https://github.com/TaikiNishimaki/OpenMAP-T1

**⚠️ IMPORTANT:** Model weights (`.pth` files) are NOT included in this repository due to:
- Large file size (~4.5 GB total)
- Separate licensing terms (JHU License)

**How to Download Pretrained Models:**

You can obtain the pretrained models from the official OpenMAP-T1 repository:

📥 **[Download Pretrained Models](https://github.com/OishiLab/OpenMAP-T1#how-to-download-the-pretrained-model)**

The models will be downloaded automatically when you first run the extension in 3D Slicer. Alternatively, you can download them manually and place them in the `MODEL_FOLDER` directory.

**Model Files (8 total):**
- `CNet.pth` - Brain cropping network (~45 MB)
- `SSNet.pth` - Skull stripping network (~45 MB)
- `PNet_axial.pth` - Parcellation network, axial view (~87 MB)
- `PNet_coronal.pth` - Parcellation network, coronal view (~87 MB)
- `PNet_sagittal.pth` - Parcellation network, sagittal view (~87 MB)
- `HNet_axial.pth` - Hemisphere separation, axial view (~45 MB)
- `HNet_coronal.pth` - Hemisphere separation, coronal view (~45 MB)
- `penMAP-T1.pth` - Penalty map (~870 MB)

**Total Size:** ~4.3 GB

By downloading and using these models, you agree to the terms of the JHU Research Software License.

### Citation
If you use this tool in your research, please cite both:

**1. OpenMAP-T1 Original Work:**
```bibtex
@article{nishimaki2024openmap,
  title={OpenMAP-T1: A Rapid Whole-Brain Parcellation Approach},
  author={Nishimaki, Taiki and others},
  journal={[Journal]},
  year={2024}
}
```

**2. This Extension (optional):**
```bibtex
@software{acer2025openmap_slicer,
  author = {Acer, Niyazi},
  title = {OpenMAP-T1 3D Slicer Extension},
  year = {2025},
  url = {https://github.com/niyaziacer/OpenMAPT1Auto}
}
```

---

## 🚀 Installation

### Method 1: Extension Manager (Recommended - Coming Soon)

1. Open 3D Slicer (v5.2.2 or later)
2. **View** → **Extension Manager**
3. Search **"OpenMAP-T1"**
4. Click **Install**
5. Restart Slicer
6. **Models will download automatically on first use**

### Method 2: Manual Installation

#### Step 1: Clone Repository
```bash
git clone https://github.com/niyaziacer/OpenMAPT1Auto.git
cd OpenMAPT1Auto
```

#### Step 2: Download Pretrained Models

**Option A: Automatic (Recommended)**

Models will be downloaded automatically when you first run the module in 3D Slicer. On first use:
1. The extension will detect missing models
2. A download dialog will appear
3. Click "Yes" to download (~4.3 GB)
4. Wait for download to complete (~5-10 minutes depending on connection)

**Option B: Manual Download**

1. Visit the [OpenMAP-T1 model repository](https://github.com/OishiLab/OpenMAP-T1#how-to-download-the-pretrained-model)
2. Download all 8 model files (`.pth`) from the provided link
3. Create `MODEL_FOLDER` directory in the extension folder:
   ```bash
   mkdir MODEL_FOLDER
   ```
4. Place all `.pth` files inside `MODEL_FOLDER/`

**File structure after downloading models:**
```
OpenMAPT1Auto/
├── MODEL_FOLDER/              ← Create this folder
│   ├── CNet.pth              ← Download from OpenMAP-T1
│   ├── SSNet.pth
│   ├── HNet_axial.pth
│   ├── HNet_coronal.pth
│   ├── PNet_axial.pth
│   ├── PNet_coronal.pth
│   ├── PNet_sagittal.pth
│   └── penMAP-T1.pth
└── OpenMAPT1Auto/
    ├── OpenMAPT1AutoParcellation.py
    └── utils/
```

#### Step 3: Add to 3D Slicer

1. Open **3D Slicer**
2. **Edit** → **Application Settings** → **Modules**
3. Click **Add** under "Additional module paths"
4. Navigate to and select the `OpenMAPT1Auto` folder
5. Click **OK**
6. **Restart Slicer**
7. Module will appear under: **Modules** → **Segmentation** → **OpenMAP-T1 Auto Parcellation**

---

## 📖 Usage

### Basic Workflow

1. **Load T1 MRI**
   - File → Add Data → Select your T1-weighted NIfTI file (`.nii` or `.nii.gz`)
   - Ensure it's ~1mm isotropic resolution for best results

2. **Open Module**
   - Modules → Segmentation → **OpenMAP-T1 Auto Parcellation**

3. **Select Input**
   - Choose T1 volume from dropdown menu

4. **Run Segmentation**
   - Click **"Run OpenMAP-T1"** button
   - Processing time:
     - GPU: 45-90 seconds
     - CPU: 8-15 minutes

5. **View Results**
   - **2D views:** Colored overlay on slice views (red/yellow/green)
   - **3D view:** Surface rendering of all brain regions
   - **Segment Editor:** All 280 regions listed with anatomical names

6. **Export Data**
   - CSV file: `output/T1_280_volumes.csv`
   - Excel file: `output/T1_280_volumes.xlsx`
   - NIfTI labelmap: `output/T1_280_segment.nii.gz`

### Advanced Options

**Disable 3D Surfaces (faster):**
- Uncheck "Create 3D Surfaces" before running
- Reduces processing time if only volume measurements are needed

**Disable Excel Export:**
- Uncheck "Export to Excel" if Excel format not required
- CSV will still be generated

---

## 📊 Features

### ✅ Comprehensive Anatomical Coverage (280 Regions)

**Cortical Structures:**
- Frontal: Superior/Middle/Inferior frontal gyri, precentral gyrus
- Parietal: Superior/Inferior parietal lobule, precuneus, postcentral gyrus
- Temporal: Superior/Middle/Inferior temporal gyri, fusiform gyrus
- Occipital: Superior/Middle/Inferior occipital gyri, cuneus, lingual gyrus
- Cingulate: Anterior/Posterior cingulate cortex (rostral, dorsal, subgenual)
- Insula: Left and right insular cortex

**Subcortical Nuclei:**
- Basal ganglia: Caudate, putamen, globus pallidus, nucleus accumbens
- Thalamus (left/right)
- Hypothalamus
- Amygdala
- Hippocampus
- Red nucleus
- Substantia nigra
- Basal forebrain (anterior/posterior)
- Mammillary bodies

**White Matter Tracts:**
- Corpus callosum (genu, body, splenulum)
- Internal capsule (anterior/posterior/retrolenticular limbs)
- External capsule
- Corona radiata (anterior/superior/posterior)
- Cingulum
- Fornix
- Superior/Inferior longitudinal fasciculus
- Inferior fronto-occipital fasciculus

**Brainstem & Cerebellum:**
- Midbrain, pons, medulla (subdivided)
- Cerebellar gray and white matter
- Cerebellar peduncles (superior/middle/inferior)

**Ventricles & CSF:**
- Lateral ventricles (frontal horn, body, atrium, occipital horn, inferior horn)
- Third ventricle
- Fourth ventricle
- Periventricular white matter

### ✅ Multiple Output Formats

1. **NIfTI Labelmap** (`.nii.gz`)
   - Aligned to input T1 geometry
   - 280 labeled regions
   - Compatible with ITK-SNAP, FSL, FreeSurfer

2. **CSV Volume Table**
   - Columns: LabelID, Volume_mm³, LabelName
   - Easy import to statistical software (R, Python, SPSS)

3. **Excel Spreadsheet** (`.xlsx`)
   - Formatted table with all measurements
   - Ready for analysis in Excel/LibreOffice

4. **3D Surface Models**
   - Closed surface representation
   - Visible in Segment Editor module
   - Interactive region selection

### ✅ Integrated Visualization

- **2D Overlay:** Color-coded regions on slice views
- **3D Rendering:** Interactive brain model with all regions
- **Segment Editor:** Browse, select, and analyze individual regions by name
- **Real-time Inspection:** Toggle visibility of specific structures

### ✅ Performance

| Hardware | Processing Time | Memory Usage |
|----------|----------------|--------------|
| RTX 3090 (24GB VRAM) | 45-90 seconds | 6-8 GB RAM |
| RTX 2060 (6GB VRAM) | 90-120 seconds | 6-8 GB RAM |
| Intel i9-12900K (CPU) | 8-15 minutes | 8-10 GB RAM |
| Intel i7-8700 (CPU) | 15-20 minutes | 8-10 GB RAM |

**570× faster than FreeSurfer** (90 seconds vs 10.8 hours)

---

## 🛠️ System Requirements

### Minimum
- **3D Slicer:** Version 5.2.2 or later
- **RAM:** 8 GB
- **Storage:** 10 GB free (5 GB for models + 5 GB for processing)
- **OS:** Windows 10/11, macOS 11+, or Linux (Ubuntu 20.04+)

### Recommended
- **RAM:** 16 GB or more
- **GPU:** NVIDIA GPU with 6+ GB VRAM (CUDA 11.7+)
- **Storage:** SSD for faster I/O
- **CPU:** Multi-core processor (8+ cores)

### Python Dependencies
(Automatically installed by 3D Slicer)
- PyTorch 1.13+
- NumPy
- NiBabel
- Pandas
- openpyxl (for Excel export)
- SciPy

---

## 📸 Screenshots

![Segmentation in 3D Slicer](Screenshots/screenshot1.png)
*3D visualization and slice views showing automated brain parcellation*

---

## 🐛 Troubleshooting

### Models Not Downloading?

**Problem:** Automatic download fails  
**Solution:**
1. Check internet connection
2. Download manually from [OpenMAP-T1 repository](https://github.com/OishiLab/OpenMAP-T1)
3. Place files in `MODEL_FOLDER/` directory
4. Restart 3D Slicer

### GPU Not Detected?

**Problem:** Module runs slowly (CPU mode)  
**Solution:**
1. Install CUDA 11.7: https://developer.nvidia.com/cuda-11-7-0-download-archive
2. Verify GPU in Python:
   ```python
   import torch
   print(torch.cuda.is_available())  # Should return True
   ```
3. Update NVIDIA drivers to latest version

### Segmentation Misaligned?

**Problem:** Labelmap doesn't overlay correctly on T1  
**Solution:**
- Ensure input is **T1-weighted MRI** (not T2, FLAIR, etc.)
- Check voxel resolution: should be ~1mm isotropic
- Verify orientation: use "Reformat" module if needed
- Avoid oblique acquisitions

### Out of Memory Error?

**Problem:** Crash during processing  
**Solution:**
- Close other applications
- Use CPU mode (slower but uses less RAM)
- Reduce image resolution if possible
- Upgrade RAM to 16+ GB

### Excel Export Failed?

**Problem:** "Excel export failed" warning  
**Solution:**
```bash
# Install openpyxl in Slicer's Python
pip_install("openpyxl")
```
Or use CSV output instead.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit changes: `git commit -m 'Add YourFeature'`
4. Push to branch: `git push origin feature/YourFeature`
5. Open a Pull Request

### Areas for Contribution
- Additional validation on different datasets
- Support for other MRI contrasts (T2, FLAIR)
- Improved model download UI
- Batch processing capabilities
- Integration with other Slicer modules

---

## 📧 Contact

**Extension Issues & Questions:**  
Niyazi Acer - acerniyazi@gmail.com
Sanko University, Department of Anatomy

**Model/Algorithm Questions:**  
See [OpenMAP-T1 repository](https://github.com/TaikiNishimaki/OpenMAP-T1) and contact original authors

**Bug Reports:**  
Please use [GitHub Issues](https://github.com/niyaziacer/OpenMAPT1Auto/issues)

---

## 🙏 Acknowledgments

- **OpenMAP-T1 Team:** Taiki Nishimaki and collaborators at Johns Hopkins University for developing the deep learning model
- **3D Slicer Community:** For the excellent platform and extensive documentation
- **JHU-MNI Atlas:** Johns Hopkins University and Mori Lab for the anatomical atlas
- **Oishi Lab:** For maintaining and distributing the OpenMAP-T1 models

---

## 📚 References

**OpenMAP-T1 Model:**
- Repository: https://github.com/TaikiNishimaki/OpenMAP-T1
- Model Download: https://github.com/OishiLab/OpenMAP-T1

**3D Slicer Platform:**
- Fedorov A., et al. (2012). 3D Slicer as an image computing platform for the Quantitative Imaging Network. *Magnetic Resonance Imaging*, 30(9), 1323-1341.

**Related Tools:**
- FreeSurfer: https://surfer.nmr.mgh.harvard.edu/
- FSL: https://fsl.fmrib.ox.ac.uk/
- ANTs: http://stnava.github.io/ANTs/

---

## 📝 Version History

**v1.0.0** (2025-01-19)
- Initial release
- 280-region automated parcellation
- 3D segmentation support
- Excel/CSV export
- Segment Editor integration
- GPU acceleration
- Automatic model download

---

## 📄 License

**Extension Code:** MIT License  
**OpenMAP-T1 Models:** JHU Research Software License  

See [LICENSE](LICENSE) for full details.

---

**Made with ❤️ for the neuroimaging community**