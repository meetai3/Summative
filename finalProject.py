# Meenal Tailor
# May 23/18
# finalProject.py
# REEEEEEEEEEEEEEEEEEEEEEEEEEEEE! yee.

import pygame

pygame.init()

width=800
height=600
window=pygame.display.set_mode((width,height))



pygame.display.set_caption("Squares and Triangles")

black = (0,0,0)
white = (255,255,255)
red = (255,25,25)

clock = pygame.time.Clock()

box = pygame.image.load("box.png")
box1= pygame.transform.scale(box,(50,50))

def playerbox(x,y):
    window.blit(box1,(x,y))

moveX,moveY=0,0


# starting coordinates for the box image
box1X=width*0.475
box1Y=height*0.9



gameLoop=True

while gameLoop: 
   
      
    for event in pygame.event.get(): 
  
        if (event.type==pygame.QUIT): 
            
            gameLoop=False
  
        if (event.type==pygame.KEYDOWN): 
  
            if (event.key==pygame.K_LEFT): 
  
                moveX = -4
            
            if (event.key==pygame.K_RIGHT): 
  
                moveX = 4
  
            if (event.key==pygame.K_UP): 
  
                moveY = -4
  
            if (event.key==pygame.K_DOWN): 
  
                moveY = 4
  
        if (event.type==pygame.KEYUP): 
  
            if (event.key==pygame.K_LEFT): 
  
                moveX=0
  
            if (event.key==pygame.K_RIGHT): 
  
                moveX=0
  
            if (event.key==pygame.K_UP): 
  
                moveY=0
  
            if (event.key==pygame.K_DOWN): 
  
                moveY=0

    window.fill(white) 

    # box1 moves
    box1X+=moveX
    box1Y+=moveY
    playerbox(box1X,box1Y)


    pygame.display.update()
    clock.tick(50) 

pygame.quit()
