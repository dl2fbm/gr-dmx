INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_DMX dmx)

FIND_PATH(
    DMX_INCLUDE_DIRS
    NAMES dmx/api.h
    HINTS $ENV{DMX_DIR}/include
        ${PC_DMX_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    DMX_LIBRARIES
    NAMES gnuradio-dmx
    HINTS $ENV{DMX_DIR}/lib
        ${PC_DMX_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(DMX DEFAULT_MSG DMX_LIBRARIES DMX_INCLUDE_DIRS)
MARK_AS_ADVANCED(DMX_LIBRARIES DMX_INCLUDE_DIRS)

