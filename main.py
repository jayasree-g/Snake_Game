import pygame
import random
from pygame import *
import time

pygame.init()
window_x = 900
window_y = 700
snake_x = 30
snake_y = 50
x_change = 0
y_change = 0
snake_x1 = 40
snake_y1 = 40
length = 0
snake_speed = 15
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption("Snake Game by Jayasree")
game_window.fill((0, 0, 0))

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
score = 0
value = score_font.render("Your Score: " + str(score), True, (222, 222, 222))
game_window.blit(value, [0, 0])
snake = pygame.image.load("snake.png").convert()
target_x = random.randrange(1, (window_x // 10)) * 10
target_y = random.randrange(1, (window_y // 10)) * 10
target = pygame.image.load("apple.png").convert()
target = pygame.transform.scale(target, (50, 34))
game_window.blit(target, (30, 70))
game_window.blit(value, [0, 0])
pygame.display.flip()
clock = pygame.time.Clock()
running = True
while running:
    if 0 == snake_x or snake_x == window_x or 0 == snake_y or snake_y == window_y or 0 == snake_x1 or snake_x1 == window_x or 0 == snake_y1 or snake_y1 == window_y:
        running = False
    # if score > 50:
    #   snake_speed = 20
    # elif score > 70:
    #   snake_speed = 30
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.key == K_UP:
                y_change = -10
                x_change = 0
            elif event.key == K_DOWN:
                y_change = 10
                x_change = 0
            elif event.key == K_LEFT:
                y_change = 0
                x_change = -10
            elif event.key == K_RIGHT:
                y_change = 0
                x_change = 10
    snake_x += x_change
    snake_y += y_change
    game_window.fill((0, 0, 0))

    snake = pygame.transform.scale(snake, (30, 30))

    game_window.blit(value, [0, 0])
    if target_x < snake_x < target_x + 50 and target_y < snake_y < target_y + 34 or target_x < snake_x + 30 < target_x + 50 and target_y < snake_y + 30 < target_y + 34:
        target_x = random.randrange(1, (window_x // 10)) * 10
        target_y = random.randrange(1, (window_y // 10)) * 10
        score += 10
        length += score
        if score % 50 == 0:
            snake_speed += 10
    snake = pygame.transform.scale(snake, (30 , 30))
    game_window.blit(target, (target_x, target_y))
    game_window.blit(snake, (snake_x, snake_y))
    value = score_font.render("Your Score: " + str(score), True, (222, 222, 222))
    pygame.display.update()
    clock.tick(snake_speed)
pygame.quit()
quit()
