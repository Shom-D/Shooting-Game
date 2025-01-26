import pygame as pg
import numpy as np
import math

class Bullet(pg.sprite.Sprite):
    
    def __init__(self, angle, image_path, position):
        super().__init__()
        self.original_image =  pg.image.load(image_path).convert_alpha()
        self.image =  pg.image.load(image_path).convert_alpha()
        self.angle = math.radians(angle)
        self.rect = self.image.get_rect()

        self.image = pg.transform.rotate(self.image, angle)
        self.rect.center = position
    
    def update(self, speed):
        self.rect.x -= np.sin(self.angle)*speed
        self.rect.y -= np.cos(self.angle)*speed

