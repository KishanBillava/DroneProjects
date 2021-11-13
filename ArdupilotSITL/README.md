# Ardupilot SITL GCS MAVProxy DroneKit Linux

#### Ardupilot -- ArduCopter
#### SITL Simulator (Software in the Loop) 
#### Mission Planner Simulation 
#### QGroundControl
#### MAVProxy Pymavlink 
#### DroneKit
#### Gazebo 
#### Linux Ubuntu 20.04






## Setting up the Build Environment (Linux/Ubuntu)  [Source](https://ardupilot.org/dev/docs/building-setup-linux.html#building-setup-linux)


Git command line
```
sudo apt-get update
sudo apt-get install git
sudo apt-get install gitk git-gui
```

Cloning with the command line -
Ardupilot repo : https://github.com/ArduPilot/ardupilot  
clone your fork
```
git clone https://github.com/your-github-userid/ardupilot
cd ardupilot
git submodule update --init --recursive
```

Install some required packages
```
Tools/environment_install/install-prereqs-ubuntu.sh -y
. ~/.profile
```
Log off and Log back again 


## Setting up SITL on Linux  [Source](https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html) 


Start SITL simulator
```
cd ardupilot/ArduCopter
sim_vehicle.py -w
sim_vehicle.py --console --map
```
![image](https://user-images.githubusercontent.com/84302215/141613076-917673c0-5c92-4dc7-b2fc-54b2b675a453.png)


## Using SITL [Source](https://ardupilot.org/dev/docs/using-sitl-for-ardupilot-testing.html#using-sitl-for-ardupilot-testing)  

Using SITL for ArduPilot Testing
```
command :  sim_vehicle.py -v ArduPlane -f quadplane --console --map

sim_vehicle.py → This is the simulation 
-v ArduPlane  →  this selects the vehicle type 
-f quadplane →  this select the frame type for selected vehicle
--console  →  selects the ground station console window 
--map  →  this enables the map 
--osd    →   the OSD emulation displays OSD panel items and locations
```


### Testing mavproxy commands 

```
Prepare for take off →  qloiter
arm the throttle       →  arm throttle
help →  will display mavproxy commands 
Here the normal throttle is input on channel 3, we want to lift off and raise the throttle 
command :  rc 3 1700
```
```
set the wind speed for 4 meter per second : → param set SIM_WIND_SPD 4
take off and flying : →  qhover
change the RTL mode → param set Q_RTL_MODE 1
command : →  cruise
now turn cruiseing around channel 1  and 1300 left turn  →   rc 1 1300
and set up rc 1 1500 to stop turning 
```
![image](https://user-images.githubusercontent.com/84302215/141613003-e6f1f584-d33b-4302-aeb4-1c9bc947ce1e.png)

```
go to map after changing to guided mode →  mode guided 
```
```
Load  a pre-existing waypoint file with the WP load command  : →
command : →  wp load ../Tools/autotest/Generic_Missions/CMAC-circuit.txt 
and make to auto
```
```
rtl -→ will set it to home 
qrtl → 
```
```
Load the graphing module to mavproxy : →  module load graph
→ graph SERVO_OUTPUT_RAW.servo5_raw SERVO_OUTPUT_RAW.servo5_raw
→  qloiter 
→   arm throttle
→  rc 3 1600
→  FBWA
```
```
Restarting the sim 
disarm 
reboot
```





