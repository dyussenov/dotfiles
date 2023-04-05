import pygame, sys, time, random

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1280, 720),0,32)
screen.fill((255,255,255))
display = pygame.Surface((1280, 720), pygame.SRCALPHA, 32)


grass_img = pygame.image.load('grass.png').convert()
dirt_img = pygame.image.load('dirt.png').convert()
burned_img = pygame.image.load('burned.png').convert()

grass_img.set_colorkey((0, 0, 0))
dirt_img.set_colorkey((0, 0, 0))
burned_img.set_colorkey((0, 0, 0))

f = open('map.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()

while True:
    display.fill((255,255,255))
    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            if tile == 1:
                #pygame.draw.rect(display, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                display.blit(grass_img, (256 + x * 32 - y * 32, x * 16 + y * 16))
            if tile == 2:    
                display.blit(dirt_img, (256 + x * 32 - y * 32, x * 16 + y * 16))
            if tile == 3:    
                display.blit(burned_img, (256 + x * 32 - y * 32, x * 16 + y * 16))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    screen.blit(pygame.transform.scale(display, screen.get_size()), (320, 60))
    pygame.display.update()
    time.sleep(1)
