# Graphics prototype 
import sys, pygame
from Bodies import *
from vector import *
from random import random

pygame.init()

size = width, height = 640, 480
speed = vx, vy = 2, 2
black = 0, 0, 0
blue = 0, 0, 255
radius = 10

n = int(input('Number of bodies: '))
gravity = float(input('Set gravity: '))

screen = pygame.display.set_mode(size)

# Initialize bodies
bodies = []
for _ in range(n):
    bodies.append(Ball(r=radius, x=random()*width, y=random()*height,
                    vx=random()*vx, vy=random()*vy, ay=gravity))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    screen.fill(black)
    for body in bodies:
        pos = round(body.pos.x), round(body.pos.y)
        body.update(dt=.1)
        
        # Bounce off edges
        if body.left < 0 or body.right > width:
            body.velflipx()
        if body.top < 0 or body.bottom > height:
            body.velflipy()
        
        pygame.draw.circle(screen, blue, pos, round(body.radius))

    #screen.blit(ball, ballrect)
    pygame.display.flip()

