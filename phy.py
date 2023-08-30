import math
import pygame
from constants import SCREEN_HEIGHT, LIFTC, DRAGC, GRAVITY

def PlanePhy(self, toRun=True):

  angle = math.radians(self.angle)
    
  if self.rect.y < SCREEN_HEIGHT-self.rect.height:
    self.vel += pygame.math.Vector2(0, GRAVITY)

  wingarea = 0.1 + abs(math.cos(angle))
  vel_angle = math.atan2(-self.vel.y,self.vel.x) #Angle of velocity
                                                              #vector
  
  p = vel_angle if vel_angle >= 0 else vel_angle + math.pi*2

  dragarea=0.01+abs(math.sin(p-angle))
  # print('Angles: ', p, '-', angle)
  # print("sine: ", math.sin(p-angle))
  # print('Diff: ', p-angle)
  
  FLUID_DENSITYV = 1
  # if self.rect.y <= 30:
  #   FLUID_DENSITYV = 0
  #   self.magnitude = 0
  #   self.vel.y = -0.0001
    
  # elif self.rect.y<70:
  #   FLUID_DENSITYV = 0.1
  #   self.vel.y = -0.001

  # elif self.rect.y<95:
  #   FLUID_DENSITYV = 0.4
  #   self.vel.y = -0.01

  # elif self.rect.y < 120:
  #   FLUID_DENSITYV = 0.6
  #   self.vel.y += -self.vel.y/2

  # elif self.rect.y < 180:
  #   FLUID_DENSITYV = 0.7
  #   self.vel.y += -self.vel.y/4

  # elif self.rect.y < 210:
  #   FLUID_DENSTIYV = 0.9
  #   self.vel.y += -self.vel.y/6
    
  lift = LIFTC*(abs(self.vel.x**2))*wingarea*FLUID_DENSITYV
  # print('Lift: ', lift)

  if lift > GRAVITY:
    lift = GRAVITY
    
  # lift = (self.vel.normalize().rotate(90)) *self.vel.magnitude_squared()*LIFTC*wingarea

  # lift = pygame.Vector2(0,0) #only for testing. I am definitely not just giving up.

  drag = self.vel.normalize()*self.vel.magnitude_squared()*DRAGC*dragarea
  # print('Wingarea:', wingarea, 'Lift:',lift, 'Drag:', drag, 'Vel_mag:',self.vel.magnitude(),"VEL", self.vel, "angle:", self.angle)
  
  if abs(self.vel.y) - abs(drag.y)>0 and abs(self.vel.x) - abs(drag.x) >0:
    self.vel = self.vel - drag
    #print('Applied drag (passed limiting condition)')
    
# if self.rect.y>self.rect.height:
  self.vel.y=(self.vel.y)-lift