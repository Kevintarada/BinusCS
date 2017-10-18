import pygame

from Alien_Invasion.Settings import Settings
from Alien_Invasion.Ship import Ship
from pygame.sprite import Group
import Alien_Invasion.game_functions as game_functions
from Alien_Invasion.Game_stats import GameStat
from Alien_Invasion.Button import Button
from Alien_Invasion.score_board import Scoreboard


def run_game():
    pygame.init()
    pygame.display.set_caption("Long long pew pew")

    setting = Settings()
    screen = pygame.display.set_mode((setting.screenWidth, setting.screenHeight))

    play_button = Button(setting, screen, "Play")
    stats = GameStat(setting)
    sb = Scoreboard(setting, screen, stats)

    ship = Ship(setting, screen)
    bullets = Group()
    aliens = Group()

    game_functions.create_fleet(setting, screen, ship, aliens)

    while True:

        game_functions.check_events(setting, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()

            game_functions.update_bullet(setting, screen, stats, sb, ship, aliens, bullets)
            game_functions.update_aliens(setting, stats, sb, screen, ship, aliens, bullets)

        game_functions.update_screen(setting, screen, ship, aliens, bullets, play_button, stats, sb)

run_game()
