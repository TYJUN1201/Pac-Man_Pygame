from pygame import joystick, key
from pygame.locals import *

joystick.init()
joystick_count = joystick.get_count()

if (joystick_count > 0):
    joyin = joystick.Joystick(0)
    joyin.init()

#pygame.init() function call, which always needs to be called after importing the pygame module and before calling any other Pygame function.
#You don’t need to know what this function does, you just need to know that it needs to be called first in order for many Pygame functions to work.
#If you ever see an error message like pygame.error: font not initialized, check to see if you forgot to call pygame.init() at the start of your program.

def checkInput(p):
    global joyin, joystick_count
    xaxis = yaxis = 0
    if joystick_count > 0:
        # if 
        xaxis = joyin.get_axis(0)
        yaxis = joyin.get_axis(1)
        #0 --> x-axis, 1 --> y-axis
    if key.get_pressed()[K_LEFT] or key.get_pressed()[K_a] or xaxis < -0.8:
        # if press left arrow or a
        # or
        p.angle = 180
        #change Pacman image direction 
        p.movex = -20
        #moving speed, once move 20 pixel
    if key.get_pressed()[K_RIGHT] or key.get_pressed()[K_d]  or xaxis > 0.8:
        p.angle = 0
        p.movex = 20
    if key.get_pressed()[K_UP] or key.get_pressed()[K_w]  or yaxis < -0.8:
        p.angle = 90
        p.movey = -20
    if key.get_pressed()[K_DOWN] or key.get_pressed()[K_s]  or yaxis > 0.8:
        p.angle = 270
        p.movey = 20
