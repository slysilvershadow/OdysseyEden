# CMake generated Testfile for 
# Source directory: /workspaces/OdysseyEden/cmake-3.27.0
# Build directory: /workspaces/OdysseyEden/cmake-3.27.0
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
include("/workspaces/OdysseyEden/cmake-3.27.0/Tests/EnforceConfig.cmake")
add_test([=[SystemInformationNew]=] "/workspaces/OdysseyEden/cmake-3.27.0/bin/cmake" "--system-information" "-G" "Unix Makefiles")
set_tests_properties([=[SystemInformationNew]=] PROPERTIES  _BACKTRACE_TRIPLES "/workspaces/OdysseyEden/cmake-3.27.0/CMakeLists.txt;519;add_test;/workspaces/OdysseyEden/cmake-3.27.0/CMakeLists.txt;0;")
subdirs("Source/kwsys")
subdirs("Utilities/std")
subdirs("Utilities/KWIML")
subdirs("Utilities/cmlibrhash")
subdirs("Utilities/cmzlib")
subdirs("Utilities/cmcurl")
subdirs("Utilities/cmnghttp2")
subdirs("Utilities/cmexpat")
subdirs("Utilities/cmbzip2")
subdirs("Utilities/cmzstd")
subdirs("Utilities/cmliblzma")
subdirs("Utilities/cmlibarchive")
subdirs("Utilities/cmjsoncpp")
subdirs("Utilities/cmlibuv")
subdirs("Source/CursesDialog/form")
subdirs("Utilities/cmcppdap")
subdirs("Source")
subdirs("Utilities")
subdirs("Tests")
subdirs("Auxiliary")
