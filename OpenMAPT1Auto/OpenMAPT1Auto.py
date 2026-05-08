# OpenMAPT1Auto.py
import slicer.ScriptedLoadableModule

class OpenMAPT1Auto(slicer.ScriptedLoadableModule.ScriptedLoadableModule):
    def __init__(self, parent):
        super().__init__(parent)
        parent.title = "OpenMAP-T1 Auto Parcellation"
        parent.categories = ["Segmentation"]
        parent.contributors = ["Niyazi Acer (Sanko University)"]
        parent.helpText = "Automated brain MRI parcellation into 280 anatomical regions using OpenMAP-T1."
        parent.acknowledgementText = "OpenMAP-T1 by Taiki Nishimaki and Johns Hopkins University."
