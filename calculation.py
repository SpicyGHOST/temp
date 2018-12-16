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

#以下变量计算时将被视为常量
l=100            #尺骨，桡骨，股骨，拓骨长度，常量
l2=m.sqrt(3)/2*l   #腓骨长度，常量 
H=m.sqrt(3)*l

def pol(x,y):
    return m.sqrt(x**2+y**2)

def arm_top(x,y,z):
    return m.degrees(m.atan(y/(H-z)))
def arm_mid(x,y,z):
    return 90+m.degrees(m.acos(0.5*pol(x,pol(y,H-z))/l))
def arm_bottom(x,y,z):
    return 2*m.degrees(m.asin(0.5*pol(x,pol(y,H-z))/l))

def leg_top(x,y,z):
    return m.degrees(m.atan(y/(H-z)))
def leg_mid(x,y,z):
    return 90-m.degrees(m.atan(x/(pol(y,H-z))))-m.degrees(m.acos((l**2+pol(x,pol(y,H-z))**2/4-l2**2/4)/(l*pol(x,pol(y,H-z)))))
def leg_bottom(x,y,z):
    return m.degrees(m.acos((l**2+l2**2/4-pol(x,pol(y,H-z))**2/4)/l/l2))

def waist_left(L,Ang):
    return 
def waist_right(L,Ang):
    return

if __name__=="__main__":
    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    z=int(input("Enter z:"))
    print(arm_top(x,y,z))
    print(arm_mid(x,y,z))
    print(arm_bottom(x,y,z))

    x=int(input("Enter x:"))
    y=int(input("Enter y:"))
    z=int(input("Enter z:"))
    print(leg_top(x,y,z))
    print(leg_mid(x,y,z))
    print(leg_bottom(x,y,z))