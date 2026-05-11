set(MODULE_NAME OpenMAPT1AutoParcellation)

set(MODULE_PYTHON_SCRIPTS
  ${MODULE_NAME}.py
  OpenMAPT1AutoParcellationLib/__init__.py
  OpenMAPT1AutoParcellationLib/utils/__init__.py
  OpenMAPT1AutoParcellationLib/utils/cropping.py
  OpenMAPT1AutoParcellationLib/utils/functions.py
  OpenMAPT1AutoParcellationLib/utils/hemisphere.py
  OpenMAPT1AutoParcellationLib/utils/load_model.py
  OpenMAPT1AutoParcellationLib/utils/make_csv.py
  OpenMAPT1AutoParcellationLib/utils/network.py
  OpenMAPT1AutoParcellationLib/utils/parcellation.py
  OpenMAPT1AutoParcellationLib/utils/postprocessing.py
  OpenMAPT1AutoParcellationLib/utils/preprocessing.py
  OpenMAPT1AutoParcellationLib/utils/stripping.py
  )

set(MODULE_PYTHON_RESOURCES
  Resources/Icons/${MODULE_NAME}.png
  OpenMAPT1AutoParcellationLib/utils/split_map.pkl
  )

slicerMacroBuildScriptedModule(
  NAME ${MODULE_NAME}
  SCRIPTS ${MODULE_PYTHON_SCRIPTS}
  RESOURCES ${MODULE_PYTHON_RESOURCES}
  WITH_GENERIC_TESTS
  )
