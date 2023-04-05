import pygame
import copy
import time
import json

class GameSound:
    def __init__(self, path_to_sound):
        self.sound = pygame.mixer.Sound(path_to_sound)

    def play(self):
        self.sound.play()


class GameObject:
    width = 32
    height = 32
    color = (255, 0, 0)

    def __init__(self, coordinate,speed,direction, parent_surface):
        self.coordinate = coordinate
        self.surface = pygame.Surface((self.width, self.height))
        self.surface.fill(self.color)
        self.speed = speed
        self.kd = 1
        self.last_shoot_timestamp = time.time()
        self.direction = direction
        self.prev_coor = coordinate
        self.parent_surface = parent_surface
        self.shoot_status = True
            

    def draw_object(self):
        self.parent_surface.blit(self.surface, self.coordinate)

    def destroy(self):
        self.surface.fill((0, 255, 0))

    def move(self, walls):
        self.Bot_rect = pygame.Rect(self.coordinate, [32, 32])
        res = self.Bot_rect.collidelistall(walls)
        if not res:
            self.prev_coor = copy.deepcopy(self.coordinate)
            self.coordinate[0] += self.speed * self.direction[0]
            self.coordinate[1] += self.speed * self.direction[1]
        else:
            self.coordinate = self.prev_coor
            self.direction[0] *= -1
            self.direction[1] *= -1

    def shoot(self):
        if time.time()-self.last_shoot_timestamp>self.kd:
            self.shoot_status = False
        if not self.shoot_status:
            self.bullet = Bullet(self.coordinate, copy.deepcopy(self.direction), pygame.image.load('textures/bullet.png'))
            self.shoot_status = True


    def move_bullet(self):
        self.bullet.move()

    def blit_bullet(self):
        self.bullet.blit_bullet(self.parent_surface)


class Bullet:
    speed = 4
    coordinate = [0,0]
    direction = (1,0)
    skin = None

    def __init__(self, coordinate, direction, skin):
        self.coordinate = coordinate
        self.direction = direction
        self.skin = skin

    def move(self):
        self.coordinate[0] += self.speed * self.direction[0]
        self.coordinate[1] += self.speed * self.direction[1]

    def blit_bullet(self, surface):
        surface.blit(self.skin, self.coordinate)

    def destroy(self):
        self.coordinate = [-5, -5]
        self.speed = 0

    def check_collision(self, enemies, sound):
        for o in enemies:
            if self.coordinate[0] > o.coordinate[0] and self.coordinate[0] < o.coordinate[0]+32 and self.coordinate[1] > o.coordinate[1] and self.coordinate[1] < o.coordinate[1]+32:
                self.destroy()
                print('Есть пробитие')
                sound.play()
                o.destroy()


class Tank:
    def __init__(self, coordinates, speed, kd):
        self.coordinates = coordinates
        self.speed = speed
        self.kd = kd
        self.load_textures()
        self.surface = pygame.Surface((32, 32), pygame.SRCALPHA, 32)
        self.player_rect = pygame.Rect(coordinates, [32,32])
        self.prev_coordinates = coordinates
        self.surface = self.surface.convert_alpha()

    def load_textures(self):
        with open("textures.json", "r") as file:
            data = json.load(file)
            player_textures = data['player']
            print(player_textures)
            for attr, value in player_textures.items():
                self.__setattr__(attr, pygame.image.load("textures/player/"+value))
            self.current_corp = self.hull_down
            self.current_bash = self.turret_down

    def move(self, direction, list_of_objects):
        self.player_rect = pygame.Rect(self.coordinates, [32, 32])
        res = self.player_rect.collidelistall(list_of_objects)
        if not res:
            self.prev_coordinates = copy.deepcopy(self.coordinates)
            self.coordinates[0] += self.speed * direction[0]
            self.coordinates[1] += self.speed * direction[1]
        else:
            self.coordinates = self.prev_coordinates

    def blit(self, parent_surface):
        self.surface.blit(self.current_corp, (0,0))
        self.surface.blit(self.current_bash, (0, 0))
        parent_surface.blit(self.surface, self.prev_coordinates)


class Wall:
    width = 32
    hight = 32

    def __init__(self, coordinate, wall):
        self.coordinate = coordinate
        self.wall = wall
        self.surface = pygame.Surface((32, 32))

    def blit(self, parent_surface):
        self.surface.blit(self.wall, (0, 0))
        parent_surface.blit(self.surface, self.coordinate)


class Notification:
    def __init__(self, text, color, is_critical=False, notification_time=5, position=[350, 350], is_blink=False):
        self.time = time
        self.position = position
        self.is_blink = is_blink
        self.notification_time = notification_time
        self.status = False
        if is_blink:
            self.blink_time = 0.5
            self.blink_status = True
            self.last_blink_timestamp = time.time()
        self.is_critical = is_critical
        if is_critical:
            self.critical_timeout = False

        font = pygame.font.Font(None, 36)
        self.rendered_text = font.render(text, True, color)

    def start_notification(self):
        self.status = True
        self.notification_timestamp = time.time()


    def blit_notification(self, parent_surface):
        if self.status:
            current_time = time.time()
            if current_time - self.notification_timestamp < self.notification_time:
                if not self.is_blink:
                    parent_surface.blit(self.rendered_text, self.position)
                else:
                    notification_timedelta = current_time - self.last_blink_timestamp

                    if self.blink_status and notification_timedelta < self.blink_time:
                        parent_surface.blit(self.rendered_text, self.position)
                    elif self.blink_status and notification_timedelta > self.blink_time:
                        self.blink_status = False
                        self.last_blink_timestamp = current_time
                    elif not self.blink_status and notification_timedelta > self.blink_time:
                        self.blink_status = True
                        self.last_blink_timestamp = current_time
            else:
                self.critical_timeout = True