try:
  import pygame, math, random
  import game_sprites, phy, gamemenu, cam
  from constants import *
  import psutil
except:
  print("Missing required modules. Check requirements ")

pygame.init()

resizablesurface = pygame.display.set_mode([VIEW_WIDTH, VIEW_HEIGHT], FLAGS)
imageSprite = pygame.image.load("images/drawn_plane_white_89x20.png").convert_alpha()
pygame.display.set_icon(imageSprite)
screen = resizablesurface.copy()
pygame.display.set_caption("Flight Simulator")

clock = pygame.time.Clock()

# for cloudnum in range(4):
#   path = ("images/cloud{}.png".format(cloudnum))
#   cloud%d.format(cloudnum) = pygame.image.load(path).convert_alpha()

terrainImage = pygame.image.load("images/terrain_final4000dpi.png").convert_alpha()
rawbg = pygame.image.load("images/bg_trans_2000dpi.png").convert()

cloudSprite = pygame.image.load("images/clouds_trans.png").convert_alpha()
birdSprite = pygame.image.load("images/bird.png").convert_alpha()

terrain = pygame.transform.scale(terrainImage, (SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.transform.scale(rawbg, (SCREEN_WIDTH, SCREEN_HEIGHT))

player = game_sprites.Sprite(imageSprite, **PLAYER_ARGS)

camera = cam.Camera(VW = VIEW_WIDTH, VH = VIEW_HEIGHT, player = player)

Terrain = game_sprites.Terrain(terrain, surface=background)

# Pre-spawn some clouds and birds
for i in range(50):
    game_sprites.Cloud.cloudspawn(camera, 50, Terrain, cloudSprite, 150, 40)
    game_sprites.Bird.birdspawn(camera, 50, Terrain, birdSprite, 50, 3)

image_rect = background.get_rect()
surf = pygame.Surface((image_rect.width, image_rect.height))
surf.blit(background, image_rect)

RunAgain = False
FULLSCREEN= False

def mainloop():

  global START_TIME, VIEW_WIDTH, VIEW_HEIGHT, RUN_PLAYER_UPDATE, RUN_PLAYER_PHY, RUN_SIDESCROLL, GAMEMODE, FLAGS
  global resizablesurface, screen, clock, imageSprite, terrainImage, rawbg, cloudSprite, birdSprite, terrain, background, player, Terrain
  global image_rect, surf, spawn_freq, FULLSCREEN

  camera = cam.Camera(VW = VIEW_WIDTH, VH = VIEW_HEIGHT, player = player)

  # surf.blit(background, image_rect)

  for event in pygame.event.get():

    keydown=mousedown=False

    if event.type == pygame.QUIT:
          print('Window closed, quitting game...')
          quit()

    if event.type==pygame.KEYDOWN:
      keydown=True
    if event.type==pygame.MOUSEBUTTONDOWN:
      mousedown=True

    if keydown:

      if event.key == pygame.K_ESCAPE:
        print('Escape key pressed, quitting game...')
        quit()
      elif event.key == pygame.K_F11:
        if FULLSCREEN == False:
          FLAGS = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.SHOWN | pygame.FULLSCREEN
          resizablesurface = pygame.display.set_mode(resizablesurface.get_size(), FLAGS)
        else:
          FLAGS = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.SHOWN
          resizablesurface = pygame.display.set_mode((VIEW_WIDTH, VIEW_HEIGHT), FLAGS)
        FULLSCREEN = not FULLSCREEN

    if mousedown:

      if GAMEMODE == 'Menu':
        if event.button == 1:
          gamemenu.restart_program()
          player.RESTART_NEEDED = False

    if keydown or mousedown:

      if GAMEMODE == 'Starting':
        GAMEMODE = 'Running'
        START_TIME = pygame.time.get_ticks()

    if event.type == pygame.VIDEORESIZE:
      screen = pygame.display.set_mode(event.size, FLAGS)
      VIEW_HEIGHT, VIEW_WIDTH = event.h, event.w

  if START_TIME:
    gametime = (pygame.time.get_ticks() - START_TIME)/1000

  if GAMEMODE == 'Running':
    camera.CameraClip(surf)
    surf.blit(background, camera.rect, camera.rect)
    surf.blit(terrain, camera.rect, camera.rect)
    phy.PlanePhy(self=player)
    keys = pygame.key.get_pressed()
    player.render(surf)
    player.update(keys, KEYMAP, surf, RUN_PLAYER_UPDATE,3)
    if spawn_freq%30==0:
      game_sprites.Cloud.cloudspawn(camera, 50, Terrain, cloudSprite, 150, 40)
      game_sprites.Bird.birdspawn(camera, 50, Terrain, birdSprite, 50, 20)
    game_sprites.Bird.birdupdate(surf = surf)
    game_sprites.Cloud.cloudupdate(surf = surf, player = player)
    screen.blit(surf, (0,0), camera)
    gamemenu.flightscore(screen, gametime)
    fps_rn = clock.get_fps()
    gamemenu.showfps(screen, fps_rn)
    gamemenu.showThrust(screen, player.thrust.magnitude, player.max_thrust_mag)

    if player.RESTART_NEEDED:
      GAMEMODE = 'Menu'

  elif GAMEMODE == 'Menu':
      if player.RESTART_NEEDED:
        gamemenu.play_game(screen)
        player.RESTART_NEEDED = False

  elif GAMEMODE == 'Starting':
    screen.blit(surf, (0,0) )
    gamemenu.newgame(screen)

  try:
    resizablesurface.blit(pygame.transform.scale(screen, resizablesurface.get_rect().size), (0, 0))
  except:
    resizablesurface.blit(screen, (0,0) )
  pygame.display.update()
  pygame.event.pump()
  clock.tick(60)
  spawn_freq += 1

while True:
  mainloop()
