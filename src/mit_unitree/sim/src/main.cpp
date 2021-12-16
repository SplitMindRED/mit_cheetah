/*! @file main.cpp
 *  @brief Main function for simulator
 */

#include <stdio.h>
#include <unistd.h>

#include <QApplication>
#include <QSurfaceFormat>
#include <thread>

#include "Collision/CollisionPlane.h"
#include "DrawList.h"
#include "Dynamics/Cheetah3.h"
#include "Dynamics/DynamicsSimulator.h"
#include "Dynamics/FloatingBaseModel.h"
#include "Dynamics/MiniCheetah.h"
#include "Dynamics/Quadruped.h"
#include "Graphics3D.h"
#include "SimControlPanel.h"
#include "Simulation.h"
#include "Utilities/SegfaultHandler.h"
#include "Utilities/utilities.h"

/*!
 * Setup QT and run a simulation
 */
int main(int argc, char *argv[])
{
  install_segfault_handler(nullptr);
  // set up Qt
  QApplication a(argc, argv);

  // open simulator UI
  SimControlPanel panel;
  panel.show();

  // run the Qt program
  a.exec();

  return 0;
}
