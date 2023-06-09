import pygame
import time

class TankBase():
    x = 0
    y = 0
    speed = 10
    last_shoot_timestamp = time.time()
    shoot_cooldown = 1
    direction = (1, 0)
    reload_time = 0
    EMPTY = pygame.Color(0, 0, 0, 255)
    def __init__(self, x: int, y: int, speed: int, hull_images: tuple, turret_images: tuple):
        self.x = x
        self.y = y
        self.speed = speed
        self.hull_images = hull_images
        self.turret_images = turret_images
        self.tank_surface = pygame.Surface((150, 150), pygame.SRCALPHA, 32)

    def move_tank(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

    def fire(self):
        print(time.time()-self.last_shoot_timestamp)
        if time.time() - self.last_shoot_timestamp >= self.shoot_cooldown:
            self.last_shoot_timestamp = time.time()
            return True
        else:
            return False

    def draw_tank(self) -> pygame.Surface:
        if self.direction == (1, 0):
            hull_direction = 2
        elif self.direction == (-1, 0):
            hull_direction = 0
        elif self.direction == (0, 1):
            hull_direction = 1
        else:
            hull_direction = 3
        #self.tank_surface.fill(self.EMPTY)
        self.tank_surface.blit(self.hull_images[hull_direction], (0,0))
        self.tank_surface.blit(self.turret_images[hull_direction], (0,0))
        return self.tank_surface

class Ammo():
    x = None
    y = None
    speed = 40
    direction=(1, 0)

    def __init__(self, x, y, speed, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        
    def draw_ammo(self, screen):
        self.x += self.direction[0] * self.speed
        self.y += self.direction[1] * self.speed
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 4, 4))



class EnemyTank(TankBase):
    detection_radius = 200
    