cmake_minimum_required(VERSION 3.0.2)
project(CV_Black_White)


find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  roscpp
  rospy
  sensor_msgs
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES CV_Black_White
#  CATKIN_DEPENDS cv_bridge image_transport roscpp rospy sensor_msgs std_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)


catkin_install_python(PROGRAMS
  scripts/Garycam_pub.py
  scripts/Garycam_sub.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})



