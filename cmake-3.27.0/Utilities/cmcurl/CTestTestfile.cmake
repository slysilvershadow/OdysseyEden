# CMake generated Testfile for 
# Source directory: /workspaces/OdysseyEden/cmake-3.27.0/Utilities/cmcurl
# Build directory: /workspaces/OdysseyEden/cmake-3.27.0/Utilities/cmcurl
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test([=[curl]=] "curltest" "http://open.cdash.org/user.php")
set_tests_properties([=[curl]=] PROPERTIES  _BACKTRACE_TRIPLES "/workspaces/OdysseyEden/cmake-3.27.0/Utilities/cmcurl/CMakeLists.txt;1580;add_test;/workspaces/OdysseyEden/cmake-3.27.0/Utilities/cmcurl/CMakeLists.txt;0;")
subdirs("lib")
