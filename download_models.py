"""
OpenMAPT1Auto Model Download Helper

This script guides users to download OpenMAP-T1 models from the official source.
Models are NOT included due to JHU license restrictions.
"""

import webbrowser
import os
from pathlib import Path

def check_models_exist():
    """Check if model files are already present"""
    model_folder = Path(__file__).parent / "MODEL_FOLDER"
    model_file = model_folder / "best_metric_model.pth"
    
    return model_folder.exists() and model_file.exists()

def download_model():
    """
    Guide users to download OpenMAP-T1 models from official source
    """
    print("\n" + "=" * 70)
    print(" " * 15 + "OpenMAPT1Auto - Model Download")
    print("=" * 70)
    
    # Check if models already exist
    if check_models_exist():
        print("\n✅ Model files are already present!")
        print(f"📁 Location: {Path(__file__).parent / 'MODEL_FOLDER'}")
        print("\nYou can now use the extension in 3D Slicer.")
        print("=" * 70)
        return True
    
    print("\n⚠️  MODEL FILES REQUIRED")
    print("-" * 70)
    print("\nThis extension requires OpenMAP-T1 pretrained models.")
    print("Due to license restrictions, models are NOT included.")
    print("\n📜 License: JHU Research Software License")
    print("   - Non-commercial research use only")
    print("   - No redistribution")
    print("   - Attribution required")
    
    print("\n" + "=" * 70)
    print("📥 HOW TO DOWNLOAD MODELS")
    print("=" * 70)
    
    print("\n1️⃣  Visit the official OpenMAP-T1 repository:")
    print("    🔗 https://github.com/OishiLab/OpenMAP-T1")
    
    print("\n2️⃣  Review and accept the license terms")
    
    print("\n3️⃣  Download the pretrained model files")
    print("    📦 Size: ~1.6 GB")
    
    print("\n4️⃣  Extract and place in MODEL_FOLDER/")
    print(f"    📁 Target location: {Path(__file__).parent / 'MODEL_FOLDER'}")
    
    print("\n5️⃣  Verify files are present:")
    print("    ✓ best_metric_model.pth")
    print("    ✓ [other model files]")
    
    print("\n" + "=" * 70)
    print("© The Johns Hopkins University")
    print("=" * 70)
    
    # Ask if user wants to open the repository
    print("\n")
    try:
        response = input("Would you like to open the repository now? (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            print("\n🌐 Opening OpenMAP-T1 repository in browser...")
            webbrowser.open("https://github.com/OishiLab/OpenMAP-T1")
            print("✓ Browser opened!")
        else:
            print("\n💡 You can manually visit:")
            print("   https://github.com/OishiLab/OpenMAP-T1")
    except (KeyboardInterrupt, EOFError):
        print("\n\n💡 Manual download link:")
        print("   https://github.com/OishiLab/OpenMAP-T1")
    
    print("\n" + "=" * 70)
    print("After downloading, run this script again to verify installation.")
    print("=" * 70 + "\n")
    
    return False

def main():
    """Main entry point"""
    success = download_model()
    
    if success:
        print("\n✅ Setup complete! You can now use OpenMAPT1Auto in 3D Slicer.\n")
    else:
        print("\n⚠️  Please download models to continue.\n")

if __name__ == "__main__":
    main()