import pygame


class Ship():

    def __init__(self,setting,screen):
        '''初始化飞船'''

        self.screen = screen

        self.move_right = False #是不是应该往右边走
        self.move_left = False #检查是否应该向左边移动

        self.image = pygame.image.load('resource/rocket.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.setting = setting #设置飞船速度

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        '''更新飞船位置'''
        if self.move_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx += self.setting.ship_speed

        if self.move_left and self.rect.left>self.screen_rect.left:
            self.rect.centerx -= self.setting.ship_speed

