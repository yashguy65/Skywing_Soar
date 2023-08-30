import pygame
import pygame.freetype
import os, sys, psutil, logging #os, sys and logging are inbuilt
from constants import *
from math import sqrt

pygame.init()
pygame.font.init()

def print_text(text, fontsize, textcolor, bgcolor, isbold):
    font = pygame.freetype.SysFont("Consolas", fontsize, bold=isbold)
    surface, _ = font.render(text=text, fgcolor=textcolor, bgcolor=bgcolor)
    return surface.convert_alpha()

def restart_program():
    try:
        psy = psutil.Process(os.getpid())  #gives id of memory process
        for handler in psy.open_files() + psy.connections():    #sees files open using memory id
            os.close(handler.fd)     #closes the files given by loop
    except Exception as exc:  #wildcard* exception
        logging.error(exc)    #should give a summary of what made program crash ig
    python = sys.executable   #path for executable binary python (bytecode for specific processor)
    os.execl(python, python, *sys.argv)  #execl causes running process 'python' to be replaced by program passed as arguments

def play_game(screen):
    global SCORE
    text1 = 'SCORE: '+SCORE+' CLICK TO TRY AGAIN'
    #text1 = 'CLICK ANYWHERE TO PLAY AGAIN'
    playagainbox = print_text(text1, 17, WHITE, None, False)
    againrect = playagainbox.get_rect(center = (screen.get_width()/2, screen.get_height()/2))
    screen.blit(playagainbox, againrect)

def quit_program():
    pygame.time.wait(1000)
    pygame.quit()
    sys.exit()

def newgame(screen):
    newgame_box = print_text('SKYWING SOAR', 46, BLACK, None, True)
    helpmsg = print_text('ESC: exit | A: accelerate | D: decelerate | UP, DOWN: Rotate | F11: Fullscreen', 10, BLUE, None, False)
    presskeymsg = print_text('PRESS ANY KEY TO START', 9, RED, None, True)
    wt, ht = screen.get_width(), screen.get_height()
    keymsg_rect = presskeymsg.get_rect(center = (wt/2, ht*2/3))
    newgame_rect = newgame_box.get_rect(center=(wt/2, ht*1/3))
    help_rect = helpmsg.get_rect(center = (wt/2, ht*3/4))
    screen.blit(newgame_box, newgame_rect)
    screen.blit(presskeymsg, keymsg_rect)
    screen.blit(helpmsg, help_rect)
    
def flightscore(screen, time):
    global SCORE
    SCORE = str(int(time))
    text1 = 'SCORE: ' + SCORE
    score = print_text(text1, 16, WHITE, None, True)
    wt = screen.get_width()
    ht = screen.get_height()
    scorebox = score.get_rect(center = (wt*34/40, ht*39/40))
    screen.blit(score, scorebox)
    flightscore.finalscore = str(int(time))
    
def showfps(screen, fps):
    text1 = 'FPS: ' + str(int(fps))
    fps_text = print_text(text1, 16, WHITE, None, True)
    wt = screen.get_width()
    ht = screen.get_height()
    fps_rect = fps_text.get_rect(center = (wt*34/40, ht*1/40))
    screen.blit(fps_text, fps_rect)
    
'''
def showThrust(screen, thrust, max_thrust):
    #net_thrust = sqrt(thrust[0]**2 + thrust[1]**2)
    net_thrust = round(thrust, 5) 
    thrust_percent = int(net_thrust/max_thrust * 100)
    text1 = ' THRUST: ' + str(thrust_percent) + '%'

    thrustxt = print_text(text1, 16, WHITE, None, True)
    wt, ht = screen.get_width(), screen.get_height()
    thrust_rect = thrustxt.get_rect(center = (wt*5/40, ht*39/40))
    screen.blit(thrustxt, thrust_rect)
'''

def showThrust(screen, thrust, max_thrust):
    wt, ht = screen.get_width(), screen.get_height()
    net_thrust = round(thrust, 5) 
    thrust_percent = (net_thrust/max_thrust * 100)
    box_w, box_h = 10, 50
    thrust_height = (thrust_percent) * box_h /100
    pygame.draw.rect(screen, WHITE, (wt*4/40, ht*34/40, box_w, box_h))
    pygame.draw.rect(screen, GREEN, (wt*4/40, ht*34/40 - thrust_height+ box_h, box_w, thrust_height))
    pygame.draw.rect(screen, WHITE, ((wt*4/40) -10 + box_w/2, ht*34/40 - thrust_height + box_h-4, 20, 8))

    desc = print_text('THRUST', 12, WHITE, None, True)
    desc_rect = desc.get_rect(center = (wt*4/40+ box_w/2, ht*34/40 + box_h + 9))
    screen.blit(desc, desc_rect)
    
