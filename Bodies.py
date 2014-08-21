# Copyright (c) 2014 Andrew Cleland
# Bodies.py - a family of classes of physical objects

# Import vector class
from vector import *

class Thing():
    # Parent class representing anything that has a position in 2D space
    def __init__(self, x, y):
        self.pos = vector(x, y)

class Body(Thing):
    # A physical body that allows for translational motion
    def __init__(self, x, y, vx=0, vy=0, ax=0, ay=0, mass=1):
        super(Body, self).__init__(x, y)
        self.mass = mass
        self.vel = vector(vx, vy)
        self.acc = vector(ax, ay)  # Things start off with no acceleration
    
    def setBounds(self):
        pass

    def update(self, dt=1, force=vector(0, 0)):
        #self.acc = force / self.mass   # Newton's 2nd law
        self.vel += self.acc * dt
        self.pos += self.vel * dt
        self.setBounds()

    def velflipx(self):
        self.vel = vector(-self.vel.x, self.vel.y)
    
    def velflipy(self):
        self.vel = vector(self.vel.x, -self.vel.y)
         
class Ball(Body):
    # A body whose shape is a circle.
    def __init__(self, r, x, y, vx=0, vy=0, ax=0, ay=0, mass=1):
        super(Ball, self).__init__(x, y, vx, vy, ax, ay, mass)
        self.radius = r
        self.setBounds()
    
    def setBounds(self):
        # Marks the boundary edges of the ball. 
        self.left = self.pos.x - self.radius
        self.right = self.pos.x + self.radius
        self.top = self.pos.y - self.radius
        self.bottom = self.pos.y + self.radius
    
    def overlaps(self, other):
        # Detects if it overlaps with another ball, and if so, corrects it.
        
        vecdiff = other.pos - self.pos  # Vector pointing from self to other
        dist = vecdiff.mag()      # Distance between centers
        overlapping = dist < self.radius + other.radius
        
        if overlapping:
            # Adjust ball positions so that they are just touching on the edges
            overlap = self.radius + other.radius - dist
            # Move self by half the overlap distance:
            self.pos -= vecdiff / dist * overlap / 2
            # Move other by half the overlap distance:
            other.pos += vecdiff / dist * overlap/2
        
        return overlapping



if __name__ == '__main__':
    body = Body(1,2)
    body.pos.print()

    thing = Thing(3,4)
    thing.pos.print()

    ball = Ball(5, 5, 6)
    ball.pos.print()
    ball.vel.print()
    print(ball.mass)
    print(ball.radius)

