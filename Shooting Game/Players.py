import pygame as pg
from Bullet import Bullet
import time

class Player(pg.sprite.Sprite):

    def __init__(self, image_path, starting_pos):
        
        super().__init__()
        self.original_image = pg.image.load(image_path).convert_alpha()
        self.image = pg.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = starting_pos
        self.angle = 90
        self.health = 1
        self.last_fired = time.time()
        self.bullets = pg.sprite.Group()
        self.dead = False


    def set_movement_keys(self, left, right, up, down, shoot, boundary_rect: pg.Rect):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.boundary = boundary_rect
        self.shoot = shoot

    def update(self, speed, screen):

        keys = pg.key.get_pressed()
        
        self.handle_player_movement(keys, speed)

        if keys[self.shoot]:
            self.fire()
        
        self.bullets.update(speed*2)
        self.bullets.draw(screen)
        self.display_health(screen)



    def handle_player_movement(self, keys: pg.key.ScancodeWrapper, speed: float):
        if type(keys) is not pg.key.ScancodeWrapper:
            raise TypeError(f"Keys must be {pg.key.ScancodeWrapper}")
        
        horizontal_keys_pressed = keys[self.right]- keys[self.left]
        vertical_keys_pressed = -keys[self.up] +keys[self.down] 

        if horizontal_keys_pressed > 0:
            self.angle = 270
        elif horizontal_keys_pressed < 0:
            self.angle = 90
        elif vertical_keys_pressed > 0:
            self.angle = 180
        elif vertical_keys_pressed < 0:
            self.angle = 0

        self.update_angle()
        self.rect.x+= horizontal_keys_pressed * speed
        self.rect.y += vertical_keys_pressed * speed

        self.rect.clamp_ip(self.boundary)


    def update_angle(self):
        self.image = pg.transform.rotate(self.original_image, self.angle)

    def fire(self):
        
        if time.time()- self.last_fired > 0.5:
            bullet = Bullet(self.angle, r".\images\bullet.png", self.rect.center)
            self.bullets.add(bullet)
            self.last_fired = time.time()

    def hit(self):
        self.health -= 0.1
        if self.health == 0.0:
            print("Dead")
            self.dead = True

    def display_health(self, screen):
        self.healthbar = pg.Rect(self.boundary.x +10, 10, (self.boundary.width-30)*self.health , 14)
        pg.draw.rect(screen, (10,200,10), self.healthbar)


        
        