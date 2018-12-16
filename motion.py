# -*- coding:utf-8 -*-
"""
接线方式
PCA9685  ----  ESP32
  GND    ----  GND
  SCL    ----  P25
  SDA    ----  P26
  VCC    ----  3.3V
  V+     ----  5V外接电源
"""
import math as m
import calculation
import utime
from servo import Servos
from machine import I2C,Pin
gpio_scl=25
gpio_sda=26
res=50        #提高分辨率以减少舵机卡顿,但需要更高的计算需求
delay=1000    #减少延迟可提高舵机运动的速度,但需要更高的计算需求,单位微妙
#定义用于储存哥舵机角度的数组
#A(X)表示X通道舵机当前角度,B(X)表示X通道舵机目标角度
A=[90, 120, 120,            #左臂
   90, 120, 120,            #右臂
   90, 64.4368, 54.6566,    #左腿
   90, 64.4368, 54.6566,    #右腿
   90, 90]                  #腰
B=A

scl_pin=Pin(gpio_scl)       #初始化i2c和Servos
sda_pin=Pin(gpio_sda)
i2c=I2C(scl=scl_pin,sda=sda_pin,freq=10000)
servos=Servos(i2c,address=0x40)

def init():            #初始化到标准姿态
    H=m.sqrt(3)*l
    A=[90, 120, 120, 90, 120, 120, 90, 64.4368, 54.6566, 90, 64.4368, 54.6566, 90, 90]
    B=A
    for i in len(A):
        servo.position(i,A(i))
    return 0

def left_arm(x,y,z):
    A(0)=arm_top(x,y,z)
    A(1)=arm_mid(x,y,z)
    A(2)=arm_bottom(x,y,z)
def right_arm(x,y,z):
    A(3)=arm_top(x,y,z)
    A(4)=arm_mid(x,y,z)
    A(5)=arm_bottom(x,y,z)
def left_leg(x,y,z):
    A(6)=leg_top(x,y,z)
    A(7)=leg_mid(x,y,z)
    A(8)=leg_bottom(x,y,z)
def right_leg(x,y,z)
    A(9)=leg_top(x,y,z)
    A(10)=leg_mid(x,y,z)
    A(11)=leg_bottom(x,y,z)
def waist(L,Ang):
    A(12)=waist_left(L,Ang)
    A(13)=waist_right(L,Ang)

def activate():        #一次运动前所有目标角度确定后,使用activate()运动
    for j in range(res):
        for i in range(len(A)):
                servos.position(i,A(i)+(B(i)-A(i))/res*j)
        utime.sleep_us(delay)
    for i in range(len(A)):
        A(i)=B(i)
    return 0

#######################################
#以下函数用于储存机器人的动作
#######################################

def walk(speed,Ang):
    delay=speed


def run(Ang):

def turnleft(Ang):

def turnright(Ang):




if __name__=="__main__":
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    z=int(input("Enter z:"))
    left_arm(x,y,z)
    activate()