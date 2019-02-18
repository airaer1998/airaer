#创建一个背景为蓝色的Pygame窗口
import sys
import pygame
from a_2 import SHIP

def bulid():
    pygame.init()
    screen=pygame.display.set_mode((800,800))
    pygame.display.set_caption("blue_window")
    screen.fill((0,120,230))

    ship=SHIP(screen)
    ship.blitme()
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

bulid()
