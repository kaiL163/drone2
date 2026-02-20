import threading

from robomaster import robot

from camera import run_camera
from mission import run_mission


if __name__ == '__main__':
    tl_drone = robot.Drone()
    tl_drone.initialize()

    stop = threading.Event()

    camera_process = threading.Thread(target=run_camera, args=(stop,))
    mission_process = threading.Thread(target=run_mission)

    camera_process.start()
    mission_process.start()

    mission_process.join()
    stop.set()
    camera_process.join()

    tl_drone.close()





