import pygame as pg

W, H = 20, 20
X, Y = 30, 30

DIRECTIONS = {
    "DOWN": (-1, 0),
    "UP": (+1, 0),
    "RIGHT": (0, +1),
    "LEFT": (0, -1),
}

def move_player():
    pass

def draw_background():
    pass

player = []

def draw_background():
    screen.fill((255, 255, 255))







pg.init()
screen = pg.display.set_mode((X * W, Y * H))
clock = pg.time.Clock()

running = True
while running:

    clock.tick(4)

    # on itère sur tous les évênements qui ont eu lieu depuis le précédent appel
    # ici donc tous les évènements survenus durant la seconde précédente
    for event in pg.event.get():
        # print(f"{event=}")
        # chaque évênement à un type qui décrit la nature de l'évênement
        # un type de pg.QUIT signifie que l'on a cliqué sur la "croix" de la fenêtre
        if event.type == pg.QUIT:
            running = False
        # un type de pg.KEYDOWN signifie que l'on a appuyé une touche du clavier
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_DOWN or event.key == pg.K_k:
                direction = DIRECTIONS["DOWN"]
            elif event.key == pg.K_UP or event.key == pg.K_i:
                direction = DIRECTIONS["UP"]
            if event.key == pg.K_RIGHT or event.key == pg.K_l:
                direction = DIRECTIONS["RIGHT"]
            elif event.key == pg.K_LEFT or event.key == pg.K_j:
                direction = DIRECTIONS["LEFT"]
            # si la touche est "Q" on veut quitter le programme
            elif event.key == pg.K_q:
                running = False

    move_player(player, direction)
    draw_background()
    

    pg.display.update()


# Enfin on rajoute un appel à pg.quit()
# Cet appel va permettre à Pygame de "bien s'éteindre" et éviter des bugs sous Windows
pg.quit()