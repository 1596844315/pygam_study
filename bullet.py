import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个队飞船发射的子弹的管理类"""

    def __init__(self,setting,screen,ship):
        """再飞船所处位置创建一个子弹对象"""
        # super(Bullet,self).__init__() #使用父类初始化函数
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0,0, #创建一个子弹大小的矩形
        setting.bullet_width,setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #用y来存储子弹当前位置
        self.y = float(self.rect.y)
        self.color = setting.bullet_color

        self.speed_factor = setting.bullet_speed

    def update(self, *args):
        '''更新子弹位置'''
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)