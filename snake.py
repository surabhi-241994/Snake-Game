import pygame, sys
import random
import time
from pygame.locals import *

def boundary(x,y):
    ymin = 10
    ymax = 490
    xmin = 10
    xmax = 790
    flagx=0
    flagy=0
    if x > xmin and x < xmax :
        flagx=1
    if y > ymin and y < ymax :
        flagy=1
    if flagx ==1 and flagy == 1:
        return 0
    elif flagx==1 and flagy == 0 :
        return 2
    elif flagx == 0 and flagy ==1 :
        return 1
    else:
        return 3
  
pygame.init()
score = 0

FPS = 15 # frames per second setting
fpsClock = pygame.time.Clock()
 
# set up the window
DISPLAYSURF = pygame.display.set_mode([800,500])
surface = pygame.display.get_surface()
pygame.display.set_caption('Animation')
pygame.mixer.music.load('back.mp3')
pygame.mixer.music.play(-1,0.0)
WHITE = (255, 255, 255)
BLUE=(0,0,255)
BLACK=(0,0,0)
YELLOW=(255,255,0)
GREEN=(0,255,0)
apple_image = pygame.image.load('apple.png').convert_alpha()
apple_image = pygame.transform.scale(apple_image,(30,30))
back_image = pygame.image.load('river.jpg.jpg').convert()
snake_head = pygame.image.load('snake_head.jpg').convert_alpha()
snake_head = pygame.transform.scale(snake_head,(30,30))
back_image = pygame.transform.scale(back_image,(800,500))
direction = 'right'

snakecor=[{'x':110,'y':16},
    {'x':102,'y':16}
    ,{'x':94,'y':16},
            {'x':86,'y':16},
          {'x':78,'y':16},
          {'x':70,'y':16},
          {'x':62,'y':16},
          {'x':54,'y':16},
          {'x':46,'y':16},
          {'x':38,'y':16},
          {'x':30,'y':16},
          {'x':22,'y':16},
          {'x':14,'y':16}]
xshift = 8
yshift = 8
maxx = pygame.Surface.get_width(surface)
maxy = pygame.Surface.get_height(surface)
foodcor = {'x' : 0,'y' : 0}
foodflag=0
while True: # the main game loop
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(back_image, [0, 0])
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, 10, 500))
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 490, 800, 500))
    pygame.draw.rect(DISPLAYSURF, BLACK, (790, 0, 800, 490))
    pygame.draw.rect(DISPLAYSURF, BLACK, (0, 0, 800, 10))
    if foodflag == 0:
        print foodcor['x']
        print foodcor['y']
        foodcor['x'] = int(random.random()*(maxx-40))+40
        foodcor['y'] = int(random.random()*(maxy-40))+40
        while foodcor['x']<30 or foodcor['x']>750 or foodcor['y']<50 or foodcor['y']>430 :
            foodcor['x'] = int(random.random()*(maxx-40))+40
            foodcor['y'] = int(random.random()*(maxy-40))+40
        foodflag=1
    #time.sleep(5)
    DISPLAYSURF.blit(apple_image,(foodcor['x'],foodcor['y']))
    #pygame.draw.circle(DISPLAYSURF, WHITE, (foodcor['x'],foodcor['y']), 4, 0)
    count=0

    if snakecor[0]['x'] >= foodcor['x'] and snakecor[0]['x'] <= foodcor['x']+30 and snakecor[0]['y'] >= foodcor['y'] and snakecor[0]['y'] <= foodcor['y']+30:
        foodflag=0
        tempx=snakecor[0]['x']
        tempy=snakecor[0]['y']
        temp = {'x':tempx,'y':tempy}
        if direction == 'left':
            temp['x'] = temp['x'] - 8
        elif direction == 'right':
            temp['x'] = temp['x'] + 8
        elif direction == 'up':
            temp['y'] = temp['y'] - 8
        else :
            temp['y'] = temp['y'] + 8
        snakecor = [temp] + snakecor
        FPS+=1
        score+=100
    
    length = len(snakecor)
    while(count < length-1):
        pygame.draw.circle(DISPLAYSURF, GREEN, (snakecor[count]['x'],snakecor[count]['y']), 6, 0)
        count=count+1
    pygame.draw.circle(DISPLAYSURF, (255,255,0), (snakecor[0]['x'],snakecor[0]['y']), 8, 0)
    #DISPLAYSURF.blit(snake_head,(snakecor[0]['x'],snakecor[0]['y']))

    checker = boundary(snakecor[0]['x'],snakecor[0]['y'])

    if checker==1:
        count=length-1
        while(count >= 1):
            snakecor[count]['x']=snakecor[count-1]['x']
            snakecor[count]['y']=snakecor[count-1]['y']
            #pygame.draw.circle(DISPLAYSURF, BLUE, (snakecor[count]['x'],snakecor[count]['y']), 4, 0)
            count=count-1
        if snakecor[0]['x'] >=789:
            snakecor[0]['x']=11
        else:
            snakecor[0]['x']= 789

    

    if checker ==2:
        count=length-1
        while(count >= 1):
            snakecor[count]['x']=snakecor[count-1]['x']
            snakecor[count]['y']=snakecor[count-1]['y']
            #pygame.draw.circle(DISPLAYSURF, BLUE, (snakecor[count]['x'],snakecor[count]['y']), 4, 0)
            count=count-1
        if snakecor[0]['y'] >= 489:
            snakecor[0]['y']=11
        else:
            snakecor[0]['y']= 489
    
    if direction == 'right':
        count=length-1
        while(count >= 1):
            snakecor[count]['x']=snakecor[count-1]['x']
            snakecor[count]['y']=snakecor[count-1]['y']
            #pygame.draw.circle(DISPLAYSURF, BLUE, (snakecor[count]['x'],snakecor[count]['y']), 4, 0)
            count=count-1
        snakecor[0]['x']+=8
    if direction == 'left':
        count=length-1
        while(count >= 1):
            snakecor[count]['x']=snakecor[count-1]['x']
            snakecor[count]['y']=snakecor[count-1]['y']
            #pygame.draw.circle(DISPLAYSURF, BLUE, (snakecor[count]['x'],snakecor[count]['y']), 4, 0)
            count=count-1
        snakecor[0]['x']-=8
    if direction == 'down':
        count=length-1
        while(count >= 1):
            snakecor[count]['x']=snakecor[count-1]['x']
            snakecor[count]['y']=snakecor[count-1]['y']
            #pygame.draw.circle(DISPLAYSURF, BLUE, (snakecor[count]['x'],snakecor[count]['y']), 4, 0)
            count=count-1
        snakecor[0]['y']+=8
    if direction == 'up':
        count=length-1
        while(count >= 1):
            snakecor[count]['x']=snakecor[count-1]['x']
            snakecor[count]['y']=snakecor[count-1]['y']
            #pygame.draw.circle(DISPLAYSURF, BLUE, (snakecor[count]['x'],snakecor[count]['y']), 4, 0)
            count=count-1
        snakecor[0]['y']-=8
    tempx=snakecor[0]['x']
    tempy=snakecor[0]['y']
    temp = {'x':tempx,'y':tempy}
    temp2=snakecor[2:]
    if temp in temp2:
        pygame.quit()
        sys.exit()    
                      
    for event in pygame.event.get():
      if event.type == KEYDOWN:
        pressed = event.key
        if pressed == pygame.K_UP:
            if direction!= 'down':
                direction = 'up'
        if pressed == pygame.K_LEFT:
            if direction!='right':
                direction = 'left'
        if pressed == pygame.K_DOWN:
            if direction!='up':
                direction = 'down'
        if pressed == pygame.K_RIGHT:
            if direction!='left':
                direction = 'right'
      if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
pygame.mixer.music.stop()
