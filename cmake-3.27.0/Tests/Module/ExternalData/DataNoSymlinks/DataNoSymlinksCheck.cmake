if(NOT EXISTS "${Data}")
  message(SEND_ERROR "Input file:\n  ${Data}\n" "does not exist!")
endif()
if(IS_SYMLINK "${Data}")
  message(SEND_ERROR "Input file:\n  ${Data}\nis a symlink but should not be!")
endif()
