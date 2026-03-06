import time
from djitellopy import Tello

def run_mission(tl_drone):
    tl_drone.enable_mission_pads()
    tl_drone.set_mission_pad_detection_direction(2)

    tl_drone.takeoff()

    tl_drone.move_left(100)

    tl_drone.move_forward(100)
    tl_drone.go_xyz_speed_mid(0, 0, 120, 50, 1)
    tl_drone.move_forward(100)
    tl_drone.go_xyz_speed_mid(0, 0, 120, 50, 1)
    tl_drone.move_forward(100)
    tl_drone.go_xyz_speed_mid(0, 0, 120, 50, 1)

    tl_drone.move_right(100)
    tl_drone.go_xyz_speed_mid(0, 0, 120, 50, 1)
    tl_drone.move_right(100)
    tl_drone.go_xyz_speed_mid(0, 0, 120, 50, 1)

    tl_drone.move_back(100)
    tl_drone.go_xyz_speed_mid(0, 0, 120, 50, 1)

    time.sleep(3)

    tl_drone.move_left(100)
    tl_drone.go_xyz_speed_mid(0, 0, 120, 50, 1)

    time.sleep(3)

    tl_drone.go_xyz_speed(100, -50, 50, 50)

    tl_drone.land()

    tl_drone.disable_mission_pads()