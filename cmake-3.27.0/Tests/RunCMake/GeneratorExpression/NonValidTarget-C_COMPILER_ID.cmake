add_custom_command(OUTPUT "${CMAKE_CURRENT_BINARY_DIR}/copied_file.c"
  COMMAND "${CMAKE_COMMAND}" -E copy "${CMAKE_CURRENT_SOURCE_DIR}/empty.c" "${CMAKE_CURRENT_BINARY_DIR}/copied_file$<C_COMPILER_ID>.c"
)
add_custom_target(drive DEPENDS "${CMAKE_CURRENT_BINARY_DIR}/copied_file.c")
