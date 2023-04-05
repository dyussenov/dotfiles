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

    def __init__(self, x: int, y: int, speed: int):
        self.x = x
        self.y = y
        self.speed = speed

    def move_right(self):
        self.x += self.speed

    def move_left(self):
        self.x -= self.speed

    def move_up(self):
        self.y -= self.speed

    def move_down(self):
        self.y += self.speed

    def fire(self):
        print(time.time()-self.last_shoot_timestamp)
        if time.time() - self.last_shoot_timestamp >= self.shoot_cooldown:
            self.last_shoot_timestamp = time.time()
            return True
        else:
            return False

    def draw_tank(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, 40, 40))
    
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
    