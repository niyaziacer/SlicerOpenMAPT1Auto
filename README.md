# OpenMAPT1Auto - 3D Slicer Extension

Automated brain MRI parcellation using OpenMAP-T1 in 3D Slicer.

---

## ⚠️ Important: Model Files Required

This extension requires **OpenMAP-T1 pretrained models**, which are licensed by **Johns Hopkins University** under specific terms. 

**We do NOT distribute the model files.** You must download them directly from the official source.

---

## 📥 How to Download the Pretrained Models

### Step 1: Visit Official Repository

Go to the official OpenMAP-T1 repository:

🔗 **https://github.com/OishiLab/OpenMAP-T1**

### Step 2: Review License Terms

**IMPORTANT:** Before downloading, please review the license:
- ✅ **Non-commercial research use only**
- ❌ **No commercial use** without separate agreement
- ✅ **Attribution required** in publications

License: [JHU Research Software License - No For-Profit - No Redistribution](https://github.com/OishiLab/OpenMAP-T1/blob/main/LICENSE)

### Step 3: Download Models

Find the pretrained model download link in their repository:

📦 **[Link to pretrained model](https://github.com/OishiLab/OpenMAP-T1#pretrained-models)**

> **Note:** The model file is approximately **1.6 GB**. Download may take several minutes depending on your internet connection.

### Step 4: Extract to MODEL_FOLDER

1. After downloading, extract the model files
2. Place them in the `MODEL_FOLDER/` directory of this extension:
   ```
   OpenMAPT1Auto/
   └── MODEL_FOLDER/
       ├── best_metric_model.pth
       └── [other model files]
   ```

3. Verify the folder structure is correct

---

## 🚀 Installation

### Prerequisites
- **3D Slicer** 5.0 or later
- **Python** 3.7+
- **PyTorch** (will be installed automatically by Slicer)
- **OpenMAP-T1 models** (see above)

### Install Extension

#### Option 1: From Extension Manager (Coming Soon)
1. Open 3D Slicer
2. Go to **View** → **Extension Manager**
3. Search for "OpenMAPT1Auto"
4. Click **Install**

#### Option 2: Manual Installation (For Development)

```bash
# Clone repository
git clone https://github.com/[your-username]/OpenMAPT1Auto.git
cd OpenMAPT1Auto

# Download models (see instructions above)
# Place models in MODEL_FOLDER/

# Add to 3D Slicer
# 1. Open 3D Slicer
# 2. Edit → Application Settings → Modules
# 3. Add path: /path/to/OpenMAPT1Auto
# 4. Restart Slicer
```

---

## 📖 Usage

1. Load your T1-weighted MRI in 3D Slicer
2. Go to **Modules** → **Segmentation** → **OpenMAPT1Auto**
3. Select input volume
4. Click **Apply**
5. Wait for automatic parcellation (may take 2-5 minutes)
6. View results in 3D

---

## 🔬 Citation

If you use this extension in your research, please cite:

### This Extension
```bibtex
@software{openmaptlauto,
  title={OpenMAPT1Auto: 3D Slicer Extension for OpenMAP-T1},
  author={[Your Name]},
  year={2026},
  url={https://github.com/[your-username]/OpenMAPT1Auto}
}
```

### Original OpenMAP-T1
**IMPORTANT:** You MUST also cite the original OpenMAP-T1 work:

```bibtex
[OpenMAP-T1 citation - get from their repository]
```

© The Johns Hopkins University

---

## ⚖️ License

### This Extension Code
[Your chosen license - e.g., MIT, Apache 2.0]

See [LICENSE](LICENSE.txt) for details.

### OpenMAP-T1 Models
The pretrained models are licensed separately under:

**JHU Research Software License Agreement - No For-Profit - No Redistribution**

By using this extension, you agree to comply with OpenMAP-T1's license terms.

Full license: https://github.com/OishiLab/OpenMAP-T1/blob/main/LICENSE

---

## 🤝 Acknowledgments

This extension is built upon the excellent work of the OpenMAP-T1 team:

- **Original Project:** [OpenMAP-T1](https://github.com/OishiLab/OpenMAP-T1)
- **Developed by:** Johns Hopkins University, Oishi Lab
- **License:** JHU Research Software License

We are grateful to the original authors for making their research available to the community.

---

## 📧 Contact

For questions about **this extension**: [your email]

For questions about **OpenMAP-T1 models/license**: Contact JHU via their repository

---

## 🐛 Troubleshooting

### "Model files not found" error

**Solution:** 
1. Ensure you downloaded models from official source
2. Verify files are in `MODEL_FOLDER/` directory
3. Check file names match: `best_metric_model.pth`

### Download link not working

**Solution:**
Visit the official repository directly: https://github.com/OishiLab/OpenMAP-T1

### License questions

**Solution:**
Contact Johns Hopkins University Technology Transfer Office or the OpenMAP-T1 team directly.

---

## 🔄 Updates

- **v1.0.0** (2026-01-20): Initial release with model download instructions

---

**Note:** This is an independent extension. For official OpenMAP-T1 support, please visit their repository.