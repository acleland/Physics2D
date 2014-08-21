# Copyright (c) 2014 Andrew Cleland
# Graphics prototype for Physics 2D

import sys, pygame
from Bodies import *
from vector import *
from random import random

pygame.init()

# Constants:
size = width, height = 640, 480
vmax = 2
black = 0, 0, 0
blue = 0, 0, 255
radius = 10

# User input:
n = int(input('Number of bodies: '))
gravity = float(input('Set gravity: '))
collisions_on = 'y' == input('Collision detection? (y/n?): ')
screen = pygame.display.set_mode(size)

# Initialize bodies
bodies = []
for i in range(n):
    bodies.append(Ball(r=radius, x=random()*width, y=random()*height,
                    vx=random()*vmax, vy=random()*vmax, ay=gravity))

# Draw bodies and animate them:
while True:
    # GUI exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    # Start by filling in the background color
    screen.fill(black)

    # Draw the bodies
    for body in bodies:
        # Round positions to integer values
        pos = round(body.pos.x), round(body.pos.y)
        
        # Move body according to current velocity, acceleration
        body.update(dt=.1)
        
        if collisions_on:
            # Check for collisions
            for other in bodies:
                # Don't compare a body to itself
                if other == body:
                    continue
                # Fix overlaps
                if body.overlaps(other):
                    body.collide(other)


        # Bounce off edges
        if body.left < 0 or body.right > width:
            body.velflipx()
        if body.top < 0 or body.bottom > height:
            body.velflipy()
        
        # Draw the body
        pygame.draw.circle(screen, blue, pos, round(body.radius))

    #screen.blit(ball, ballrect)
    pygame.display.flip()

