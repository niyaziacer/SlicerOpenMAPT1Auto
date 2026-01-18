cmake_minimum_required(VERSION 3.16.3...3.19.7 FATAL_ERROR)

project(OpenMAPT1Auto)

#-----------------------------------------------------------------------------
# Extension meta-information
set(EXTENSION_HOMEPAGE "https://github.com/niyaziacer/OpenMAPT1Auto")
set(EXTENSION_CATEGORY "Segmentation")
set(EXTENSION_CONTRIBUTORS "Niyazi Acer (Erciyes University)")
set(EXTENSION_DESCRIPTION "Automatic whole-brain parcellation into 280 anatomical regions using OpenMAP-T1 deep learning model. Provides rapid segmentation (~90 seconds with GPU), 3D visualization, and volumetric analysis with Excel export.")
set(EXTENSION_ICONURL "https://raw.githubusercontent.com/niyaziacer/OpenMAPT1Auto/main/OpenMAPT1Auto.png")
set(EXTENSION_SCREENSHOTURLS "https://raw.githubusercontent.com/niyaziacer/OpenMAPT1Auto/main/Screenshots/screenshot1.png")
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

#-----------------------------------------------------------------------------
include(${Slicer_EXTENSION_GENERATE_CONFIG})
include(${Slicer_EXTENSION_CPACK})