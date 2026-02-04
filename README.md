# OpenMAPT1Auto - 3D Slicer Extension

Automated brain MRI parcellation into **280 anatomical regions** using [OpenMAP-T1](https://github.com/OishiLab/OpenMAP-T1) deep learning model.

![3D Visualization](Screenshots/Screenshot2.png)

---

## ⚠️ License

- **Extension code:** MIT
- **OpenMAP-T1 models:** [JHU Research Software License - Non-Commercial](https://github.com/OishiLab/OpenMAP-T1/blob/main/LICENSE)
  - ✅ Non-commercial research use only
  - ❌ No commercial use without separate agreement
  - ✅ Attribution required in publications

---

## 🚀 Installation

### Prerequisites

- **3D Slicer** 5.0 or later
- **PyTorch** (installed automatically by Slicer)
- **OpenMAP-T1 models** (~1.5GB, downloaded automatically)

### Option 1: From Extension Manager (Recommended)

1. Open 3D Slicer
2. Go to **View → Extension Manager**
3. Search for **OpenMAPT1Auto**
4. Click **Install**
5. Restart Slicer

### Option 2: Manual Installation

1. Clone repository:
```bash
git clone https://github.com/niyaziacer/SlicerOpenMAPT1Auto.git
```

2. Open 3D Slicer
3. Go to **Edit → Application Settings → Modules**
4. Add path: `/path/to/SlicerOpenMAPT1Auto`
5. Restart Slicer

---

## 📥 Model Download

Models are downloaded **automatically** when you first use the extension:

1. Open the extension in Slicer
2. Click **"Download Models from Google Drive"**
3. Accept the license agreement
4. Wait for download (~1.5GB, 10-15 minutes)

### Manual Download (if automatic fails)

1. Download from: [Google Drive Link](https://drive.google.com/file/d/1YEE65X5Cx8LHK-C070TbZARHp1C08KxA/view?usp=sharing)
2. Extract the zip file
3. Place `MODEL_FOLDER/` inside the extension directory

---

## 📖 Usage

1. Load your **T1-weighted MRI** in 3D Slicer
2. Go to **Modules → Segmentation → OpenMAP-T1 Auto Parcellation**
3. Download models if not already downloaded
4. Select your T1 volume from the dropdown
5. Click **"Run OpenMAP-T1 Pipeline"**
6. Wait for processing (2-5 minutes depending on GPU/CPU)
7. Results appear automatically in 2D slices and 3D view

### Output Files

All outputs are saved in the `output/` folder:

| File | Description |
|---|---|
| `T1_280_volumes.csv` | Volume measurements per region (CSV) |
| `T1_280_volumes.xlsx` | Volume measurements per region (Excel) |
| `T1_280_segment.nii.gz` | Segmentation labelmap (NIfTI) |

You can also export results to Excel directly from the **Export Results** button in the extension.

---

## 🔬 Features

- Automated brain parcellation into **280 anatomical regions**
- Automatic model download from Google Drive (~1.5GB)
- Non-commercial license agreement dialog
- Volume calculation for all regions
- Export results to **CSV and Excel**
- 3D visualization with labeled segments in Segment Editor

---

## 🏗️ Pipeline Stages

1. **Preprocessing** - Standardize T1 volume
2. **Cropping** - Extract brain region
3. **Skull Stripping** - Remove non-brain tissue
4. **Parcellation** - Segment into 280 regions
5. **Hemisphere Separation** - Left/Right classification
6. **Postprocessing** - Align and refine segmentation

---

## 🔬 Citation

If you use this extension in your research, please cite both:

### This Extension
```bibtex
@software{openmapt1auto,
  title={OpenMAPT1Auto: 3D Slicer Extension for Automated Brain Parcellation},
  author={Acer, Niyazi},
  year={2025},
  url={https://github.com/niyaziacer/SlicerOpenMAPT1Auto}
}
```

### Original OpenMAP-T1 (Required)
```bibtex
@article{nishimaki2024openmap,
  title={OpenMAP-T1: A Rapid Deep Learning Approach to Parcellation of 280 Anatomical Regions to Cover the Whole Brain},
  author={Nishimaki, Taiki and others},
  year={2024}
}
```

---

## 🐛 Troubleshooting

| Problem | Solution |
|---|---|
| "Models not found" | Click **Download Models** button in the extension |
| Download fails | Use the manual download link above |
| "openpyxl not found" | Open Python Console in Slicer, run: `import slicer; slicer.util.pip_install("openpyxl")` |
| Alignment issues | Make sure you select the correct T1 volume |

---

## 🤝 Acknowledgments

Built upon **OpenMAP-T1** by Taiki Nishimaki and Johns Hopkins University.
- Original Project: [OpenMAP-T1](https://github.com/OishiLab/OpenMAP-T1)
- License: [JHU Research Software License](https://github.com/OishiLab/OpenMAP-T1/blob/main/LICENSE)

---

## 📧 Contact

- **Extension:** [acerniyazi@gmail.com](mailto:acerniyazi@gmail.com)
- **OpenMAP-T1 models/license:** [OishiLab GitHub](https://github.com/OishiLab/OpenMAP-T1)
