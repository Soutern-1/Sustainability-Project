import pygame
from pygame.sprite import Group
import random

clock = pygame.time.Clock()

pygame.init()
display = pygame.display.set_mode((1000,500))

framerate = 30
framecount = 0
axe_rate = 30

score = 0

axe_speed = -8
popup = True
gameOver = False

tree_image = pygame.image.load("images/tree_image.png").convert_alpha() 
tree_image = pygame.transform.scale(tree_image,(400,150))

menu_image = pygame.image.load("images/main_menu.png")
menu_image = pygame.transform.scale(menu_image,(300,150))

background = pygame.image.load("images/background.png")
# background = pygame.transform.scale(background,(1000,500))



font1 = pygame.font.SysFont("Arial",20)
title = pygame.font.SysFont("Arial",50)
gameOver_text = title.render(f"Game Over.",True,(255,255,255))
score_text = font1.render(f"Score:{score}",True, (255,255,255))

class Axe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        self.image = pygame.image.load("images/axe_image.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = random.randint(100,400)


    def update(self):
        self.rect.x+=axe_speed

class Tree(pygame.sprite.Sprite):
     def __init__(self):
          super().__init__()
          self.image = tree_image
          self.image = pygame.transform.scale(self.image,(250,500))
          self.rect = self.image.get_rect()

#making the groups
tree = Tree()
tree_group = pygame.sprite.Group()
tree_group.add(tree)

axe = Axe()
axe_group = pygame.sprite.Group()
axe_group.add(axe)


while(1):
    display.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if popup == True:
                popup = False


    clock.tick(framerate)

    #What we want when the popup has not yet been closed
    if popup == True:
        display.blit(menu_image,(350,100))
        pygame.display.flip()
        continue

    #what we want to run while the game is running, and the popup has been closed
    if gameOver == False:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        tree_group.draw(display)
        for axe in axe_group:
            axe.update()
            display.blit(axe.image,axe.rect)

            if mouse_pressed[0] and axe.rect.collidepoint(mouse_pos):
                axe.kill()
                score+=1
                score_text = font1.render(f"Score:{score}",True, (255,255,255))
                print(score)

        if pygame.sprite.groupcollide(axe_group, tree_group ,True ,False, collided = None):
            gameOver = True
            print("Collided")

        display.blit(score_text,(0,0))
        pygame.display.flip()
        
    #hadling the interval between axe creations (while game is running)
        framecount += 1
        if framecount >= axe_rate:
            axe = Axe()
            axe_group.add(axe)
            framecount = 0
                
            
    #what we want to run when game ends
    if gameOver == True:
        axe_speed = 0
        final_score_text = font1.render(f"Final Score:{score}",True,(255,255,255))
        display.blit(final_score_text,(150,250))
        display.blit(gameOver_text,(100,200))


    pygame.display.update()


