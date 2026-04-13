import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("geym")

def gem():
    global P, E, E0, K, lK, I, U, B, k, Q, V, C, H, krp, victory
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

    victory = pygame.image.load('Pr/victory.png').convert_alpha()

    I = pygame.image.load('Pr/игровая ячейка.png').convert_alpha()
    B = pygame.image.load('Pr/блокнутая ячейка.png').convert_alpha()
    U = pygame.image.load('Pr/простая ечейка.png').convert_alpha()

    k = random.randint(1, 11)
    #k = 11
    if k == 1:
        K = pygame.image.load('Pr/крашеная ечейка, цвет синий.png').convert_alpha()
    elif k == 2:
        K = pygame.image.load('Pr/крашеная ечейка, цвет красный.png').convert_alpha()
    elif k == 3:
        K = pygame.image.load('Pr/крашеная ечейка, цвет голубой.png').convert_alpha()
    elif k == 4:
        K = pygame.image.load('Pr/крашеная ечейка, цвет жёлтый.png').convert_alpha()
    elif k == 5:
        K = pygame.image.load('Pr/крашеная ечейка, цвет зелёный.png').convert_alpha()
    elif k == 6:
        K = pygame.image.load('Pr/крашеная ечейка, цвет малиновый.png').convert_alpha()
    elif k == 7:
        K = pygame.image.load('Pr/крашеная ечейка, цвет ораньжевый.png').convert_alpha()
    elif k == 8:
        K = pygame.image.load('Pr/крашеная ечейка, цвет розовый.png').convert_alpha()
    elif k == 9:
        K = pygame.image.load('Pr/крашеная ечейка, цвет салатовый.png').convert_alpha()
    elif k == 10:
        K = pygame.image.load('Pr/крашеная ечейка, цвет фиолетовый.png').convert_alpha()
    elif k == 11:
        K = [pygame.image.load('Pr/крашеная ечейка, цвет красный.png').convert_alpha(),
            pygame.image.load('Pr/крашеная ечейка, цвет синий.png').convert_alpha(),
            pygame.image.load('Pr/крашеная ечейка, цвет голубой.png').convert_alpha(),
            pygame.image.load('Pr/крашеная ечейка, цвет жёлтый.png').convert_alpha(),
            pygame.image.load('Pr/крашеная ечейка, цвет зелёный.png').convert_alpha(),
            pygame.image.load('Pr/крашеная ечейка, цвет малиновый.png').convert_alpha(),
            pygame.image.load('Pr/крашеная ечейка, цвет ораньжевый.png').convert_alpha(),
            pygame.image.load('Pr/крашеная ечейка, цвет розовый.png').convert_alpha(),
            pygame.image.load('Pr/крашеная ечейка, цвет салатовый.png').convert_alpha(),
            pygame.image.load('Pr/крашеная ечейка, цвет фиолетовый.png').convert_alpha()
            ]
        lK = []
        for i in range(18):
            lK += [[]]
            for j in range(32):
                lK[i].append(random.randint(1, 10)-1)

    V = pygame.mixer.Sound('Pr/V.mp3')
    H = pygame.mixer.Sound('Pr/H.mp3')
    C = pygame.mixer.Sound('Pr/C.mp3')



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
                    if k == 11:
                        screen.blit(K[lK[j][h]], ((h*50)-5, j*50))
                    else:
                        screen.blit(K, ((h*50)-5, j*50))

    

    if not (Q[0] == E[0] and Q[1] == E[1]):
        H.play()

    Q[0], Q[1] = E[0], E[1]

    if not ((1 in P[1]) or (1 in P[2]) or (1 in P[3]) or (1 in P[4]) or (1 in P[5]) or (1 in P[6]) or (1 in P[7]) or (1 in P[8]) or (1 in P[9]) or (1 in P[10]) or (1 in P[11]) or (1 in P[12]) or (1 in P[13]) or (1 in P[14]) or (1 in P[15]) or (1 in P[16])):

        if krp == 0:
            V.play()
        krp += 1
        victory.set_alpha(krp*2)
        screen.blit(victory, (0, 25 - ((krp*12.5)**0.5)))
        if krp == 200:
            gem()
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


    pygame.display.update()
                








pygame.quit()