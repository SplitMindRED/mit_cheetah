#include <ros/ros.h>
//#include <SimulationBridge.h>
//#include "user/MIT_Controller/MIT_Controller.hpp"

int main(int argc, char** argv)
{
  ros::init(argc, argv, "mini_cheetah");
  ros::NodeHandle n;
  ros::Rate rate(10);

  ROS_INFO("Initialization...");

//  RobotType robotType = RobotType::MINI_CHEETAH;
//  MIT_Controller MITController;

//  SimulationBridge SimBridge(robotType, new MIT_Controller());

  ROS_INFO("Initialization done!");

  while (ros::ok())
  {
//    SimBridge.runRobotControl();


    ros::spinOnce();
    rate.sleep();
  }

  return 0;
}
