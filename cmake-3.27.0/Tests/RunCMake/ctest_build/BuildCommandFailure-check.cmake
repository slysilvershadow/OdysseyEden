file(GLOB build_xml_file "${RunCMake_TEST_BINARY_DIR}/Testing/*/Build.xml")
if(build_xml_file)
  file(READ "${build_xml_file}" build_xml LIMIT 4096)
  if(NOT build_xml MATCHES [[this command failed]])
    string(REPLACE "\n" "\n  " build_xml "  ${build_xml}")
    set(RunCMake_TEST_FAILED
      "Build.xml does not have expected error message:\n${build_xml}"
      )
  endif()
else()
  set(RunCMake_TEST_FAILED "Build.xml not found")
endif()
