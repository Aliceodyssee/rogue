from random import choice, randint
import pygame as pg
import numpy as np
from CharacterClass import Character

player = Character("@",2,2)
screenMap = []
for i in range(14) :
    L = []
    for j in range(26) :
        L.append(0)
    screenMap.append(L)

walls_COLOR = (220, 220, 220)
WHITE = (255, 255, 255)
dancefloor_COLOR = (128, 128, 0)
corridor_COLOR = (192, 16, 16)
door_COLOR = (92, 16, 16)
player_COLOR = (253,108,158)

#liste des positions de chaque type d'objet
L_pos_ceiling = [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6),
                (2,12), (2,13), (2,14), (2,15), (2,16), (2,17), (2,18),
                (6,19), (6,20), (6,21), (6,22), (6,23), (6,24),
                (8,1), (8,3), (8,4), (8,5), (8,6),
                (9,12), (9,13), (9,14), (9,15), (9,16), (9,18),
                (10,19), (10,20), (10,22), (10,23)]

L_pos_walls = [ (2,1), (3,1), (4,1), (5,1), (6,1), (7,1),
                (2,6), (3,6), (4,6), (6,6), (7,6),
                (3,12),(4,12),(5,12),(6,12),(8,12),
                (7,18),(4,18),(5,18),(6,18),(8,18),
                (7,19),(8,19),(9,19),
                (7,23),(8,23),(9,23)]

L_pos_doors = [(8,2),(5,6),(7,12),(9,17),(3,18),(10,21)]

L_pos_corridor = [(9,2), (10,2),
                (5,7), (5,8), (5,9), (5,10),
                (6,10), (7,10),(8,10),(9,10), (10,10),
                (7,11), (10,17), (11,21), (12,21), (12,22), (12,23),
                (3,19),(3,20),(3,21),
                (2,21), (1,21), (1,22), (1,23)]
for i in range(2,18):
    L_pos_corridor.append((11,i))
for i in range(1,13):
    L_pos_corridor.append((i,24))

L_pos_dancefloor = []

for i in range(2,8):
    for j in range(2,6):
        L_pos_dancefloor.append((i,j))

for i in range(3,9):
    for j in range(13,18):
        L_pos_dancefloor.append((i,j))
        
for i in range(7,10):
    for j in range(20,23):
        L_pos_dancefloor.append((i,j))

def background():  
    #on les met dans le screenMap
    for i in range(len(L_pos_ceiling)):
        screenMap[L_pos_ceiling[i][0]][L_pos_ceiling[i][1]]= "-"

    for i in range(len(L_pos_walls)):
        screenMap[L_pos_walls[i][0]][L_pos_walls[i][1]]= "|"

    for i in range(len(L_pos_doors)):
        screenMap[L_pos_doors[i][0]][L_pos_doors[i][1]]= "+"

    for i in range(len(L_pos_corridor)):
        screenMap[L_pos_corridor[i][0]][L_pos_corridor[i][1]]= "#"

    for i in range(len(L_pos_dancefloor)):
        screenMap[L_pos_dancefloor[i][0]][L_pos_dancefloor[i][1]]= "."
    for i in range(14):
        for j in range(26):
            if screenMap[i][j] == ".":
                rect = pg.Rect( i * W, j * H, W, H)
                pg.draw.rect(screen_img, dancefloor_COLOR, rect)
            if screenMap[i][j] == "#":
                rect = pg.Rect( i * W, j * H, W, H)
                pg.draw.rect(screen_img, corridor_COLOR, rect)
            if screenMap[i][j] == "+":
                rect = pg.Rect( i * W, j * H, W, H)
                pg.draw.rect(screen_img, door_COLOR, rect)
            if screenMap[i][j] == "0":
                rect = pg.Rect( i * W, j * H, W, H)
                pg.draw.rect(screen_img, WHITE, rect)
            if screenMap[i][j] =="-" or screenMap[i][j] == "|":
                rect = pg.Rect( i * W, j * H, W, H)
                pg.draw.rect(screen_img, walls_COLOR, rect)
    if screenMap[4][4]!="@":
        screenMap[4][4]="j"
        rect = pg.Rect((4)*W, (4)*H,W,H)
        pg.draw.rect(screen_img, (121, 248, 248), rect)
    else:
        rect = pg.Rect((4)*W, (4)*H,W,H)
        pg.draw.rect(screen_img, dancefloor_COLOR, rect)

W, H = 20, 20
X, Y = 30, 30

pg.init()
screen_img = pg.display.set_mode((X * W, Y * H))
clock = pg.time.Clock()



print(np.array(screenMap))




W, H = 20, 20
X, Y = 30, 30

DIRECTIONS = {
    "DOWN": (0, +1),
    "UP": (0, -1),
    "RIGHT": (+1, 0),
    "LEFT": (-1, 0),
}

direction = (0,0)



screen_copy=screenMap.copy()

rect = pg.Rect((player.x)*W, (player.y)*H,W,H)
pg.draw.rect(screen_img, player_COLOR, rect)



def move_player(player,direction):
    
    x,y = player.x,player.y
    dx,dy = direction

    if ((screenMap[x+dx][y+dy] == ".") or (screenMap[x+dx][y+dy] =="#") or (screenMap[x+dx][y+dy] == "+") or (screenMap[x+dx][y+dy]=="j")):
        screenMap[x][y]=screen_copy[x][y]

        if screenMap[x][y] == ".":
            rect = pg.Rect(x*W,y*H,W,H)
            pg.draw.rect(screen_img, dancefloor_COLOR, rect)
            if (screenMap[x+dx][y+dy]=="j"):
                screenMap[x+dx][y+dy]=player.name
                pg.display.set_caption("Potion r??cup??r??e ")
                rect = pg.Rect((x+dx)*W,(y+dy)*H,W,H)
                pg.draw.rect(screen_img, dancefloor_COLOR, rect)
        if screenMap[x][y] == "#":
            rect = pg.Rect(x*W,y*H,W,H)
            if (screenMap[x+dx][y+dy]=="j"):
                screenMap[x+dx][y+dy]=player.name
                pg.display.set_caption("Potion r??cup??r??e ")
                rect = pg.Rect((x)*W,(y)*H,W,H)
                pg.draw.rect(screen_img, dancefloor_COLOR, rect)
            pg.draw.rect(screen_img, corridor_COLOR, rect)
            if (screenMap[x+dx][y+dy]=="j"):
                screenMap[x+dx][y+dy]=player.name
                pg.display.set_caption("Potion r??cup??r??e ")
                rect = pg.Rect((x)*W,(y)*H,W,H)
                pg.draw.rect(screen_img, dancefloor_COLOR, rect)
        if screenMap[x][y] == "+":
            rect = pg.Rect(x*W,y*H,W,H)
            pg.draw.rect(screen_img, door_COLOR, rect)
            if (screenMap[x+dx][y+dy]=="j"):
                screenMap[x+dx][y+dy]=player.name
                pg.display.set_caption("Potion r??cup??r??e ")
                rect = pg.Rect((x)*W,(y)*H,W,H)
                pg.draw.rect(screen_img, dancefloor_COLOR, rect)
        player.move(dx,dy)
        screenMap[x+dx][y+dy]=player.name
        rect = pg.Rect((x+dx)*W, (y+dy)*H,W,H)
        pg.draw.rect(screen_img, player_COLOR, rect)
    


    


pg.init()
screen = pg.display.set_mode((X * W, Y * H))
clock = pg.time.Clock()

running = True
while running:

    clock.tick(4)

    # on it??re sur tous les ??v??nements qui ont eu lieu depuis le pr??c??dent appel
    # ici donc tous les ??v??nements survenus durant la seconde pr??c??dente
    for event in pg.event.get():
        # print(f"{event=}")
        # chaque ??v??nement ?? un type qui d??crit la nature de l'??v??nement
        # un type de pg.QUIT signifie que l'on a cliqu?? sur la "croix" de la fen??tre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuy?? une touche du clavier
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN or event.key == pg.K_k:
                direction = DIRECTIONS["DOWN"]
            elif event.key == pg.K_UP or event.key == pg.K_i:
                direction = DIRECTIONS["UP"]
            if event.key == pg.K_RIGHT or event.key == pg.K_l:
                direction = DIRECTIONS["RIGHT"]
            elif event.key == pg.K_LEFT or event.key == pg.K_j:
                direction = DIRECTIONS["LEFT"]
            elif event.key == pg.K_t:
                pg.display.set_caption(f"sac ?? dos : {player.listItems} ")

            # si la touche est "Q" on veut quitter le programme
            elif event.key == pg.K_q:
                running = False
    background()
    move_player(player, direction)
    direction=(0,0)
    '''while(player.x,player.y != 4,4):
        rect = pg.Rect((4)*W, (4)*H,W,H)
        pg.draw.rect(screen_img, (121, 248, 248), rect)
    '''
 
    pg.display.update()


# Enfin on rajoute un appel ?? pg.quit()
# Cet appel va permettre ?? Pygame de "bien s'??teindre" et ??viter des bugs sous Windows
pg.quit()




