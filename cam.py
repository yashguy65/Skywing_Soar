import pygame

class Camera():
  def __init__(self, VW, VH, player):
    
    self.rect = pygame.Rect(0, 0, VW, VH)
    self.rect.center = (player.x, player.y)

  def CameraClip (self, surf):
    
    if self.rect.top <= 0:
      self.rect.top = 0
    if self.rect.bottom >= surf.get_height():
      self.rect.bottom = surf.get_height()
    if self.rect.left <= 0:
      self.rect.left = 0
    if self.rect.right >= surf.get_width():
      self.rect.right = surf.get_width()
    return self
      