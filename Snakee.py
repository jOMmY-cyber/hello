import pygame
import time
import random
from pygame import *
pygame.init()


screen = pygame.display.set_mode([300, 300])
clock = pygame.time.Clock()
running = True
red = (255,0,0)
white = (255, 255, 255)
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
gameover = False
pygame.display.set_caption('Show Text')
x = 0
y = 0
a = 300
b = 300
count = 0
snack_body = [(200,200),(200,205)]
speed = 0.5
direction = 'left'
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    key = pygame.key.get_pressed()
    # print('key=',key)
    # 1/0
    if key[K_UP]:
        direction = 'up'
    if key[K_DOWN]:
        direction = 'down'
    if key[K_LEFT]:
        direction = 'left'
    if key[K_RIGHT]:
        direction = 'right'


    screen.fill((255,255,255))
    # walk
    snack_body_temp = []
    for x_, y_ in snack_body:
        if direction == 'up':
            y_-= speed
        if direction == 'down':
            y_+= speed
        if direction == 'left':
            x_-= speed
        if direction == 'right':
            x_+= speed
        snack_body_temp.append((x_,y_))
    snack_body = snack_body_temp

    # draw snack
    for a_, b_ in snack_body:
        a_ = int(a_)
        b_ = int(b_)
        pygame.draw.circle(screen,(0,100,255),(a_,b_),7)
    

    # random point
    thres = 15
    if a > x- thres and a < x + thres and b > y- thres and b < y + thres:
        x = random.randint(0, 300)
        y = random.randint(0, 300)
    pygame.draw.circle(screen,(255,0,0),(x,y),10)

    if x_ >= 300:
        x_ = 1
    if x_ <= 0:
        x_ = 300
    if y_ >= 300:
        y_ = 1
    if y_ <= 0:
        y_ = 300
    # if not match
    count += 1

    #else
    # end print count
    pygame.display.update()
    clock.tick(100) # frame rate
