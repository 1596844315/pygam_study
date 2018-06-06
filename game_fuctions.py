import sys

import pygame


def check_event(ship):
    '''检查鼠标和按键'''
    for event in pygame.event.get(): #轮询 当前事件
        if event.type == pygame.QUIT: #如果事件类型为退出游戏
            sys.exit()

        elif event.type == pygame.KEYDOWN: #如果按下键盘按键的事件
            if event.key == pygame.K_RIGHT: #如果按的是右键
                ship.move_right = True
            elif event.key == pygame.K_LEFT: #如果按的是左键
                ship.move_left = True


        elif event.type == pygame.KEYUP: #如果放松键盘按键事件
            if event.key == pygame.K_RIGHT: #如果松开右键
                ship.move_right = False  #该
            elif event.key == pygame.K_LEFT:#如果松开左键
                ship.move_left = False


def update_screen(setting,screen,ship):
    '''更新屏幕图像'''

    screen.fill(setting.color) #填充背景颜色
    ship.blitme() #绘制飞船

    pygame.display.flip() #所有图像展示出来