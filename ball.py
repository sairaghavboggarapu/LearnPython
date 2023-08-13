import pygame
import sys
pygame.init()#this will initiate display module
size = width,height = 1000, 1000
speed = [2, 1]
background = 255, 255, 0
screen = pygame.display.set_mode(size)#initiate a window or screen to display
pygame.display.set_caption("python ball")
ball = pygame.image.load("intro_ball.jpeg")
ballrect = ball.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    screen.fill(background)
    screen.blit(ball, ballrect)
    pygame.display.flip()#update the content to scree
