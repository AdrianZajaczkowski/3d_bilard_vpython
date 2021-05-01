#!/usr/bin/env python3

from vpython import *

scene.center = vector(0, 0, 0)
scene.forward = vector(1, 1, -1)
scene.up = vector(1, 1, 1)
scene.width = 1000
scene.height = 700

floor = box(pos=vector(0, 0, 0), size=vector(20, 40, 0.01), axis=vector(0, 0, 0), color=color.green)

wall1 = box(pos=vector(0, 20, 0), size=vector(21, 1, 3), axis=vector(0, 0, 0), color=color.green,lenght=40)
wall2 = box(pos=vector(0, -20, 0), size=vector(21, 1, 3), axis=vector(0, 0, 0), color=color.green,lenght=40)
wall3 = box(pos=vector(10, 0, 0), size=vector(1, 41, 3), axis=vector(0, 0, 0), color=color.green,lenght=40)
wall4 = box(pos=vector(-10, 0, 0), size=vector(1, 41, 3), axis=vector(0, 0, 0), color=color.green,lenght=40)


white = sphere(pos=vector(0, 14, 1),radius = 1,color = color.white,velocity=vector(0,-4,0))  # white ball start sequence 
green = sphere(pos=vector(0, -4, 1),radius = 1,color = color.green,velocity=vector(0,0,0))
blue = sphere(pos=vector(1, -6, 1),radius = 1,color = color.blue,velocity=vector(0,0,0))
red = sphere(pos=vector(-1.05, -6, 1),radius = 1,color = color.red,velocity=vector(0,0,0))
black = sphere(pos=vector(-2.1, -8, 1),radius = 1,color = color.black,velocity=vector(0,0,0))
yellow = sphere(pos=vector(0, -8, 1),radius = 1,color = color.yellow,velocity=vector(0,0,0))
orange = sphere(pos=vector(2.1, -8, 1),radius = 1,color = color.orange,velocity=vector(0,0,0))

balls_color=[white,black,green,yellow,blue,orange,red] # list of balls 

def impact_wall(color):
    if color.pos.x >= (wall3.pos.x - color.radius) or color.pos.x <= (wall4.pos.x + color.radius): # impact to horizontal walls
        color.velocity.x *= -1
    elif color.pos.y >= (wall1.pos.y -  color.radius) or color.pos.y <= (wall2.pos.y + color.radius): 
        color.velocity.y *= -1
    

def ballVelocity(color):
    color.pos = color.pos + color.velocity * dt # aceleration at dt 

def impact_balls(first,second):
    distance = mag(first.pos - second.pos)  
    separation = first.pos - second.pos
    contactSeparation = separation.norm() * (first.radius + second.radius)
    if separation.mag < contactSeparation.mag:
        elasticForce = - elasticConst * (separation - contactSeparation)
        second.velocity = second.velocity - (elasticForce * dt)
        first.velocity = first.velocity + (elasticForce * dt)
        
dt=0.1
elasticConst = 50
while True:
    rate(100)

    for color in range(len(balls_color)):
        ballVelocity(balls_color[color])
        impact_wall(balls_color[color])
        for s_color in range(color,len(balls_color)):
            impact_balls(balls_color[color],balls_color[s_color])
           