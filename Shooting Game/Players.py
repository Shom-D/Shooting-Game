import pygame as pg


class Player(pg.sprite.Sprite):

    def __init__(self, image_path, starting_pos):
        super().__init__()
        self.pos = starting_pos
        self.image = pg.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()

    def set_movement_keys(self, left, right, up, down, boundary_rect: pg.Rect):
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.boundary = boundary_rect

    def update(self, speed):

        keys = pg.key.get_pressed()
        horizontal_keys_pressed = keys[self.left]-keys[self.right]
        vertical_keys_pressed = keys[self.up]-keys[self.down]

        if horizontal_keys_pressed > 0:
            self.image = pg.transform.rotate(self.image, -90)
        elif horizontal_keys_pressed < 0:
            self.image = pg.transform.rotate(self.image, 90)
        elif vertical_keys_pressed > 0:
            self.image = pg.transform.rotate(self.image, 0)
        elif vertical_keys_pressed < 0:
            self.image = pg.transform.rotate(self.image, 180)

        print(f"Horizontal movement is {horizontal_keys_pressed}")
        print(f"Vertical Movement is {vertical_keys_pressed}")

        self.rect.x -= (keys[self.left]-keys[self.right]) * speed
        self.rect.y -= (keys[self.up]-keys[self.down]) * speed

        self.rect.clamp(self.boundary)

        
        