
from ship import Ship
import pygame
from pygame.sprite import Group
from setting import Setting
from game_fuctions import check_event,update_screen


def run_game():
    ''''''
    pygame.init()
    ai_setting = Setting()
    screen = pygame.display.set_mode((ai_setting.width,ai_setting.height))
    pygame.display.set_caption('外星人大战')
    ship = Ship(ai_setting,screen)
    bullets = Group()

    while True:
        check_event(ai_setting,screen,ship,bullets)
        ship.update()
        bullets.update()
        update_screen(ai_setting,screen,ship,bullets)


if __name__ == '__main__':
    run_game()