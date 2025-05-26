from vector import Vector2
import pygame

BOUNCE_CONST = 0.9
FRICTION_CONST = 0.7
AIR_RESTANCE = 0.3



class Ball:
    def __init__(self, x, y, radius, red, green, blue, grav, width, height, delta, mode="reg"):
        self.pos = Vector2(x, y)
        self.radius = radius
        self.red = red
        self.green = green
        self.blue = blue
        self.grav = Vector2(0, grav)
        self.velo = Vector2(0, 0)
        self.width = width
        self.height = height
        self.delta = delta
        self.mode = mode
        self.mass = 1
        self.counter = 0
        self.saved = [self.pos]
        self.color = 0x555555
        self.cycle = False

    def setVelo(self, velocity):
        self.velo = velocity
    
    def boostX(self, boost):
        if self.velo.x != 0:
            self.velo.x = self.velo.x * boost
        else:
            self.velo.x = self.velo.x + boost
            

    def boostY(self, boost):
        if self.velo.y != 0:
            self.velo.y = self.velo.x * boost
        else:
            self.velo.x = self.velo.x + boost

    def setMass(self, mass):
        self.mass = mass

    def mouseSub(self, mousePos):
        return mousePos.pointBetween(self.pos).mult(1)

    def setVeloOffMouse(self, mousePos):
        self.velo = self.mouseSub(mousePos)



    def update(self, thickness):
        widthDelta = self.width - self.radius
        heightDelta = self.height - self.radius
        radiusDelta = self.radius + thickness

        self.velo = self.velo.add(self.grav.mult(self.mass))
        self.pos = self.pos.add(self.velo.mult(self.delta)) 

        self.saved.append(self.pos)

        if len(self.saved) > 250:
            del self.saved[0]

        

        x = self.pos.x
        y = self.pos.y



        if x > widthDelta:
            self.pos.x = widthDelta
        elif x < radiusDelta:
            self.pos.x = radiusDelta
        if y > heightDelta:
            self.pos.y = heightDelta
        elif y < radiusDelta:
            self.pos.y = radiusDelta

        if self.mode == "bounce":
            if x > widthDelta or x < radiusDelta:
                self.velo.x = (self.velo.x * -BOUNCE_CONST)

            elif y > heightDelta or y < radiusDelta:
                self.velo.y = self.velo.y * -BOUNCE_CONST

            
            
    def clearTrail(self):
        self.saved.clear()

    def render(self, screen, thickness=10):
        self.update(thickness)
        if len(self.saved) > 1:
            for i in range(1, len(self.saved)):
                #self.color = self.color - 1 no does not work :(
                #print(self.color)
                pygame.draw.line(screen, self.color, [self.saved[i - 1].x, self.saved[i - 1].y], ([self.saved[i].x, self.saved[i].y]), 1)

        pygame.draw.circle(screen, (self.red, self.blue, self.green), [self.pos.x, self.pos.y], self.radius, self.radius)
        
        
        


