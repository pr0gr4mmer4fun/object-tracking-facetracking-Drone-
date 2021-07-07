from djitellopy import tello
import keyboard_module as kp
from time import sleep

kp.keyboard_module()
me = tello.Tello()
me.connect()
print(me.get_battery())

def getKeyboardinput():
   lr, fb, up, yv, = 0, 0, 0, 0
   speed = 50

   if kp.keyboard("LEFT"): lr = -speed
   elif kp.keyboard("RIGHT"): lr = speed

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
