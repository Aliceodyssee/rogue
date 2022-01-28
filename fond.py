from random import choice, randint
import pygame as pg
import numpy as np

screen = []
for i in range(14) :
    L = []
    for j in range(26) :
        L.append(0)
    screen.append(L)

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
        
#on les met dans le screen
for i in range(len(L_pos_ceiling)):
    screen[L_pos_ceiling[i][0]][L_pos_ceiling[i][1]]= "-"

for i in range(len(L_pos_walls)):
    screen[L_pos_walls[i][0]][L_pos_walls[i][1]]= "|"

for i in range(len(L_pos_doors)):
    screen[L_pos_doors[i][0]][L_pos_doors[i][1]]= "+"

for i in range(len(L_pos_corridor)):
    screen[L_pos_corridor[i][0]][L_pos_corridor[i][1]]= "#"

for i in range(len(L_pos_dancefloor)):
    screen[L_pos_dancefloor[i][0]][L_pos_dancefloor[i][1]]= "."


print(np.array(screen))