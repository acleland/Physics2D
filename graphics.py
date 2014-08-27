# Copyright (c) 2014 Andrew Cleland
# Graphics prototype for Physics 2D

import sys, pygame
import random
from Bodies import *

# Initialize pygame and pygame clock
pygame.init()
clock = pygame.time.Clock()

# Constants:
size = width, height = 500, 500
vmax = .25 * width   # pixels per second
black = 0, 0, 0
blue = 0, 0, 255
white = 255, 255, 255
radius = 1/50 * width 
bgcolor = white
ballcolor = blue
maxfps = 60

# User input:
n = int(input('Number of bodies: '))
gravity = float(input('Set gravity: '))
collisions_on = 'y' == input('Collision detection? (y/n?): ')
screen = pygame.display.set_mode(size)

# Initialize bodies
bodies = []
for i in range(n):
    bodies.append(Ball(r=radius, x=random.random()*width, 
                        y=random.random()*height, 
                        vx=random.uniform(-1,1)*vmax, 
                        vy=random.uniform(-1,1)*vmax, ay=gravity))

# Draw bodies and animate them:
while True:
    # get time passed, limit frame rate
    delta_t = clock.tick(maxfps)
    # GUI exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            print(clock.get_fps())
            sys.exit()
    
    # Start by filling in the background color
    screen.fill(bgcolor)

    # Draw the bodies
    for body in bodies:
        # Round positions to integer values
        pos = round(body.pos.x), round(body.pos.y)
        
        # Move body according to current velocity, acceleration
        body.update(dt = 1/maxfps)

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
            if body.left < 0:
                body.setPos(body.radius, body.pos.y)
            elif body.right > width:
                body.setPos(width - body.radius, body.pos.y)
        if body.top < 0 or body.bottom > height:
            body.velflipy()
            if body.top < 0:
                body.setPos(body.pos.x, body.radius)
            elif body.bottom > height:
                body.setPos(body.pos.x, height - body.radius)
        
        # Draw the body
        pygame.draw.circle(screen, ballcolor, pos, round(body.radius))

    pygame.display.flip()

