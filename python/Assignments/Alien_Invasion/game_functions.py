import pygame
import sys
from Alien_Invasion.Bullet import Bullet
from Alien_Invasion.alien import Alien
from time import sleep

def ship_hit(setting, stats, sb, screen, ship, aliens, bullets):
    if stats.ships_left  > 0:
        stats.ships_left -= 1

        sb.prep_ships()
        aliens.empty()
        bullets.empty()

        create_fleet(setting, screen, ship, aliens)
        ship.center_ship()

        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_events(setting, screen, stats, sb, play_button, ship, aliens, bullets):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                check_Keydown(event, setting, screen, ship, bullets)

            elif event.type == pygame.KEYUP:
                check_Keyup(event, ship)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_play_button(setting, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(setting, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        setting.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        sb.prep_high_score()
        sb.prep_score()
        sb.prep_ships()

        create_fleet(setting, screen, ship, aliens)
        ship.center_ship()

def check_Keydown(event, setting, screen, ship, bullets):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            ship.moving_left = True

        elif event.key == pygame.K_SPACE:
            fire_bullet(setting, screen, ship, bullets)

        elif event.key == pygame.K_q:
            sys.exit()

def fire_bullet(setting, screen, ship, bullets):
    if len(bullets) < setting.bullet_allowed :
        new_bullet = Bullet(setting, screen, ship)
        bullets.add(new_bullet)

def check_Keyup(event, ship):
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

def update_screen(setting, screen, ship, alien, bullets, play_button, stats, sb):
    screen.fill(setting.bgcolor)

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.draw(screen)
    sb.show_score()

    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def update_bullet(setting, screen, stats, sb, ship, aliens, bullets):
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(setting, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(setting, screen, stats, sb, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += setting.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        bullets.empty()
        setting.increase_speed()
        create_fleet(setting, screen, ship, aliens)

def update_aliens(setting, stats, sb, screen, ship, aliens, bullets):
    check_fleet_edges(setting, aliens)
    aliens.update()

    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(setting, stats, sb, screen, ship, aliens, bullets)

    check_aliens_bottom(setting, stats, sb, screen, ship, aliens, bullets)

def create_fleet(setting, screen, ship, aliens):
    alien = Alien(setting, screen)
    number_aliens_x = get_number_aliens(setting, alien.rect.width)
    number_rows = get_number_rows(setting, ship.rect.height, alien.rect.height)

    for row_number in range (number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(setting, screen, aliens, alien_number, row_number)

def get_number_aliens(setting, alien_width):
    available_space_x = setting.screenWidth - 2*alien_width
    number_aliens_x = int(available_space_x/(2*alien_width))
    return number_aliens_x

def create_alien(setting, screen, aliens, alien_number, row_number):
    alien = Alien(setting, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(setting, ship_height, alien_height):
    available_space_y = (setting.screenHeight - (3*alien_height) - ship_height)
    number_rows = int(available_space_y/(2*alien_height))
    return number_rows

def check_fleet_edges(setting, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_directions(setting, aliens)
            break

def change_fleet_directions(setting, aliens):
    for alien in aliens.sprites():
        alien.rect.y += setting.fleet_drop_speed
    setting.fleet_direction *= -1

def check_aliens_bottom (setting, stats, sb, screen, ship, aliens, bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(setting, stats, sb, screen, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
