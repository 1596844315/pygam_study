import sys

import pygame
from bullet import Bullet

def check_keydown_event(event,ship,setting,screen,bullets):
    '''检查按键按下'''
    if event.key == pygame.K_RIGHT:#如果按下右键
        ship.move_right = True
    elif event.key == pygame.K_LEFT:#如果按下左键
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(setting,screen,ship,bullets)
def fire_bullet(setting,screen,ship,bullets):
    if len(bullets)< setting.bullet_allowed:
        new_bullet = Bullet(setting,screen,ship)
        bullets.add(new_bullet)
def check_keyup_event(event,ship):
    '''检查按键松开'''
    if event.key == pygame.K_RIGHT:#如果松开右键
        ship.move_right = False
    elif event.key == pygame.K_LEFT:#如果松开左键
        ship.move_left = False

def check_event(setting,screen,ship,bullets):
    '''检查鼠标和按键'''
    for event in pygame.event.get(): #轮询 当前事件
        if event.type == pygame.QUIT: #如果事件类型为退出游戏
            sys.exit()

        elif event.type == pygame.KEYDOWN: #如果按下键盘按键的事件
            check_keydown_event(event,ship,setting,screen,bullets)


        elif event.type == pygame.KEYUP: #如果放松键盘按键事件
            check_keyup_event(event,ship)


def update_screen(setting,screen,ship,bullets):
    '''更新屏幕图像'''

    screen.fill(setting.color) #填充背景颜色
    ship.blitme() #绘制飞船
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip() #所有图像展示出来

def update_bullets(bullets):
    '''消除多余子弹'''
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

