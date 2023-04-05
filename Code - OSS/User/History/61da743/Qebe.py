# здесь подключаются модули
import pygame
import sys

from tanks import TankBase
from tanks import Ammo

FPS = 60
 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
 
pygame.display.update()

player_turret = (
    pygame.image.load('Separated/Turret/german_tiger_turret1.png').convert_alpha(),
    pygame.image.load('Separated/Turret/german_tiger_turret2.png').convert_alpha(),
    pygame.image.load('Separated/Turret/german_tiger_turret3.png').convert_alpha(),
    pygame.image.load('Separated/Turret/german_tiger_turret4.png').convert_alpha(),
    pygame.image.load('Separated/Turret/german_tiger_turret5.png').convert_alpha(),
    pygame.image.load('Separated/Turret/german_tiger_turret6.png').convert_alpha(),
    pygame.image.load('Separated/Turret/german_tiger_turret7.png').convert_alpha(),
    pygame.image.load('Separated/Turret/german_tiger_turret8.png').convert_alpha(),
)

player_hull = (
    pygame.image.load('Separated/Hull/german_tiger_hull1.png').convert_alpha(),
    pygame.image.load('Separated/Hull/german_tiger_hull2.png').convert_alpha(),
    pygame.image.load('Separated/Hull/german_tiger_hull3.png').convert_alpha(),
    pygame.image.load('Separated/Hull/german_tiger_hull4.png').convert_alpha(),
    pygame.image.load('Separated/Hull/german_tiger_hull5.png').convert_alpha(),
    pygame.image.load('Separated/Hull/german_tiger_hull6.png').convert_alpha(),
    pygame.image.load('Separated/Hull/german_tiger_hull7.png').convert_alpha(),
    pygame.image.load('Separated/Hull/german_tiger_hull8.png').convert_alpha(),
)


player = TankBase(510, 150, 5, player_hull, player_turret)
ammo = None
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player.fire():
                    ammo = Ammo(player.x, player.y, 20, player.turret_position)
            if event.key == pygame.K_z:
                player.turn_turret(1)
            if event.key == pygame.K_x:
                player.turn_turret(-1)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        player.direction = (-1, 1)
        player.move_tank()
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        player.direction = (-1, -1)
        player.move_tank()    
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        player.direction = (1, 1)
        player.move_tank()
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        player.direction = (1, -1)
        player.move_tank()
    elif keys[pygame.K_UP]:
        player.direction = (0, -1)
        player.move_tank()
    elif keys[pygame.K_DOWN]:
        player.direction = (0, 1)
        player.move_tank()
    elif keys[pygame.K_LEFT]:
        player.direction = (-1, 0)
        player.move_tank()
    elif keys[pygame.K_RIGHT]:
        player.direction = (1, 0)
        player.move_tank()    


    screen.fill((255,255,255))
    screen.blit(player.draw_tank(), (player.x, player.y))
    if ammo:
        ammo.draw_ammo(screen)

    pygame.display.update()