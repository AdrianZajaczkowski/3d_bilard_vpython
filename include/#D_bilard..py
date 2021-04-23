#!/usr/bin/env python3

from vpython import *
scene.forward = vector(-1,1,-1)
scene.up = vector(-1,1,1)
scene.height = 900
scene.width = 800
floor = box(pos=vector(0,0,0), size=vector(10,5,0.1) ,color = color.blue)

floor1 = box(pos=vector(0,2.5,0.2),size=vector(10.1,0.1,0.4), color = color.green)

floor2= box(pos=vector(0,-2.5,0.2),size=vector(10.1,0.1,0.4), color = color.green)


floor3 = box(pos=vector(5,0,0.2), size=vector(0.1,5,0.4), color = color.green)

floor4 = box(pos=vector(-5,0,0.2), size=vector(0.1,5,0.4), color = color.green)






ball1 = sphere(pos=vector(0,0,0.3),radius = 0.2,color = color.red)

ball2= sphere(pos=vector(0.35,0.2,0.3),radius = 0.2,color = color.green)

ball3 = sphere(pos=vector(0.35,-0.2,0.3),radius = 0.2,color = color.blue)



ball4 = sphere(pos=vector(0.7,0,0.3),radius = 0.2,color = color.yellow)

ball5 = sphere(pos=vector(0,0.4,0.3),radius = 0.2,color = color.black)

ball6 = sphere(pos=vector(0,-0.4,0.3),radius = 0.2,color = color.red)



##
'''
x=0.4 
nx=0.6


'''