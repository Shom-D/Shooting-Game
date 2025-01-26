import pygame as pg
import sys
from Players import *
import time


def main():
    WIDTH = 700
    HEIGHT = 500
    FPS = 60
    running = True
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    fps = pg.time.Clock()

    players = pg.sprite.Group()

    image_path = r".\images\tank_up.png"
    player1 = Player(image_path, starting_pos= (WIDTH/4, HEIGHT/2))
    player_rect = pg.Rect(0,0, WIDTH*37/80, HEIGHT)
    
    player1.set_movement_keys(left = pg.K_a, right= pg.K_d, up = pg.K_w, down= pg.K_s, boundary_rect = player_rect, shoot = pg.K_q)
    pg.draw.rect(screen, color=(255,0,0), rect=player1.boundary)
    players.add(player1)
    player1_group = pg.sprite.Group()
    player1_group.add(player1)

    player2 = Player(image_path, starting_pos=(3*WIDTH/4, HEIGHT/2))
    player_rect = pg.Rect(43/80*WIDTH, 0 , WIDTH, HEIGHT)
    player2.set_movement_keys(left = pg.K_LEFT, right= pg.K_RIGHT, up = pg.K_UP, down= pg.K_DOWN, boundary_rect= player_rect, shoot=pg.K_SLASH)

    players.add(player2)
    player2_group = pg.sprite.Group()
    player2_group.add(player2)

    dt=1e-2

    while running:
        
        start_time = time.time()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
                sys.exit()

        screen.fill((100,100,100))     
        pg.draw.rect(screen, color=(170,0,0), rect=player1.boundary)
        pg.draw.rect(screen, color=(0,0, 170), rect= player2.boundary)

        if pg.sprite.groupcollide(player1_group, player2.bullets, dokilla= False, dokillb= True):
            player1.hit()
        if pg.sprite.groupcollide(player2_group, player1.bullets, False, True):
            player2.hit()
        
        players.update(100*dt, screen)
        players.draw(screen)
        

        

        pg.display.update()
        fps.tick(FPS)

        dt = time.time() - start_time

if __name__== "__main__":
    main()


    