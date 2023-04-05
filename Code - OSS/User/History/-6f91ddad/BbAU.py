import pygame
import sys
import time
from objects import *

pygame.init()

sound1 = pygame.mixer.Sound(r'sound/start_battle.mp3')
sound1.play()

kill_sound = GameSound(r'sound/arthasyesattack1.mp3')


pygame.font.init()
sc = pygame.display.set_mode((300, 200))
alarm = Notification('alarm!', [244, 111, 111], is_critical=True, is_blink=True)
player_x = 0
player_y = 0

map_surf = pygame.Surface((1024,768))
f = open('texturs','r')
map_items = [
    pygame.image.load("textures/GOOBRICKS.png"),
    pygame.image.load("textures/DUNGEONCELL.png"),
    pygame.image.load("textures/CLAYBRICKS.png"),
]
map_item_coor = [0,0]

list_of_objects = [
]

for l in f:
    for i in l:
        if i != '\n':
            if i == "2":
                list_of_objects.append(pygame.Rect(map_item_coor,(32,32)))
            map_surf.blit(map_items[int(i)],map_item_coor)
            map_item_coor[0] += 32
    map_item_coor[1] += 32
    map_item_coor[0] = 0

FPS =60
W = 1024
H = 768


WHITE = (255, 255, 255)
BLUE = (0,0,255)

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W // 2
y = H // 2
r = 50


speed_x = 0
speed_y = 0

bullet = pygame.image.load("textures/bullet.png")
serf = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
serf = serf.convert_alpha()
player = Tank([0,0], 4, 1.5)
wall = [
    pygame.image.load("textures/BIGBRICKS.png")

]
w = Wall((0, 0), wall[0])
piu = False
bullet_cord = (0, 0)
bullet_direxion = (0, 0)
kd = time.time()



enemies = [
    GameObject([256, 64], 5, [1, 0], sc),
    GameObject([512, 512], 5, [0, 1], sc),
    GameObject([640, 512], 5, [1, 0], sc)
]


while 1:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 3
        player.move((-1, 0),list_of_objects)
        player.current_corp = player.hull_left

    elif keys[pygame.K_RIGHT]:
        x += 3
        player.current_corp = player.hull_right
        player.move((1, 0),list_of_objects)
    elif keys[pygame.K_UP]:
        y -= 3
        player.current_corp = player.hull_top
        player.move((0,-1),list_of_objects)
    elif keys[pygame.K_DOWN]:
        y += 3
        player.current_corp = player.hull_down
        player.move((0, 1),list_of_objects)

    if keys[pygame.K_w]:
        player.current_bash = player.turret_top
    elif keys[pygame.K_s]:
        player.current_bash = player.turret_down
    elif keys[pygame.K_d]:
        player.current_bash = player.turret_right
    elif keys[pygame.K_a]:
        player.current_bash = player.turret_left

    if keys[pygame.K_SPACE] and time.time()-kd > 1.5:
        bullet_cord = [player.coordinates[0],player.coordinates[1]]
        kd = time.time()
        if player.current_bash == player.turret_left:
            bullet_direxion = (-1,0)
            bullet_cord[1] = bullet_cord[1] + 8
        if player.current_bash == player.turret_right:
            bullet_direxion = (1,0)
            bullet_cord[1]= bullet_cord[1] + 8
        if player.current_bash == player.turret_down:
            bullet_direxion = (0,1)
            bullet_cord[0] = bullet_cord[0] + 8
        if player.current_bash == player.turret_top:
            bullet_direxion = (0,-1)
            bullet_cord[0] = bullet_cord[0] + 8
        bullet1 = Bullet(coordinate=bullet_cord, direction=bullet_direxion, skin=bullet)
        piu = True

    sc.fill(WHITE)
    sc.blit(map_surf,(0,0))
    w.blit(sc)
    player.blit(sc)


    sc.blit(serf, (x, y))

    for e in enemies:
        e.shoot()
        e.move(list_of_objects)
        e.draw_object()
        if not e.shoot_status:
            e.move_bullet()
            e.blit_bullet(sc)
        

    if piu:
        bullet1.blit_bullet(sc)
        bullet1.move()
        bullet1.check_collision(enemies, kill_sound)

    alarm.blit_notification(sc)


    if player.coordinates[0] < 0 or player.coordinates[1] < 0:
        if not alarm.status:
            alarm.start_notification()
    elif player_x >= 0 and player_y >= 0 and alarm.status:
        alarm.status = False

    alarm.blit_notification(sc)
    if alarm.critical_timeout:
        exit()

    pygame.display.update()



    clock.tick(FPS)