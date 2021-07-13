import pygame
from pygame import draw
from player import Player
from bullet import Bullet

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BLACK = (0,0,0)
player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, radius=25)
bullets = []

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen.fill(BLACK)
pygame.display.set_caption('Hello there')

def draw_player():
    draw.circle(screen, (255,255,255), (player.x, player.y), player.radius)

def handle_keys_pressed():
    keys_pressed = pygame.key.get_pressed()

    # exit game
    if keys_pressed[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    # player movement
    if keys_pressed[pygame.K_w]:
        player.move(Player.UP)

    if keys_pressed[pygame.K_d]:
        player.move(Player.RIGHT)

    if keys_pressed[pygame.K_s]:
        player.move(Player.DOWN)
        
    if keys_pressed[pygame.K_a]:
        player.move(Player.LEFT)

def spawn_bullet():
    mouse_pos = pygame.mouse.get_pos()
    mouse_x = mouse_pos[0]
    mouse_y = mouse_pos[1]

    bullets.append(Bullet(player.x, player.y, mouse_x, mouse_y, 10))

def draw_bullets():
    for bullet in bullets:
        draw.circle(screen, (0, 100, 255), (bullet.x, bullet.y), bullet.radius)
        bullet.update()

def main_loop():
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                spawn_bullet()
            if event.type == pygame.QUIT:
                done = True

        handle_keys_pressed()

        screen.fill(BLACK)
        draw_player()
        draw_bullets()

        pygame.display.update()

def main():
    main_loop()
    pygame.quit()
    quit()

if __name__ == '__main__': main()