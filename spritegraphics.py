# Copyright (c) 2014 Andrew Cleland
# Graphics prototype for Physics 2D

import sys, pygame
import random
from Bodies import *
from vector import *


pygame.init()

# Constants:
size = width, height = 640, 480
vmax = 2
black = 0, 0, 0
blue = 0, 0, 255
white = 255, 255, 255
radius = 10
screen = pygame.display.set_mode(size)

# A class for drawing ball sprites
class BallSprite(pygame.sprite.Sprite):
    def __init__(self, ball):    # ball is an instance of Ball() class
        pygame.sprite.Sprite.__init__(self)
        self.ball = ball
        diameter = round(2 * ball.radius)
        self.pos = (round(ball.pos.x), round(ball.pos.y))
        #self.image = pygame.Surface((diameter, diameter))
        #self.image.fill(white) 
        #pygame.draw.circle(self.image, blue, (diameter//2,diameter//2), ball.radius)
        self.base_image = pygame.image.load('ball.png').convert_alpha()
        self.image = self.base_image
        self.rect = self.image.get_rect()

    def update(self, dt):
        self.ball.update(dt)
        self.rect.center = (round(self.ball.pos.x), round(self.ball.pos.y))
        #self = BallSprite(self.ball)



# User input:
n = int(input('Number of bodies: '))
gravity = float(input('Set gravity: '))
collisions_on = 'y' == input('Collision detection? (y/n?): ')

# Initialize ball sprites
ballsprites = []
for i in range(n):
    ballsprites.append(BallSprite(Ball(r=radius, x=random.random()*width, 
                        y=random.random()*height, 
                        vx=random.uniform(-1,1)*vmax, 
                        vy=random.uniform(-1,1)*vmax, ay=gravity)))

# Main loop
while True:
    # GUI exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    # Start by filling in the background color
    background = pygame.Surface(screen.get_size())
    background.fill(black)
    screen.blit(background, (0,0))

    # Draw the bodies
    for sprite in ballsprites:
        # Round positions to integer values
        pos = round(sprite.ball.pos.x), round(sprite.ball.pos.y)
        
        # Move body according to current velocity, acceleration
        sprite.update(dt=.1)
        
        if collisions_on:
            # Check for collisions
            for other in ballsprites:
                # Don't compare a body to itself
                if other == sprite:
                    continue
                # Fix overlaps
                if sprite.ball.overlaps(other.ball):
                    sprite.ball.collide(other.ball)


        # Bounce off edges
        if sprite.ball.left < 0 or sprite.ball.right > width:
            sprite.ball.velflipx()
        if sprite.ball.top < 0 or sprite.ball.bottom > height:
            sprite.ball.velflipy()
        
        # Draw the sprites
        screen.blit(sprite.image, sprite.rect)
    
    #screen.blit(ball, ballrect)
    pygame.display.flip()

