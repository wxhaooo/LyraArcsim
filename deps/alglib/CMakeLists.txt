
include_directories(${CMAKE_CURRENT_SOURCE_DIR})

set(HEADERS
    alglibinternal.h
    alglibmisc.h
    ap.h
    dataanalysis.h
    diffequations.h
    fasttransforms.h
    integration.h
    interpolation.h
    linalg.h
    optimization.h
    solvers.h
    specialfunctions.h
    statistics.h
    stdafx.h
)

set(SOURCES
    src/alglibinternal.cpp
    src/alglibmisc.cpp
    src/ap.cpp
    src/dataanalysis.cpp
    src/diffequations.cpp
    src/fasttransforms.cpp
    src/integration.cpp
    src/interpolation.cpp
    src/linalg.cpp
    src/optimization.cpp
    src/solvers.cpp
    src/specialfunctions.cpp
    src/statistics.cpp
)

# Set include directories.
# include_directories()

# Disable stupid MSVC compiler warnings.
# add_definitions(-D_SCL_SECURE_NO_WARNINGS -D_CRT_SECURE_NO_WARNINGS)

set(CMAKE_DEBUG_POSTFIX "d")

add_library(alglib STATIC
    ${HEADERS}
    ${SOURCES}
)

# propnet has the following dependencies.
#add_dependencies(propnet
#)

# Set link libraries.
#target_link_libraries(propnet
#    ${Boost_LIBRARIES}
#)

# install(TARGETS propnet
#         RUNTIME DESTINATION bin
#         LIBRARY DESTINATION lib
#         ARCHIVE DESTINATION lib)
#
# #install(DIRECTORY include
#         DESTINATION .
#         PATTERN "*.hpp")
