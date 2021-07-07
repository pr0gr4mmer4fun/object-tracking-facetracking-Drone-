from djitellopy import Tello
from utils import *
import cv2

w,h, = 360,240

def initializeTello():
    myDrone = Tello()
    myDrone.connect()
    myDrone.for_back_velocity = 0
    myDrone.left_right_velocity = 0
    myDrone.up_down_velocity = 8
    myDrone.yaw_velocity = 0
    myDrone.speed = 0
    print(myDrone.get_battery())
    myDrone.streamoff()
    myDrone.streamon()
    return myDrone

def tellogetframe(myDrone, w= 360,h=240):

    myFrame = myDrone.get_frame_read()
    myFrame = myFrame.frame
    img = cv2.resize(myFrame, (w,h))
    return img


myDrone = initializeTello()

while True:
    img = tellogetframe(myDrone,w,h)

    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        myDrone.land()
        break

from djitellopy import Tello
import keyboard as kp
from time import sleep

kp.init()
me = Tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardinput():
   lr, fb, up, yv, = 0, 0, 0, 0
   speed = 50

   if kp.getKey("LEFT"): lr = -speed
   elif kp.getKey("RIGHT"): lr = speed

   if kp.getKey("UP"): fb = speed
   elif kp.getKey("DOWN"): fb = -speed

   if kp.getKey("w"): ud = speed
   elif kp.getKey("s"): ud = -speed

   if kp.getKey("a"): yv = speed
   elif kp.getKey("d"): yv = -speed

   if kp.getKey("q"): yv = me.land()
   if kp.getKey("e"): yv = me.takeoff()

   return [lr, fb, up, yv]


while True:
   vals = getKeyboardinput()
   me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
   sleep(0.05)
