import time 
from dronekit import connect, VehicleMode, LocationGlobalRelative, Command, LocationGlobal
from pymavlink import mavutil
# # https://dronekit-python.readthedocs.io/en/latest/guide/taking_off.html 
# ----------Functions
# ---  Arm and takeoff 
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)

def arm_and_takeoff(altitude):
    while not vehicle.is_armable:
        print("waiting to be armable")
        time.sleep(1)

    print("Arming motors")
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed:
        time.sleep(1)

    print("Taking off")
    vehicle.simple_takeoff(altitude)

    # wait to reach the target altitude 
    while True:
        v_alt = vehicle.location.global_relative_frame.alt
        if v_alt >= altitude -1:
            print("altitude reached")
            break
        time.sleep(1)

# ------ Main Program -----
arm_and_takeoff(20)

# set the default speed 
vehicle.airspeed = 5

# -- Go to wp1 
print("go to wp1")
wp1 = LocationGlobalRelative(-35.363031, 149.159348, 20) # 
vehicle.simple_goto(wp1)

# Here we can do anything 
time.sleep(30)

# come back 
print("coming back ")
vehicle.mode = VehicleMode("RTL")
time.sleep(20)
vehicle.close()

# End 
