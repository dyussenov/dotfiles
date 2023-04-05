import pygame
import time

def translate_direction(direction: tuple()) -> int:
    if direction == (-1, 0):
        return 0
    elif direction == (-1, 1):
        return 1
    elif direction == (0, 1):
        return 2
    elif direction == (1, 1):
        return 3
    elif direction == (1, 0):
        return 4
    elif direction == (1, -1):
        return 5
    elif direction == (0, -1):
        return 6
    else:
        return 7

def translate_position(position: int) -> tuple:
    if position == 0:
        return (-1, 0)
    elif position == 1:
        return (-1, 1)
    elif position == 2:
        return (0, 1)
    elif position == 3:
        return (1, 1)
    elif position == 4:
        return (1, 0)
    elif position == 5:
        return (1, -1)
    elif position == 6:
        return (0, -1)
    else:
        return (-1, -1)

class TankBase():
    x = 400
    y = 200
    speed = 10
    last_shoot_timestamp = time.time()
    shoot_cooldown = 1
    direction = (1, 0)
    reload_time = 0
    EMPTY = pygame.Color(0, 0, 0, 0)
    def __init__(self, x: int, y: int, speed: int, hull_images: tuple, turret_images: tuple):
        self.x = x
        self.y = y
        self.speed = speed
        self.hull_images = hull_images
        self.turret_images = turret_images
        self.tank_surface = pygame.Surface((150, 150), pygame.SRCALPHA, 32)
        self.turret_position = 6
    def move_tank(self):
        self.x += self.speed * self.direction[0]
        self.y += (self.speed * self.direction[1])//2

    def turn_turret(self, direction):
        self.turret_position += direction
        if self.turret_position == 8:
            self.turret_position = 0
        if self.turret_position == -1:
            self.turret_position = 7

    def fire(self):
        print(time.time()-self.last_shoot_timestamp)
        if time.time() - self.last_shoot_timestamp >= self.shoot_cooldown:
            self.last_shoot_timestamp = time.time()
            return True
        else:
            return False

    def draw_tank(self) -> pygame.Surface:
        hull_direction = translate_direction(self.direction)

        self.tank_surface.fill(self.EMPTY)
        self.tank_surface.blit(self.hull_images[hull_direction], (0,0))
        self.tank_surface.blit(self.turret_images[self.turret_position], (0,0))
        return self.tank_surface

class Ammo():
    def __init__(self, x, y, speed, position):
        self.x = x + 70
        self.y = y + 70
        self.direction = translate_position(position)
        self.speed = speed
        
    def draw_ammo(self, screen):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, 4, 4))



class EnemyTank(TankBase):
    detection_radius = 200
    