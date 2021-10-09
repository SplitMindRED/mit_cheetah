cmake_minimum_required(VERSION 3.5)
project(mit_cheetah_gazebo)

find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  roscpp
  std_msgs
)

catkin_package()

include_directories(
  include
  lib
  lib/lcm-types
  lib/lcm-types/cpp
  lib/robot
  lib/robot/include
  lib/sim
  lib/sim/include
  lib/common
  lib/common/FootstepPlanner
  lib/common/include
  lib/common/include/Utilities
  lib/common/include/Controllers
  lib/user
  lib/user/MIT_Controller
  lib/third-party
  lib/third-party/qpOASES
  lib/third-party/qpOASES/include
  /usr
  /usr/local
  /usr/local/include
  /usr/local/include/lcm
  ${catkin_INCLUDE_DIRS}
)

add_subdirectory(lib/common)
add_subdirectory(lib/robot)
add_subdirectory(lib/third-party)
add_subdirectory(lib/user)
add_subdirectory(lib/sim)

set(SOURCE_LIB_ROBOT lib/robot/src/SimulationBridge.cpp)

add_library(lib_robot ${SOURCE_LIB_ROBOT})

add_executable(mini_cheetah_node src/mini_cheetah_node.cpp)

add_dependencies(mini_cheetah_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(mini_cheetah_node ${catkin_LIBRARIES} lib_robot)
