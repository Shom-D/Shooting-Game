import pygame as pg
import sys
from Players import *

'''class Shooting_game:
    def __init__(self):
        pass
    
    def __add__(self, other: Shooting_game):
'''


def main():
    WIDTH = 500
    HEIGHT = 400
    FPS = 60
    running = True
    screen = pg.display.set_mode((WIDTH, HEIGHT))

    sprite_list = pg.sprite.Group()

    image_path = r".\images\tank_up.png"
    player1 = Player(image_path, starting_pos= (WIDTH/4, HEIGHT/2))
    player_rect = pg.Rect(0,0, WIDTH*17/40, HEIGHT)
    player1.set_movement_keys(left = pg.K_a, right= pg.K_d, up = pg.K_w, down= pg.K_s, boundary_rect = player_rect)
    sprite_list.add(player1)

    player2 = Player(image_path, starting_pos=(3*WIDTH/4, HEIGHT/2))
    player_rect = pg.Rect(23/40*WIDTH, 0 , WIDTH, HEIGHT)
    player2.set_movement_keys(left = pg.K_LEFT, right= pg.K_RIGHT, up = pg.K_UP, down= pg.K_DOWN, boundary_rect= player_rect)

    sprite_list.add(player2)

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()
            
        screen.fill((50,50,50)) 
        sprite_list.update(0.5)
        sprite_list.draw(screen)

        pg.display.update()

if __name__== "__main__":
    main()


    