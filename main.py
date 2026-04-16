import pygame
import random
import helper

pygame.init()

screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("coloring cube")
pygame.display.set_icon(pygame.image.load(helper.resource_path('Pr/игровая ячейка.png')).convert_alpha())


ww = 0
vv = 1
Xv = pygame.Rect(1500, 0, 50, 50)
Xo = pygame.Rect(1550, 0, 50, 50)
Xw = pygame.Rect(1450, 0, 50, 50)

ze = pygame.image.load(helper.resource_path('Pr/звук есть.png')).convert_alpha()
zn = pygame.image.load(helper.resource_path('Pr/звук нету.png')).convert_alpha()
ob = pygame.image.load(helper.resource_path('Pr/абновить.png')).convert_alpha()
wp = pygame.image.load(helper.resource_path('Pr/простой цвет.png')).convert_alpha()
ws = pygame.image.load(helper.resource_path('Pr/набор цвета.png')).convert_alpha()

victory = pygame.image.load(helper.resource_path('Pr/victory.png')).convert_alpha()

I = pygame.image.load(helper.resource_path('Pr/игровая ячейка.png')).convert_alpha()
B = pygame.image.load(helper.resource_path('Pr/блокнутая ячейка.png')).convert_alpha()
U = pygame.image.load(helper.resource_path('Pr/простая ечейка.png')).convert_alpha()

V = pygame.mixer.Sound(helper.resource_path('Pr/V.mp3'))
H = pygame.mixer.Sound(helper.resource_path('Pr/H.mp3'))
C = pygame.mixer.Sound(helper.resource_path('Pr/C.mp3'))



def gem():
    global P, E, E0, K, lK, k, Q, krp, wl
    P = [
        [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,],
        [8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]
    ]
    E = [random.randint(1, 16),random.randint(1, 30)]
    A = []
    for i in range(2000):
        A += [[random.randint(1, 4),random.randint(1, 15)]]
    if not A[0][0] == 1:
        P[E[0]-1][E[1]] = 8
    if not A[0][0] == 2:
        P[E[0]][E[1]+1] = 8
    if not A[0][0] == 3:
        P[E[0]+1][E[1]] = 8
    if not A[0][0] == 4:
        P[E[0]][E[1]-1] = 8
    P[E[0]][E[1]] = 1

    E0 = [[0],[0]]
    E0[0], E0[1] = E[0], E[1]

    #print(E)
    Q = [[0],[0]]
    krp = 0

    for i in A:
        if i[0] == 1:
            for j in range(i[1]):
                if P[E[0]-1][E[1]] != 8:
                    P[E[0]-1][E[1]] = 1
                    E[0] -= 1
            if P[E[0]-1][E[1]] == 1:
                while P[E[0]-1][E[1]] == 1:
                    E[0] -= 1
            P[E[0]-1][E[1]] = 8
        elif i[0] == 2:
            for j in range(i[1]):
                if P[E[0]][E[1]+1] != 8:
                    P[E[0]][E[1]+1] = 1
                    E[1] += 1
            if P[E[0]][E[1]+1] == 1:
                while P[E[0]][E[1]+1] == 1:
                    E[1] += 1
            P[E[0]][E[1]+1] = 8
        elif i[0] == 3:
            for j in range(i[1]):
                if P[E[0]+1][E[1]] != 8:
                    P[E[0]+1][E[1]] = 1
                    E[0] += 1
            if P[E[0]+1][E[1]] == 1:
                while P[E[0]+1][E[1]] == 1:
                    E[0] += 1
            P[E[0]+1][E[1]] = 8
        elif i[0] == 4:
            for j in range(i[1]):
                if P[E[0]][E[1]-1] != 8:
                    P[E[0]][E[1]-1] = 1
                    E[1] -= 1
            if P[E[0]][E[1]-1] == 1:
                while P[E[0]][E[1]-1] == 1:
                    E[1] -= 1
            P[E[0]][E[1]-1] = 8

    P[E0[0]][E0[1]] = 2




    k = [[0],[0]]
    k[0] = random.randint(1, 10)
    #k[0] = 10
    if k[0] == 10:
        k[1] = random.randint(1, 6)
        #k[1] = 6
        lK = []
        for i in range(18):
            lK += [[]]
            for j in range(32):
                lK[i].append(random.randint(1, 3)-1)
        if k[1] == 1:
            wl = pygame.image.load(helper.resource_path('Pr/цвет микс 1.png')).convert_alpha()
            K = [
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 2.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет зелёный.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет салатовый.png')).convert_alpha()
            ]
        elif k[1] == 2:
            wl = pygame.image.load(helper.resource_path('Pr/цвет микс 2.png')).convert_alpha()
            K = [
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 4.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет синий.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет фиолетовый.png')).convert_alpha()
            ]
        elif k[1] == 3:
            wl = pygame.image.load(helper.resource_path('Pr/цвет микс 3.png')).convert_alpha()
            K = [
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 5.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет красный.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет ораньжевый.png')).convert_alpha()
            ]
        elif k[1] == 4:
            wl = pygame.image.load(helper.resource_path('Pr/цвет микс 4.png')).convert_alpha()
            K = [
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 6.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет розовый.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет малиновый.png')).convert_alpha()
            ]
        elif k[1] == 5:
            wl = pygame.image.load(helper.resource_path('Pr/цвет микс 5.png')).convert_alpha()
            K = [
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 3.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 2.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет жёлтый.png')).convert_alpha()
            ]
        elif k[1] == 6:
            wl = pygame.image.load(helper.resource_path('Pr/цвет микс 6.png')).convert_alpha()
            K = [
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 1.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет салатовый.png')).convert_alpha(),
                pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет голубой.png')).convert_alpha()
            ]
    else:
        k[1] = random.randint(1, 16)
        if k[1] == 1:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет синий.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет синий.png')).convert_alpha()
        elif k[1] == 2:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет красный.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет красный.png')).convert_alpha()
        elif k[1] == 3:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет голубой.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет голубой.png')).convert_alpha()
        elif k[1] == 4:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет жёлтый.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет жёлтый.png')).convert_alpha()
        elif k[1] == 5:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет зелёный.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет зелёный.png')).convert_alpha()
        elif k[1] == 6:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет малиновый.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет малиновый.png')).convert_alpha()
        elif k[1] == 7:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет ораньжевый.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет ораньжевый.png')).convert_alpha()
        elif k[1] == 8:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет розовый.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет розовый.png')).convert_alpha()
        elif k[1] == 9:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет салатовый.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет салатовый.png')).convert_alpha()
        elif k[1] == 10:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет фиолетовый.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет фиолетовый.png')).convert_alpha()
        elif k[1] == 11:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 1.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет 1.png')).convert_alpha()
        elif k[1] == 12:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 2.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет 2.png')).convert_alpha()
        elif k[1] == 13:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 3.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет 3.png')).convert_alpha()
        elif k[1] == 14:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 4.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет 4.png')).convert_alpha()
        elif k[1] == 15:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 5.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет 5.png')).convert_alpha()
        elif k[1] == 16:
            K = pygame.image.load(helper.resource_path('Pr/крашеная ечейка, цвет 6.png')).convert_alpha()
            wl = pygame.image.load(helper.resource_path('Pr/цвет 6.png')).convert_alpha()

    #for i in P:
    #    print(i)
    #print(E0)

    #B_cub = pygame.Surface((50, 50))
    #B_cub.fill((255, 0, 0))
    #U_cub = pygame.Surface((50, 50))
    #U_cub.fill((0, 255, 0))
    #K_cub = pygame.Surface((50, 50))
    #K_cub.fill((0, 0, 255))
    #cub = pygame.Surface((50, 50))
    #cub.fill((255, 255, 255))

    #print(A[0])
    #print(A[0][0])


    E[0], E[1] = E0[0], E0[1]




gem()
Go = True
while Go:
    for i in range(32):
        h = 31 - i
        for j in range(18):
            if E[0] == j and E[1] == h:
                screen.blit(I, ((h*50)-5, j*50))
            else:
                if P[j][h] == 8 or P[j][h] == 0:
                    screen.blit(B, ((h*50)-5, j*50))
                elif P[j][h] == 1:
                    screen.blit(U, ((h*50)-5, j*50))
                elif P[j][h] == 2:
                    if k[0] == 10:
                        screen.blit(K[lK[j][h]], ((h*50)-5, j*50))
                    else:
                        screen.blit(K, ((h*50)-5, j*50))
    if ww == 0:
        if k[0] == 10:
            screen.blit(ws, ((1450)-5, 0))
        else:
            screen.blit(wp, ((1450)-5, 0))
    else:
        screen.blit(wl, ((1450)-5, 0))
    screen.blit(ob, ((1550)-5, 0))
    if vv == 1:
        screen.blit(ze, ((1500)-5, 0))
    else:
        screen.blit(zn, ((1500)-5, 0))

    if (not (Q[0] == E[0] and Q[1] == E[1])) and vv == 1:
        H.play()

    m_p = pygame.mouse.get_pos()
    Q[0], Q[1] = E[0], E[1]

    if not ((1 in P[1]) or (1 in P[2]) or (1 in P[3]) or (1 in P[4]) or (1 in P[5]) or (1 in P[6]) or (1 in P[7]) or (1 in P[8]) or (1 in P[9]) or (1 in P[10]) or (1 in P[11]) or (1 in P[12]) or (1 in P[13]) or (1 in P[14]) or (1 in P[15]) or (1 in P[16])):

        if krp == 0 and vv == 1:
            V.play()
        krp += 1
        victory.set_alpha(krp*2)
        screen.blit(victory, (0, 25 - ((krp*12.5)**0.5)))
        if krp == 200:
            gem()
            if vv == 1:
                C.play()
            O = 0

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Go = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    while not (P[E[0]-1][E[1]] == 8 or P[E[0]-1][E[1]] == 0):
                            P[E[0]-1][E[1]] = 2
                            E[0] -= 1
                elif event.key == pygame.K_RIGHT:
                    while P[E[0]][E[1]+1] != 8 and P[E[0]][E[1]+1] != 0:
                            P[E[0]][E[1]+1] = 2
                            E[1] += 1
                elif event.key == pygame.K_DOWN:
                    while P[E[0]+1][E[1]] != 8 and P[E[0]+1][E[1]] != 0:
                            P[E[0]+1][E[1]] = 2
                            E[0] += 1
                elif event.key == pygame.K_LEFT:
                    while P[E[0]][E[1]-1] != 8 and P[E[0]][E[1]-1] != 0:
                            P[E[0]][E[1]-1] = 2
                            E[1] -= 1
                elif event.key == pygame.K_e:
                    E[0], E[1] = E0[0], E0[1]
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Xv.collidepoint(m_p):
                    if vv == 1:
                        vv = 0
                    else:
                        vv = 1
                elif Xo.collidepoint(m_p):
                    gem()
                    if vv == 1:
                        C.play()
                elif Xw.collidepoint(m_p):
                    if ww == 1:
                        ww = 0
                    else:
                        ww = 1


    pygame.display.update()
                
pygame.quit()