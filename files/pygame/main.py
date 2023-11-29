import pygame, random, string
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640,360))
class Animation:
    def __init__(self, frames, delay):
        self.frames = frames
        self.delay = delay
        self.timer = 0
    def update(self, dt):
        timer += dt
        if self.value >= len(curAnimPlayer):
            value = 0
        if timer > 0.05:
            self.value += 1
            self.timer = 0
            if self.value >= len(self.frames):
                self.value = 0
running = True
playerRect = pygame.Rect(320-16, 180-32, 25,65)
idle = [
    pygame.image.load("./img/homer/idle/frame1.png")
    ]
walk =[
    pygame.image.load("./img/homer/walking/frame0.png"),
    pygame.image.load("./img/homer/walking/frame1.png"),
    pygame.image.load("./img/homer/walking/frame2.png"),
    pygame.image.load("./img/homer/walking/frame3.png"),
    pygame.image.load("./img/homer/walking/frame4.png"),
    pygame.image.load("./img/homer/walking/frame5.png"),
    pygame.image.load("./img/homer/walking/frame6.png"),
    pygame.image.load("./img/homer/walking/frame7.png"),
]
fall = [
    pygame.image.load("./img/homer/fall.png")
]
jump = [
    pygame.image.load("./img/homer/jump.png")
]
curAnimPlayer = idle
pos = [0,0]
movingD = False
movingR = False
movingL = False
movingU = False
facingLeft = False
clock = pygame.time.Clock()
mapp = pygame.image.load("./img/map.png")
"""[
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,0],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]"""

def MakePxMap(pxMap):

    outMap = []

    for x in range(len(pxMap)):
        outMap.append([])
        for y in range(len(pxMap[0])):
            outMap[x].append(0)
    for x in range(len(pxMap)):
        for y in range(len(pxMap[0])):
            #print(pxMap[0])
            if pxMap[x][y] == -16777216: outMap[x][y] = 0
            else: outMap[x][y] = 1

    return outMap

tile = pygame.image.load("./img/tile.png")

def lerp( a, b, f):
    return a * (1.0 - f) + (b * f)

def GetPos(rect):
    global pos
    return pygame.Rect(rect.x-pos[0],rect.y-pos[1],rect.width,rect.height)

def MakeMap(tile,mapVal,width,height):
    rectMap = []
    print(len(mapVal))
    print(len(mapVal[0]))
    for x in range(len(mapVal)):
        for y in range(len(mapVal[0])):
        
            if mapVal[x][y] == 1:
                rectMap.append(pygame.Rect(100+(x*tile.get_width()),100+(y*tile.get_height()),tile.get_width(),tile.get_height()))
            
    return rectMap
rectMapp = MakeMap(tile,MakePxMap(pygame.PixelArray(mapp)),6,5)
velY = 0
dt = 0
moveSpeed = 200
gravity = 20

jumpHeight = -800
velX = 0

FPS = 60
grounded = False
value = 0

timer = 0
def anim():
    global curAnimPlayer
    
    if grounded:
        
        if velX > 0.3 or velX < -0.3:
            curAnimPlayer = walk
            return
    else:
        if velY > 0.1:
            curAnimPlayer = fall
            return
        else:
            curAnimPlayer = jump
            return
    curAnimPlayer = idle

while running:
    pygame.display.set_caption(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
    pygame.display.set_icon(curAnimPlayer[value])
    timer += dt
    anim()

        
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_a:
                movingL = True
                facingLeft = True
            elif event.key==K_d:
                movingR = True
                facingLeft = False
            elif event.key==K_w:
                print(velY)
                if grounded:
                    velY = jumpHeight * dt
                movingU = True
            elif event.key == K_s:
                movingD = True
        if event.type == pygame.KEYUP:
            if event.key == K_a:
                movingL = False
            elif event.key==K_d:
                movingR = False
            elif event.key==K_w:
                movingU = False
            elif event.key == K_s:
                movingD = False
    if movingL:
        velX = -moveSpeed*dt
    if movingR:
        velX = moveSpeed*dt
    if not movingR and not movingL:
        velX = lerp(velX,0,dt*10)

    velY += dt*gravity
    
    canMoveY = True
    canMoveX = True
    grounded = False
    for i in rectMapp:
        if pygame.Rect(playerRect.x,playerRect.y+10,playerRect.width,playerRect.height).colliderect(GetPos(i)):
            grounded = True
            
        if pygame.Rect(playerRect.x,playerRect.y+velY,playerRect.width,playerRect.height).colliderect(GetPos(i)):
            canMoveY = False
            velY = 0
        if pygame.Rect(playerRect.x+velX,playerRect.y-1,playerRect.width,playerRect.height).colliderect(GetPos(i)):
            canMoveX = False
            velX = 0
    if canMoveY: pos[1] += velY
    if canMoveX: pos[0] += velX

    
    screen.fill("skyblue")
    for i in rectMapp:
        #pygame.draw.rect(screen,"blue",GetPos(i))
        screen.blit(tile, GetPos(i))

    if value+1 > len(curAnimPlayer):
        value -= 1
    image = curAnimPlayer[value]
    if facingLeft:
        image = pygame.transform.flip(image, True, False)
    screen.blit(image,pygame.Rect(playerRect.x-10,playerRect.y,playerRect.width,playerRect.height))
    #pygame.draw.rect(screen,"red",playerRect)
    dt = clock.tick(FPS) / 1000
    pygame.display.update()

pygame.quit()
