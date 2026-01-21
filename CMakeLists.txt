cmake_minimum_required(VERSION 3.16.3...3.19.7 FATAL_ERROR)

project(OpenMAPT1Auto)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://github.com/niyaziacer/SlicerOpenMAPT1Auto")
set(EXTENSION_CATEGORY "Segmentation")
set(EXTENSION_CONTRIBUTORS "Niyazi Acer (Sanko University)")
set(EXTENSION_DESCRIPTION "This extension provides automated brain MRI parcellation using OpenMAP-T1 deep learning model. It segments T1-weighted MRI images into 280 anatomical regions covering the whole brain. Model files must be downloaded separately from official OpenMAP-T1 repository.")
set(EXTENSION_ICONURL "https://raw.githubusercontent.com/niyaziacer/SlicerOpenMAPT1Auto/main/OpenMAPT1Auto.png")
set(EXTENSION_SCREENSHOTURLS "https://raw.githubusercontent.com/niyaziacer/SlicerOpenMAPT1Auto/main/Screenshots/Screenshot1.png https://raw.githubusercontent.com/niyaziacer/SlicerOpenMAPT1Auto/main/Screenshots/Screenshot2.png")
set(EXTENSION_DEPENDS "NA") # Specified as a list or "NA" if no dependencies

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(OpenMAPT1Auto)
## NEXT_MODULE

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})