import pygame
from Code import Ball, Player,Nets
from random import randint


pygame.init()
pygame.mixer.init()

width, height = 600, 300
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Volley Ball.io")

music = pygame.mixer.Sound("Volley_music.mp3")
music.play()
Start_Effect = pygame.mixer.Sound("Start_Game.mp3")
Start_Effect.play()
Hitting_Sound = pygame.mixer.Sound("Hitting_Sound.mp3")
gravity = 0.1
FPS = 60
VolleyBall_x, VolleyBall_y = 285, 150
VolleyBall = Ball("VolleyBall.png", VolleyBall_x, VolleyBall_y, 32, 32)
VolleyBall_speed_y = 0 
VolleyBall_speed_x = 0  
Background = pygame.transform.scale(pygame.image.load("Background.png"), (width, height))
Blue_Player = Player("Blue.png", 170, 150, 32, 32,10)
Red_Player = Player("Red.png", 400, 150, 32, 32,10)
Net = Nets("Net.png",285,160,32,145)

Running = True
clock = pygame.time.Clock()

while Running:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            Running = False

    window.blit(Background, (0, 0))
    Net.load(window)
    
    Blue_Player.load(window)
    Blue_Player.movement()
    Blue_Player.gravity()
    Blue_Player.jumping()

    Red_Player.load(window)
    Red_Player.movement2()
    Red_Player.gravity()
    Red_Player.jumping2()

    if VolleyBall_speed_y != 0 or VolleyBall_speed_x != 0: 
        VolleyBall.y += VolleyBall_speed_y
        VolleyBall_speed_y += gravity  

        if VolleyBall.y >= 265: 
            VolleyBall.y = 265
            VolleyBall_speed_y *= -0.95 

        VolleyBall.x += VolleyBall_speed_x
        if VolleyBall.x <= 0 or VolleyBall.x >= width - 32: 
            VolleyBall_speed_x *= -0.95

    if Blue_Player.rect.colliderect(VolleyBall.rect):
        Hitting_Sound.play()
        VolleyBall_speed_y = -5
        VolleyBall_speed_x = randint(3, 5) * (-1 if VolleyBall.x > Blue_Player.x else 1)

    if Red_Player.rect.colliderect(VolleyBall.rect):
        Hitting_Sound.play()
        VolleyBall_speed_y = -3
        VolleyBall_speed_x = randint(3, 5) * (-1 if VolleyBall.x > Red_Player.x else 1)

    if Net.rect.colliderect(VolleyBall.rect):
        VolleyBall_speed_y = -5
        VolleyBall_speed_x = VolleyBall_speed_x * (-1 if VolleyBall.x > Net.x else 1)
    
    if Blue_Player.rect.colliderect(Net.rect):
        Blue_Player.x = 253
    
    if Red_Player.rect.colliderect(Net.rect):
        Red_Player.x = 317

    VolleyBall.load(window)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
