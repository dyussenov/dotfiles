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

grass_img = pygame.image.load('grass.png').convert()
dirt_img = pygame.image.load('dirt.png').convert()
burned_img = pygame.image.load('burned.png').convert()
tree_img = pygame.image.load('tree.png').convert()
tree2_img = pygame.image.load('tree2.png').convert()
farm_img = pygame.image.load('farmhouse.png').convert()


grass_img.set_colorkey((0, 0, 0))
dirt_img.set_colorkey((0, 0, 0))
burned_img.set_colorkey((0, 0, 0))
tree_img.set_colorkey((0, 0, 0))
tree2_img.set_colorkey((0, 0, 0))
farm_img.set_colorkey((0, 0, 0))

f = open('ground_layer.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

f = open('upper_layer.txt')
upper_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

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


player = TankBase(510, 150, 6, player_hull, player_turret)
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

    
    screen.fill((255,255,255))
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:
               screen.blit(grass_img, (256 + x * 32 - y * 32, x * 16 + y * 16))
            if tile == 2:    
                screen.blit(dirt_img, (256 + x * 32 - y * 32, x * 16 + y * 16))
            if tile == 3:    
                screen.blit(burned_img, (256 + x * 32 - y * 32, x * 16 + y * 16))
    
    for y, row in enumerate(upper_data):
        for x, tile in enumerate(row):
            if tile == 1:
                screen.blit(tree_img, (256 + x * 32 - y * 32, x * 16 + y * 16))
            elif tile == 2:
                screen.blit(tree2_img, (256 + x * 32 - y * 32, x * 16 + y * 16))
            elif tile == 3:
                screen.blit(farm_img, (256 + x * 32 - y * 32, x * 16 + y * 16))
            

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        player.direction = (-1, 0)
        player.move_tank()
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        player.direction = (0, -1)
        player.move_tank()    
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        player.direction = (0, 1)
        player.move_tank()
    elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        player.direction = (1, 0)
        player.move_tank()
    elif keys[pygame.K_UP]:
        player.direction = (1, -1)
        player.move_tank()
    elif keys[pygame.K_DOWN]:
        player.direction = (-1, 1)
        player.move_tank()
    elif keys[pygame.K_LEFT]:
        player.direction = (-1, -1)
        player.move_tank()
    elif keys[pygame.K_RIGHT]:
        player.direction = (1, 1)
        player.move_tank()    


    screen.blit(player.draw_tank(), (player.x, player.y))
    if ammo:
        ammo.draw_ammo(screen)

    pygame.display.update()