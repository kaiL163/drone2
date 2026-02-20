import cv2
from robomaster import robot

def run_camera(tl_drone, stop):
    tl_camera = tl_drone.camera
    tl_camera.start_video_stream(display=False)
    tl_camera.set_fps("high")
    tl_camera.set_resolution("high")
    tl_camera.set_bitrate(6)
    
    while not stop.is_set():
        img = tl_camera.read_cv2_image()
        cv2.imshow("Drone", img)
        cv2.waitKey(1)

    cv2.destroyAllWindows()
    tl_camera.stop_video_stream()
    
