import cv2
from robomaster import robot

def run_mission(tl_drone):
    tl_flight = tl_drone.flight

    tl_flight.mission_pad_on()

    tl_flight.takeoff().wait_for_completed()

    tl_flight.go(x=100, y=0, z=0, mid="")
    tl_flight.go(x=0, y=-150, z=0, mid="")
    tl_flight.go(x=-100, y=0, z=0, mid="")
    tl_flight.go(x=100, y=150, z=0, mid="")

    tl_flight.land().wait_for_completed()

    tl_flight.mission_pad_off()