import pygame

x=70

player_1 = False

pygame.init
screen=pygame.display.set_mode((x*8,x*8))
pygame.display.set_caption("The Incredible chess")
icon=pygame.image.load("requirements/chess.png")
pygame.display.set_icon(icon)

b_piece = {}
b_piece["king"] = pygame.image.load("king.png")
b_piece["king"] = pygame.transform.scale(b_piece["king"],(60,60))
b_piece["queen"] = pygame.image.load("queen.png")
b_piece["queen"] = pygame.transform.scale(b_piece["queen"],(60,60))
b_piece["bishop"] = pygame.image.load("bishop.png")
b_piece["bishop"] = pygame.transform.scale(b_piece["bishop"],(60,60))
b_piece["knight"] = pygame.image.load("knight.png")
b_piece["knight"] = pygame.transform.scale(b_piece["knight"],(60,60))
b_piece["rook"] = pygame.image.load("rook.png")
b_piece["rook"] = pygame.transform.scale(b_piece["rook"],(60,60))
b_piece["pawn"] = pygame.image.load("pawn.png")
b_piece["pawn"] = pygame.transform.scale(b_piece["pawn"],(50,50))

w_piece = {}
w_piece["king"] = pygame.image.load("king1.png")
w_piece["king"] = pygame.transform.scale(w_piece["king"],(60,60))
w_piece["queen"] = pygame.image.load("queen1.png")
w_piece["queen"] = pygame.transform.scale(w_piece["queen"],(60,60))
w_piece["bishop"] = pygame.image.load("bishop1.png")
w_piece["bishop"] = pygame.transform.scale(w_piece["bishop"],(60,60))
w_piece["knight"] = pygame.image.load("knight1.png")
w_piece["knight"] = pygame.transform.scale(w_piece["knight"],(60,60))
w_piece["rook"] = pygame.image.load("rook1.png")
w_piece["rook"] = pygame.transform.scale(w_piece["rook"],(60,60))
w_piece["pawn"] = pygame.image.load("pawn1.png")
w_piece["pawn"] = pygame.transform.scale(w_piece["pawn"],(50,50))

piece = b_piece

board = []
for i in range(64):
    board.append(None)

class king:
    count = 0
    def __init__(self):
        #global player_1
        if king.count == 2:
            return
        elif king.count == 1:
            king.count = 2
            if player_1:
                self.pos = 59
            else:
                self.pos = 60
            board[self.pos] = False
        elif king.count ==0:
            king.count =1
            if player_1 :
                self.pos = 3
            else:
                self.pos = 4
            board[self.pos] = True
    def avail(self):
        mov =[]
        temp = [7,-7,8,-8,9,-9]
        for item in temp:
            if 64>item+self.pos>=0 and board[self.pos+item] != board[self.pos] and (self.pos//8+1 == (self.pos+item)//8 or self.pos//8-1 == (self.pos+item)//8):
                mov.append(item+self.pos)
        if self.pos%8 != 0 and board[self.pos] != board[self.pos-1]:
            mov.append(self.pos-1)
        if (self.pos+1)%8 != 0 and board[self.pos] != board[self.pos+1]:
            mov.append(self.pos+1)
        pygame.draw.rect(screen,(120,255,20),(x*(self.pos%8),x*(7-self.pos//8),x,x),5,-1)
        return tuple(mov)
    def draw(self):
        if board[self.pos] == True:
            screen.blit(b_piece["king"],(x*(self.pos%8),x*(7-self.pos//8)+6))
        elif board[self.pos] == False:
            screen.blit(w_piece["king"],(x*(self.pos%8),x*(7-self.pos//8)+6))


class queen:
    count = 0
    def __init__(self):
        if queen.count == 2:
            return
        elif queen.count == 1:
            queen.count = 2
            if player_1:
                self.pos = 60
            else:
                self.pos = 59
            board[self.pos] = False
        elif queen.count ==0:
            queen.count =1
            if player_1:
                self.pos = 4
            else:
                self.pos = 3
            board[self.pos] = True
    def avail(self):
        mov =[]
        for i in range(self.pos+1,8*(self.pos//8+1)):
            if board[i]== board[self.pos] :
                break
            mov.append(i)
            if board[i]!= board[self.pos] and board[i]!=None :
                break
        for i in range(self.pos-1,8*(self.pos//8)-1,-1):
            if board[i]== board[self.pos] :
                break
            mov.append(i)
            if board[i]!= board[self.pos] and board[i] != None :
                break
        for i in range(self.pos+8,64,8):
            if board[i]== board[self.pos] :
                break
            mov.append(i)
            if board[i] != board[self.pos] and board[i]!=None:
                break
        for i in range(self.pos-8,-1,-8):
            if board[i]== board[self.pos] :
                break
            mov.append(i)
            if board[i]!= board[self.pos] and board[i] != None:
                break
        for i in range(self.pos+7,64,7):
            if  (i+1)%8==0 or board[i]== board[self.pos]:
                break
            mov.append(i)
            if board[i] != board[self.pos] and board[i] != None:
                break
        for i in range(self.pos-7,-1,-7):
            if  i%8==0 or board[i]== board[self.pos]:
                break
            mov.append(i)
            if board[i]!= board[self.pos]  and board[i] != None:
                break
        for i in range(self.pos+9,64,9):
            if  i%8==0 or board[i]== board[self.pos]:
                break
            mov.append(i)
            if board[i] != board[self.pos] and board[i] != None:
                break
        for i in range(self.pos-9,-1,-9):
            if (i+1)%8==0 or board[i]== board[self.pos]:
                break
            mov.append(i)
            if board[i] != board[self.pos] and board[i] != None:
                break
        pygame.draw.rect(screen,(120,255,20),(x*(self.pos%8),x*(7-self.pos//8),x,x),5,-1)
        return tuple(mov)
    def draw(self):
        if board[self.pos] == True:
            screen.blit(b_piece["queen"],(x*(self.pos%8),x*(7-self.pos//8)+6))
        elif board[self.pos] == False:
            screen.blit(w_piece["queen"],(x*(self.pos%8),x*(7-self.pos//8)+6))


class bishop:
    count = 0
    def __init__(self):
        if bishop.count == 4:
            return
        elif bishop.count == 3:
            bishop.count = 4
            self.pos = 61
            board[self.pos] = False
        elif bishop.count == 2:
            bishop.count = 3
            self.pos = 58
            board[self.pos] = False
        elif bishop.count == 1:
            bishop.count = 2
            self.pos = 5
            board[self.pos] = True
        elif bishop.count == 0:
            bishop.count = 1
            self.pos = 2
            board[self.pos] = True
    def avail(self):
        mov =[]
        for i in range(self.pos+7,64,7):
            if  (i+1)%8==0 or board[i]== board[self.pos]:
                break
            mov.append(i)
            if board[i] != board[self.pos] and board[i] != None:
                break
        for i in range(self.pos-7,-1,-7):
            if  i%8==0 or board[i]== board[self.pos]:
                break
            mov.append(i)
            if board[i]!= board[self.pos]  and board[i] != None:
                break
        for i in range(self.pos+9,64,9):
            if  i%8==0 or board[i]== board[self.pos]:
                break
            mov.append(i)
            if board[i] != board[self.pos] and board[i] != None:
                break
        for i in range(self.pos-9,-1,-9):
            if (i+1)%8==0 or board[i]== board[self.pos]:
                break
            mov.append(i)
            if board[i] != board[self.pos] and board[i] != None:
                break
        pygame.draw.rect(screen,(120,255,20),(x*(self.pos%8),x*(7-self.pos//8),x,x),5,-1)
        return tuple(mov)
    def draw(self):
        if board[self.pos] == True:
            screen.blit(b_piece["bishop"],(x*(self.pos%8),x*(7-self.pos//8)+6))
        elif board[self.pos] == False:
            screen.blit(w_piece["bishop"],(x*(self.pos%8),x*(7-self.pos//8)+6))
            
class rook:
    count = 0
    def __init__(self):
        if rook.count == 4:
            return
        elif rook.count == 3:
            rook.count = 4
            self.pos = 63
            board[self.pos] = False
        elif rook.count == 2:
            rook.count = 3
            self.pos = 56
            board[self.pos] = False
        elif rook.count == 1:
            rook.count = 2
            self.pos = 7
            board[self.pos] = True
        elif rook.count == 0:
            rook.count = 1
            self.pos = 0
            board[self.pos] = True
    def avail(self):
        mov =[]
        for i in range(self.pos+1,8*(self.pos//8+1)):
            if board[i]== board[self.pos] :
                break
            mov.append(i)
            if board[i]!= board[self.pos] and board[i]!=None :
                break
        for i in range(self.pos-1,8*(self.pos//8)-1,-1):
            if board[i]== board[self.pos] :
                break
            mov.append(i)
            if board[i]!= board[self.pos] and board[i] != None :
                break
        for i in range(self.pos+8,64,8):
            if board[i]== board[self.pos] :
                break
            mov.append(i)
            if board[i] != board[self.pos] and board[i]!=None:
                break
        for i in range(self.pos-8,-1,-8):
            if board[i]== board[self.pos] :
                break
            mov.append(i)
            if board[i]!= board[self.pos] and board[i] != None:
                break
        pygame.draw.rect(screen,(120,255,20),(x*(self.pos%8),x*(7-self.pos//8),x,x),5,-1)
        return tuple(mov)
    def draw(self):
        if board[self.pos] == True:
            screen.blit(b_piece["rook"],(x*(self.pos%8),x*(7-self.pos//8)+6))
        elif board[self.pos] == False:
            screen.blit(w_piece["rook"],(x*(self.pos%8),x*(7-self.pos//8)+6))

        
class knight:
    count = 0
    def __init__(self):
        if knight.count ==4:
            return
        elif knight.count == 3:
            knight.count += 1
            self.pos = 62
            board[self.pos] = False
        elif knight.count == 2:
            knight.count += 1
            self.pos = 57
            board[self.pos] = False
        elif knight.count == 1:
            knight.count += 1
            self.pos = 6
            board[self.pos] = True
        elif knight.count == 0:
            knight.count += 1
            self.pos = 1
            board[self.pos] = True
    def avail(self):
        X = self.pos%8
        Y = self.pos//8
        mov = []
        temp = ((2, 1), (2, -1), (-2, 1), (-2, -1))
        for i,j in temp:
            mov.append((i+X,j+Y))
            mov.append((X+j,Y+i))
        temp = list(filter(lambda a : 0 <= a[0] <8 and 0 <= a[1] <8,mov))
        mov = []
        for item in temp:
            if board[item[0]+8*item[1]] != board[self.pos] :
                mov.append(item[0]+8*item[1])
        pygame.draw.rect(screen,(120,255,20),(x*(self.pos%8),x*(7-self.pos//8),x,x),5,-1)
        return tuple(mov)
    def draw(self):
        if board[self.pos] == True:
            screen.blit(b_piece["knight"],(x*(self.pos%8),x*(7-self.pos//8)+6))
        elif board[self.pos] == False:
            screen.blit(w_piece["knight"],(x*(self.pos%8),x*(7-self.pos//8)+6))


class pawn:
    count = 0
    def __init__(self):
        if pawn.count == 16:
            return
        elif pawn.count > 7:
            pawn.count += 1
            self.pos = 39 + pawn.count
            board[self.pos] = False
        else :
            pawn.count += 1
            self.pos = pawn.count + 7
            board[self.pos] = True
    def avail(self):
        mov = []
        if board[self.pos] is True :
            if self.pos <56 and board[self.pos+8] == None :
                mov = [self.pos+8]
            if self.pos//8 == 1 and board[self.pos+8] is None and board[self.pos+16] is not True:
                mov.append(self.pos+16)
            if self.pos <56 and board[self.pos+7] is False and self.pos%8 > 0:
                mov.append(self.pos+7)
            if self.pos <55 and board[self.pos+9] is False and self.pos%8 < 7:
                mov.append(self.pos+9)
        elif board[self.pos] is False:
            if board[self.pos-8] == None :
                mov = [self.pos-8]
            if self.pos//8 == 6 and board[self.pos-8] is None and board[self.pos-16] is not False:
                mov.append(self.pos-16)
            if board[self.pos-7] is True and self.pos%8 <7  :
                mov.append(self.pos-7)
            if board[self.pos-9] is True and self.pos%8 > 0:
                mov.append(self.pos-9)
        else:
            mov = False
        pygame.draw.rect(screen,(120,255,20),(x*(self.pos%8),x*(7-self.pos//8),x,x),5,-1)
        return tuple(mov)

    def draw(self):
        if board[self.pos]==True:
            screen.blit(b_piece["pawn"],(x*(self.pos%8)+5,x*(7-self.pos//8)+10))
        elif board[self.pos] == False:
            screen.blit(w_piece["pawn"],(x*(self.pos%8)+5,x*(7-self.pos//8)+10))
        
    # construction

class chess:
    def __init__(self,black):
        self.p1=[]
        global player_1,b_piece,w_piece
        player_1 = black
        if not black :
            b_piece,w_piece = w_piece,b_piece

        self.p1.append(rook())
        self.p1.append(knight())
        self.p1.append(bishop())
        if player_1:
            self.p1.append(king())
            self.p1.append(queen())
        else:    
            self.p1.append(queen())
            self.p1.append(king())
        self.p1.append(bishop())
        self.p1.append(knight())
        self.p1.append(rook())

        for i in range(8,16):
            self.p1.append(pawn())

        for i in range(16,48):
            self.p1.append(None)

        for i in range(48,56):
            self.p1.append(pawn())

        self.p1.append(rook())
        self.p1.append(knight())
        self.p1.append(bishop())
        if player_1:
            self.p1.append(king())
            self.p1.append(queen())
        else:    
            self.p1.append(queen())
            self.p1.append(king())
        self.p1.append(bishop())
        self.p1.append(knight())
        self.p1.append(rook())
        
    def draw(self):
        for i in range(64):
            if board[i]== True or board[i] == False:
                self.p1[i].draw()


black = (50,50,50)
white = (255,255,255)
box=white

def change(box):
    if box == black:
        return white
    else :
        return black

c = chess(False)
turn = True

def draw_boxes():
    global box
    for i in range(0,x*8,x):
        for j in range(0,x*8,x):
            pygame.draw.rect(screen,box,(i,j,x,x))
            box=change(box)
        box=change(box)

draw_boxes()
c.draw()
avai =[]
# game stuffs
running =True
while running:
    
    mo_pos =pygame.mouse.get_pos()
    state = pygame.mouse.get_pressed()[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    pygame.display.update()

    if state :
        draw_boxes()
        c.draw()
        
        pos = mo_pos[0]//x+8*(7-mo_pos[1]//x)
        if pos in avai and board[pos0] == turn :
            c.p1[pos] = c.p1[pos0]
            c.p1[pos0] = None
            board[pos] = board[pos0]
            board[pos0]= None
            c.p1[pos].pos = pos
            turn = not turn
            avai = []
            c.p1[pos].draw()
        elif c.p1[pos] is not None and board[pos]== turn :
            avai=c.p1[pos].avail()
            pos0 = pos
        else :
            avai = []
        for items in avai :   
            pygame.draw.rect(screen,(255,20,20),(x*(items%8),x*(7-items//8),x,x),5,-1)
