import pygame, game_sprites
pygame.init()

SCREEN_WIDTH = 12500
SCREEN_HEIGHT = 1250
START_TIME = None

#GRAVITY=0.01
VIEW_WIDTH = 700
VIEW_HEIGHT = 500

KEYMAP = {
'tiltup': pygame.K_UP,
'tiltdown': pygame.K_DOWN,
'decel': pygame.K_a,
'accel': pygame.K_d
}

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
BLACK = (0,0,0)
SKYBLUE = (135,206,235)

LIFTC = 0.01
DRAGC =0.02
GRAVITY= 0.12
SCORE = 0

spawn_freq = 0
cloudlist= []
birdlist = []

FLAGS = pygame.RESIZABLE | pygame.DOUBLEBUF | pygame.SHOWN #| pygame.NOFRAME

PLAYER_ARGS = { 'x':325, 'y':250, 'w':89, 'h':20,
                            'rot_angle_constant':0.5, 'max_thrust_mag':0.5}
CLOUD_ARGS = {'w':80, 'h':40, 'cloudvelc':2.5}
BIRD_ARGS = {'w':40, 'h':20, 'birdvelx':4, 'birdvely':2}

RUN_PLANE_PHY = RUN_PLAYER_UPDATE = RUN_SIDESCROLL = True

GAMEMODE = 'Starting'
