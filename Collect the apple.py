import pygame,sys,os
from pygame import mixer
from pygame.locals import *
import random

pygame.init()

window=pygame.display.set_mode((800,600 ))
pygame.display.set_caption('Collect the apple')


bg=pygame.image.load('background.png')
bg_2=pygame.image.load('openingimage.png')
apple=pygame.image.load('apple.jpg')
basket=pygame.image.load('basket.jpg')
rotten_apple=pygame.image.load('rotten_apple_2.jpg')

mixer.music.load('backgroung.wav.mp3')
mixer.music.play(-1)

basket_x =400
basket_y =500
apple_x =0
apple_y =0
rotten_apple_1_x=0
rotten_apple_1_y=0
rotten_apple_2_x=0
rotten_apple_2_y=0
apple_speed=1
rotten_apple_speed=1
color=(150,111,25)
text_1='GAME OVER you missed the apple. Press c to continue or q to quit'
text_2='GAME OVER you collected a rotten apple Press c to continue or q to quit '
text_3='SCORE :'
font=pygame.font.SysFont(None,25,bold=True)
font_1=pygame.font.SysFont(None, 40,bold=True,italic=True)
score=0

status_1='ready'
status_2='ready'
def create_apple():
    global status_1 ,apple_x, apple_y
    if status_1 == 'not ready':
        return
    apple_x =random.randint(200,660)
    apple_y =random.randint(32,64)
    status_1 ='not ready'

def create_rotten_apple():
    global status_2 ,rotten_apple_1_x ,rotten_apple_1_y ,rotten_apple_2_x ,rotten_apple_2_y ,apple_x ,apple_y
    if status_2 == 'not ready':
        return
    rotten_apple_1_x =random.randint(0,apple_x-100)
    rotten_apple_1_y =random.randint(32,64)
    rotten_apple_2_x =random.randint(apple_x+100,790)
    rotten_apple_2_y =random.randint(32,64)
    status_2 ='not ready'


def apple_fall():
    global status_1 ,apple_x, apple_y ,apple_speed
    if status_1 == 'ready':
        return
    window.blit(apple, (apple_x,apple_y))
    apple_y =apple_y+apple_speed

def rotten_apple_fall():
    global status_2 ,rotten_apple_1_x ,rotten_apple_1_y ,rotten_apple_2_x ,rotten_apple_2_y ,rotten_apple_speed
    if status_2 == 'ready':
        return
    window.blit(rotten_apple, (rotten_apple_1_x,rotten_apple_1_y))
    window.blit(rotten_apple, (rotten_apple_2_x,rotten_apple_2_y))
    rotten_apple_1_y =rotten_apple_1_y+rotten_apple_speed
    rotten_apple_2_y =rotten_apple_2_y+rotten_apple_speed

def check_collection():
    global status_1 ,apple_x, apple_y ,basket_x ,basket_y ,apple_speed ,score
    xHit =False
    yHit =False
    if apple_x >= basket_x and apple_x <= basket_x+100:
        xHit=True
    if apple_y >= basket_y and apple_y <= basket_y+100:
        yHit=True
    if xHit and yHit:
        score +=1
        status_1= 'ready'
        if score ==10 :
            apple_speed=2
        if score ==20:
            apple_speed=3
        return

def check_wrong_apple_collection():
    global status_2 ,rotten_apple_1_x ,rotten_apple_1_y ,rotten_apple_2_x ,rotten_apple_2_y ,run_3
    if status_2 =='not ready':
         x_Hit=False
         y_Hit=False
         if rotten_apple_1_x >= basket_x-16 and rotten_apple_1_x <=basket_x+100:
             x_Hit=True
         if rotten_apple_1_y >= basket_y and rotten_apple_1_y <=basket_y+100:
             y_Hit=True
         if rotten_apple_2_x >= basket_x-16 and rotten_apple_2_x <=basket_x+100:
             x_Hit=True
         if rotten_apple_2_y >= basket_y and rotten_apple_2_y <=basket_y+100:
             y_Hit=True
         if x_Hit and y_Hit:
             run_3=True
             return

def check_apple_fell_ground():
     global status_1 ,apple_x, apple_y ,basket_x ,basket_y ,run_2
     if status_1 == 'not ready':
         if apple_y ==584:
            run_2 =True

def check_rotten_apple_fell_ground():
    global status_2 ,rotten_apple_1_x ,rotten_apple_1_y ,rotten_apple_2_x ,rotten_apple_2_y ,rotten_apple_speed
    if rotten_apple_1_y >=580 and rotten_apple_2_y >=580:
        status_2='ready'


def message_to_screen_1():
     screen_text_1 =font.render(text_1, True, color )
     window.blit(screen_text_1, (150,300))
     screen_text_4 =font_1.render("YOUR SCORE IS :"+str(score), True, color)
     window.blit(screen_text_4, (200,350))

def message_to_screen_2():
     screen_text_2 =font.render(text_2, True, color)
     window.blit(screen_text_2, (100,300))
     screen_text_4 =font_1.render("YOUR SCORE IS :"+str(score), True, color)
     window.blit(screen_text_4, (200,350))
 
def change_status():
    global status_1 ,status_2 ,score ,apple_speed
    status_1 ='ready'
    status_2 ='ready'
    score =0
    apple_speed =1

def show_score():
    screen_text_3 =font_1.render("SCORE :"+str(score), True, color)
    window.blit(screen_text_3, (600,50))

pygame.display.flip()
run_1 =False
run_2 =False
run_3 =False
run_4 =True
while run_4:
     window.blit(bg_2, (0,0))
     pygame.display.update()
     for event in pygame.event.get():
             if event.type == QUIT:
                 run_4 =False
             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_RETURN:
                     run_4 =False
                     run_1 =True

while run_1:
     window.blit(bg, (0,0))
     while run_2:
         window.fill((255,255,255))
         message_to_screen_1()
         pygame.display.update()
         for event in pygame.event.get():
             if event.type == QUIT:
                 run_1 =False
                 run_2 =False
             if event.type == pygame.KEYDOWN:
                 if event.key ==pygame.K_q:
                     run_1 =False
                     run_2 =False
                 if event.key ==pygame.K_c:
                     change_status()
                     run_2 =False
     while run_3:
         window.fill((255,255,255)) 
         message_to_screen_2() 
         pygame.display.update()
         for event in pygame.event.get():
             if event.type == QUIT:
                 run_1 =False
                 run_3 =False
             if event.type == pygame.KEYDOWN:
                 if event.key ==pygame.K_q:
                     run_1 =False
                     run_3 =False
                 if event.key ==pygame.K_c:
                     change_status()
                     run_3 =False     


     for event in pygame.event.get():
         if event.type == QUIT:
            run_1 =False 
         elif event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
                 basket_x +=35
                 if basket_x >=700:
                    basket_x =700
             elif event.key == pygame.K_LEFT:
                 basket_x -=35
                 if basket_x <=0:
                    basket_x =0

     window.blit(basket, (basket_x,basket_y))
     create_apple()
     create_rotten_apple() 
     apple_fall()
     rotten_apple_fall()
     check_collection()
     check_wrong_apple_collection()
     check_rotten_apple_fell_ground()
     check_apple_fell_ground()
     show_score()

     pygame.display.update()               

                             
