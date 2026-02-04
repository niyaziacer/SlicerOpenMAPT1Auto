cmake_minimum_required(VERSION 3.16.3...3.19.7 FATAL_ERROR)

project(OpenMAPT1Auto)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://github.com/niyaziacer/SlicerOpenMAPT1Auto")
set(EXTENSION_CATEGORY "Segmentation")
set(EXTENSION_CONTRIBUTORS "Niyazi Acer (Sanko University)")
set(EXTENSION_DESCRIPTION "Automated brain MRI parcellation into 280 anatomical regions using OpenMAP-T1 deep learning model. NON-COMMERCIAL USE ONLY.")
set(EXTENSION_ICONURL "https://raw.githubusercontent.com/niyaziacer/SlicerOpenMAPT1Auto/master/OpenMAPT1Auto/Resources/Icons/OpenMAPT1Auto.png")
set(EXTENSION_SCREENSHOTURLS "https://raw.githubusercontent.com/niyaziacer/SlicerOpenMAPT1Auto/master/Screenshots/Screenshot1.png")
set(EXTENSION_DEPENDS "NA")
set(EXTENSION_BUILD_SUBDIRECTORY inner-build)

set(SUPERBUILD_TOPLEVEL_PROJECT inner)

#-----------------------------------------------------------------------------
# Extension dependencies
find_package(Slicer REQUIRED)
include(${Slicer_USE_FILE})

#-----------------------------------------------------------------------------
# Extension modules
add_subdirectory(OpenMAPT1Auto)
add_subdirectory(OpenMAPT1AutoParcellation)

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})