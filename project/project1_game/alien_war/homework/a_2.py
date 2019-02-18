#将一幅位图转换为位图，创建一个类，将该角色绘制到屏幕中央，并将该图像的背景色设置为屏幕背景色，或将屏幕背景色设置为该图像的背景色
import pygame

class SHIP(object):

    def __init__(self,screen):
        self.screen=screen

        self.image=pygame.image.load("../alien_war/image/ship.bmp")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.center=self.screen_rect.center

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)


