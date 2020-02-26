#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from pybricks.ev3devio import Ev3devSensor 
import utime
import ev3dev2
from ev3dev2.port import LegoPort

class MySensor(Ev3devSensor):  #Define Class 
    _ev3dev_driver_name="ev3-analog-01"
    #do not forget to set port mode to EV3-Analog 
    def readvalue(self):
        self._mode('ANALOG')
        return self._value(0)


# Before running the code go to Device Browser and Sensors. Make sure you can see ev3-analog-01, otherwise you will get an error.

# Write your program here
def main():
    brick.sound.beep()
    sens1 = LegoPort(address ='ev3-ports:in1') # which port?? 1,2,3, or 4
    #sens2 = LegoPort(address ='ev3-ports:in2') # which port?? 1,2,3, or 4
   
    sens1.mode = 'ev3-analog'
    #sens2.mode = 'ev3-analog'
   
    utime.sleep(0.5)

    sensor_left=MySensor(Port.S1) # same port as above
    sensor_right=MySensor(Port.S2) # same port as above

    left_motor = Motor(Port.A)
    right_motor = Motor(Port.D)
    speed = 0
    value = 100

    while True:
        left_color = sensor_left.readvalue()
        right_color = sensor_right.readvalue()
        print('left sensor is ', left_color)
        print('right sensor is ', right_color)
        left_motor.run(speed)
        right_motor.run(speed)

        #while left_color > value:  #if left sensor sees the black line
            #left_motor.run(speed)
            #right_motor.run(speed + 200) #turn left

        #while right_color > value:  #if right sensor sees the black line
            #right_motor.run(speed)
            #left_motor.run(speed + 200)  #turn right
        
main()

