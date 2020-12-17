import pygame
pygame.init()



screen = pygame.display.set_mode([300,300])
pygame.display.set_caption("TicTacToe")
pole = []
for i in range(3):
    pole.append([])
    for j in range(3):
        pole[i].append('')

turn = False
def Move():
    bestScore = -2
    for i in range(3):
        for j in range(3):
            if pole[i][j] == '':
                pole[i][j] = 'O'
                score = minmax(False)
                pole[i][j] = ''
                if score>bestScore:
                    bestScore = score
                    bestMove = [i,j]
    pole[bestMove[0]][bestMove[1]] = 'O'

def checkResult():
    for i in range(3):
        if pole[i].count('X') == 3:
            return 'X'
        if pole[i].count('O') == 3:
            return 'O'
    for j in range(3):
        x = 0
        o = 0
        for i in range(3):
            if pole[i][j] == 'X':
                x+=1
            elif pole[i][j] == 'O':
                o+=1
        if x == 3:
            return 'X'
        if o == 3:
            return 'O'
    x=0
    o=0
    for i in range(3):
        if pole[i][i] == 'X':
            x+=1
        if pole[i][i] == 'O':
            o+=1
    if x == 3:
        return 'X'
    if o == 3:
        return 'O'

    x=0
    o=0
    for i in range(3):
        if pole[i][2-i] == 'X':
            x+=1
        if pole[i][2-i] == 'O':
            o+=1
    if x == 3:
        return 'X'
    if o == 3:
        return 'O'

    count = 0
    for i in range(3):
        for j in range(3):
            if pole[i][j] == '':
                count+=1
    if count == 0:
        return 'T'
    
def minmax(maxmize):
    if checkResult()=='X':
        return -1
    if checkResult()=='O':
        return 1
    if checkResult()=='T':
        return 0
    
    if maxmize:
        bestScore = -2
        for i in range(3):
            for j in range(3):
                if pole[i][j] == '':
                    pole[i][j] = 'O'
                    score = minmax(False)
                    pole[i][j] = ''
                    if score>bestScore:
                        bestScore = score
        return bestScore
    else:
        bestScore = 2
        for i in range(3):
            for j in range(3):
                if pole[i][j] == '':
                    pole[i][j] = 'X'
                    score = minmax(True)
                    pole[i][j] = ''
                    if score<bestScore:
                        bestScore = score
        return bestScore

font1 = pygame.font.SysFont('Arial',95,bold=True)
    
while True:
    screen.fill(pygame.Color('white'))
    for i in range(100,300,100):
        pygame.draw.line(screen,pygame.Color('black'), [0,i], [300,i],2)
        pygame.draw.line(screen,pygame.Color('black'), [i,0], [i,300],2)

    if turn == False:
        Move()
        turn = True

    for i in range(3):
        for j in range(3):
            sign = font1.render(pole[i][j],1,pygame.Color('black'))
            screen.blit(sign,(j*100+5,i*100+5))
    
    if checkResult()=='X':
        print('X WON')
        exit()
    elif checkResult()=='O':
        print('O WON')
        exit()
    elif checkResult()=='T':
        print('TIE')
        exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos[0]//100, event.pos[1]//100
            if turn and pole[y][x] == '':
                pole[y][x] = 'X'
                turn = False
    if checkResult()=='X':
        print('X WON')
        exit()
    elif checkResult()=='O':
        print('O WON')
        exit()
    elif checkResult()=='T':
        print('TIE')
        exit()
    pygame.display.flip()
