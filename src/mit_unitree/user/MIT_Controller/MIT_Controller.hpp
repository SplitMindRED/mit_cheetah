#ifndef MIT_CONTROLLER
#define MIT_CONTROLLER

#include <RobotController.h>
#include <ros/ros.h>
#include <trajectory_msgs/JointTrajectory.h>

#include "Controllers/ContactEstimator.h"
#include "Controllers/GaitScheduler.h"
#include "FSM_States/ControlFSM.h"
#include "MIT_UserParameters.h"
//#include <gui_main_control_settings_t.hpp>

class MIT_Controller : public RobotController
{
public:
  MIT_Controller();
  virtual ~MIT_Controller()
  {
  }

  virtual void initializeController();
  virtual void runController();
  virtual void updateVisualization()
  {
  }
  virtual ControlParameters* getUserControlParameters()
  {
    return &userParameters;
  }
  virtual void Estop()
  {
    _controlFSM->initialize();
  }

protected:
  ControlFSM<float>* _controlFSM;
  // Gait Scheduler controls the nominal contact schedule for the feet
  GaitScheduler<float>* _gaitScheduler;
  MIT_UserParameters userParameters;
  ros::NodeHandle _nh;
  ros::Publisher _pub;
};

#endif
