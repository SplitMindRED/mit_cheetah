cmake_minimum_required(VERSION 3.5)
project(cheetah_software)

set(CMAKE_DISABLE_IN_SOURCE_BUILD ON)
set(CMAKE_DISABLE_SOURCE_CHANGES  ON)

find_package(catkin REQUIRED 
  roscpp
  std_msgs
  trajectory_msgs
  quadruped_msgs
  unitree_legged_msgs
  COMPONENTS)

catkin_package(
  INCLUDE_DIRS
  LIBRARIES ${PROJECT_NAME}
)

# include_directories(
#   ${catkin_INCLUDE_DIRS}
#   )

if ("${CMAKE_SOURCE_DIR}" STREQUAL "${CMAKE_BINARY_DIR}")
  message(SEND_ERROR "In-source builds are not allowed.")
endif ()

set(CMAKE_COLOR_MAKEFILE   ON)
#execute_process(COMMAND ../scripts/make_types.sh)

set(CMAKE_MODULE_PATH ${PROJECT_SOURCE_DIR}/cmake)

#set(CMAKE_VERBOSE_MAKEFILE ON)

option(MINI_CHEETAH_BUILD "use compiler flags for mini cheetah computer" OFF)
set(BUILD_TYPE_RELEASE TRUE)

option(USE_SIM "Do not build simulator" OFF)
set(UNITREE_LEGGED_SDK_PATH "../unitree_legged_sdk")
set(UNITREE_PLATFORM "amd64")

if(MINI_CHEETAH_BUILD)
  SET (THIS_COM "../" )
  CONFIGURE_FILE(${CMAKE_CURRENT_SOURCE_DIR}/config.h.cmake
    ${CMAKE_BINARY_DIR}/Configuration.h)
  set(CMAKE_CXX_FLAGS "-O3 -no-pie -ggdb -Wall \
  -Wextra -Wcast-align -Wdisabled-optimization -Wformat=2 \
  -Winit-self -Wmissing-include-dirs -Woverloaded-virtual \
  -Wshadow -Wsign-promo")
  set(CMAKE_C_FLAGS "-O3  -ggdb -std=gnu99 -I.")
  message("**** Mini-Cheetah build enabled ****")
else(MINI_CHEETAH_BUILD)
  SET (THIS_COM "${PROJECT_SOURCE_DIR}/" )
  CONFIGURE_FILE(${CMAKE_CURRENT_SOURCE_DIR}/config.h.cmake
    ${CMAKE_BINARY_DIR}/Configuration.h)

  if(CMAKE_SYSTEM_NAME MATCHES Linux)
    set(CMAKE_CXX_FLAGS "-O3 -no-pie -march=native -ggdb -Wall \
    -Wextra -Wcast-align -Wdisabled-optimization -Wformat=2 \
    -Winit-self -Wmissing-include-dirs -Woverloaded-virtual \
    -Wshadow -Wsign-promo")
  elseif(APPLE)
    set(CMAKE_CXX_FLAGS "-O3 -march=native -ggdb -Wall \
    -Wextra -Wcast-align -Wdisabled-optimization -Wformat=2 \
    -Winit-self -Wmissing-include-dirs -Woverloaded-virtual \
    -Wshadow -Wsign-promo")
    include_directories("/usr/local/include/")   # lcm includes
  endif()

  set(CMAKE_C_FLAGS "-O3  -ggdb  -march=native -std=gnu99 -I.")
  message("**** Mini-Cheetah build disabled ****")
endif(MINI_CHEETAH_BUILD)

set(CMAKE_CXX_STANDARD 14)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIR}
  ${UNITREE_LEGGED_SDK_PATH}/include
  ${UNITREE_LEGGED_SDK_PATH}/include/unitree_legged_sdk
  )

#find_package(lcm)

link_directories(${UNITREE_LEGGED_SDK_PATH}/lib)
string(CONCAT LEGGED_SDK_NAME libunitree_legged_sdk_${UNITREE_PLATFORM}.so)
set(EXTRA_LIBS ${LEGGED_SDK_NAME})
add_definitions(-DSDK3_2)

add_subdirectory(robot)

add_subdirectory(third-party)
add_subdirectory(common)

if(USE_SIM)
 add_subdirectory(sim)
else(USE_SIM)

endif()

add_subdirectory(user)
#add_subdirectory(rc_test)


