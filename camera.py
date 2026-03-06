import cv2

def run_camera(tl_drone, stop):
    frame_read = tl_drone.get_frame_read()

    while not stop.is_set():
        img = frame_read.frame
        cv2.imshow("Drone", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
