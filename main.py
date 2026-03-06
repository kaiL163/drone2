import threading
from djitellopy import Tello
from mission import run_mission
from camera import run_camera

if __name__ == '__main__':
    tl_drone = Tello()
    tl_drone.connect()
    tl_drone.streamon()

    stop_event = threading.Event()
    
    camera_thread = threading.Thread(target=run_camera, args=(tl_drone, stop_event))
    mission_thread = threading.Thread(target=run_mission, args=(tl_drone,))

    camera_thread.start()
    mission_thread.start()

    mission_thread.join()
    stop_event.set()
    camera_thread.join()    

    tl_drone.streamoff()
    tl_drone.end()
