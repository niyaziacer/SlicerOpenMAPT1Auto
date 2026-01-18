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

You must download them separately (see Installation below).

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
2. View → Extension Manager
3. Search "OpenMAP-T1"
4. Click Install
5. Restart Slicer
6. Models will download automatically on first use

### Method 2: Manual Installation
```bash
# Clone repository
git clone https://github.com/niyaziacer/OpenMAPT1Auto.git

# Add to Slicer
# Edit → Application Settings → Modules → Additional module paths
# Add: /path/to/OpenMAPT1Auto

# Download models (automatic on first run, or manual):
# [Instructions will be added]
```

---

## 📖 Usage

1. **Load T1 MRI:** File → Add Data → Select your T1-weighted NIfTI file
2. **Open Module:** Modules → Segmentation → OpenMAP-T1 Auto Parcellation
3. **Select Input:** Choose T1 volume from dropdown
4. **Run:** Click "Run OpenMAP-T1" button
5. **Wait:** ~90 seconds (GPU) or ~10 minutes (CPU)
6. **Results:**
   - 2D/3D segmentation visible in slice/3D views
   - Segment Editor: All 280 regions listed with names
   - Output folder: CSV + Excel files with volumes

---

## 📊 Features

✅ **280 Brain Regions:** Comprehensive parcellation including:
- Cortical structures (frontal, parietal, temporal, occipital)
- Subcortical nuclei (thalamus, caudate, putamen, hippocampus, amygdala)
- White matter tracts (corpus callosum, internal capsule, fornix)
- Brainstem and cerebellum subdivisions
- Ventricles and CSF spaces

✅ **Multiple Outputs:**
- NIfTI labelmap (aligned to input T1)
- CSV volume table (LabelID, Volume_mm³, LabelName)
- Excel file (.xlsx) for easy analysis
- 3D surface models (optional)

✅ **Integrated Visualization:**
- 2D overlay on slice views
- 3D rendering in 3D view
- Segment Editor: Browse all regions by name

✅ **Fast Processing:**
- GPU: 45-90 seconds
- CPU: 8-15 minutes
- 570× faster than FreeSurfer

---

## 🛠️ System Requirements

**Minimum:**
- 3D Slicer 5.2.2 or later
- 8 GB RAM
- Windows 10/11, macOS 11+, or Linux

**Recommended:**
- 16 GB RAM
- NVIDIA GPU with 6+ GB VRAM (CUDA 11.7+)
- SSD for faster I/O

**Python Dependencies:**
(Installed automatically by Slicer)
- PyTorch 1.13+
- NumPy
- NiBabel
- Pandas
- openpyxl (for Excel export)

---

## 📸 Screenshots

[Add screenshots here]

---

## 🐛 Troubleshooting

### Models not downloading?
Check internet connection or download manually from [link].

### GPU not detected?
Install CUDA 11.7: https://developer.nvidia.com/cuda-11-7-0-download-archive

### Segmentation misaligned?
Ensure input is T1-weighted MRI with ~1mm isotropic resolution.

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch
3. Submit pull request

---

## 📧 Contact

**Extension Issues:** Niyazi Acer - acerniyazi@gmail.com  
**Model/Algorithm:** See [OpenMAP-T1 repository](https://github.com/TaikiNishimaki/OpenMAP-T1)

---

## 🙏 Acknowledgments

- **OpenMAP-T1 Team:** Taiki Nishimaki and collaborators at Johns Hopkins University
- **3D Slicer Community:** For the excellent platform and support
- **JHU-MNI Atlas:** Johns Hopkins University and Mori Lab

---

## 📚 References

[Add OpenMAP-T1 paper reference when published]

References
OpenMAP-T1 Original Publication:

Nishimaki K, Onda K, Ikuta K, Chotiyanonta J, Uchida Y, Mori S, Iyatomi H, Oishi K; Alzheimer’s Disease Neuroimaging Initiative; Australian Imaging Biomarkers and Lifestyle Study of Ageing.
OpenMAP-T1: A Rapid Deep-Learning Approach to Parcellate 280 Anatomical Regions to Cover the Whole Brain.
Hum Brain Mapp. 2024 Nov;45(16):e70063.
doi: 10.1002/hbm.70063
PMID: 39523990 • PMCID: PMC11551626











