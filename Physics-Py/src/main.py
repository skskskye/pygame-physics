import pygame
from ball import Ball
from vector import Vector2
import random

FPS = 60 #fps
BLACK = (0, 0, 0)

LINE_THICKNESS = 10
WIDTH = 600
HEIGHT = 600
BOOST = 1.5

color = [0, 0, 0]
cycle = False

pygame.init()

fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("physics :3")
font = pygame.font.Font(None, 36)

ball = Ball(0, 0, 25, 255, 255, 255, 9.8, WIDTH - LINE_THICKNESS, HEIGHT - LINE_THICKNESS, (1/FPS), "bounce")
ball.setVelo(Vector2(400, 20))
running = True

print(pygame.display.get_driver())

want = input("want rainbow, Yes or type literally anythinge else dont use this feature its terrible lol: ")

while running:
    print("FAGGOT")


    
 
    if want.upper() == "YES":
#this is not a rainbow but it kinda wrosk i do not care to fix it lol
        if color[2] < 200 and cycle == False:
            color[2] += 1
        elif color[1] < 200 and cycle == False: 
            color[1] += 1
        elif color[0] < 200 and cycle == False: 
            color[0] += 1
        else:
            cycle = True
        if color[2] > 75 and cycle == True:
            color[2] -= 1
        elif color[1] > 75 and cycle == True :
            color[1] -= 1
        elif color[0] > 75 and cycle == True:
            color[0] -= 1
        else:
            cycle = False

    screen.fill((color[0], color[1], color[2]))
    pygame.draw.rect(screen, (30, 30, 30), (0, 0, WIDTH, HEIGHT), LINE_THICKNESS)
    yVelo = ball.velo.y
    xVelo = ball.velo.x
    currentFps = fpsClock.get_fps()
    text = font.render(f"x velo: {int(xVelo)} y velo: {int(yVelo)} fps: {int(currentFps)}", True, (255, 255, 255))  # White color

    text_rect = text.get_rect(center=(300, 20))  # Centered on screen
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.boostY(BOOST)
            elif event.key == pygame.K_DOWN:
                ball.boostY(-BOOST)
            if event.key == pygame.K_RIGHT:
                ball.boostX(BOOST)
            elif event.key == pygame.K_LEFT:
                ball.boostX(-BOOST)
            elif event.key == pygame.K_r:
                if ball.mode == "bounce":
                    ball.pos = Vector2(random.randint(100, 500), random.randint(100, 500))
                    ball.setVelo(Vector2(random.randint(-1000, 1000), random.randint(-200, 200)))
                else:
                    ball.setVelo(Vector2(0, 1))
                    ball.pos = Vector2(0,0)
                
                ball.clearTrail()
            elif event.key == pygame.K_p:
                print("reassign values")
                startingX = int(input("starting x pos: "))
                startingY = int(input("starting y pos: "))
                gravity = float(input("gravity: "))
                mass = float(input("mass: "))
                radius = int(input("radius: "))
                red = int(input("red: "))
                green = int(input("green: "))
                blue = int(input("blue: "))
                

                ball.pos.x = startingX
                ball.pos.y = startingY
                ball.grav = Vector2(0, gravity)
                ball.mass = mass
                ball.radius = radius
                ball.red = red
                ball.green = green
                ball.blue = blue
                ball.clearTrail()
                

                

    
    

    

    screen.blit(text, text_rect)
    ball.render(screen, LINE_THICKNESS)
    
    pygame.display.update()
    fpsClock.tick(FPS)

# Quit Pygame
pygame.quit()