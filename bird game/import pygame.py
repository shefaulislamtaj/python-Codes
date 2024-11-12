import pygame
import random
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
GROUND_HEIGHT = 100
PIPE_WIDTH = 70
GRAVITY = 1
JUMP_AMOUNT = -12

# Load images
bird_img = pygame.image.load("bird.png")
bird_img = pygame.transform.scale(bird_img, (50, 40))
pipe_img = pygame.image.load("pipe.png")

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

bird_rect = bird_img.get_rect(center=(100, HEIGHT // 2))
pipe_heights = [200, 250, 300, 350]
pipes = [pipe_img.get_rect(midbottom=(WIDTH + idx * 300, random.choice(pipe_heights))) for idx in range(2)]

clock = pygame.time.Clock()

score = 0

def draw_window():
    win.fill((255, 255, 255))
    win.blit(bird_img, bird_rect)
    for pipe in pipes:
        win.blit(pipe_img, pipe)
    pygame.draw.rect(win, (0, 255, 0), (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))
    
    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    win.blit(text, (20, 20))

    pygame.display.update()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_rect.y += JUMP_AMOUNT

    # Game logic
    bird_rect.y += GRAVITY
    for pipe in pipes:
        pipe.centerx -= 5
        if pipe.right < 0:
            pipe.height = random.choice(pipe_heights)
            pipe.centerx = WIDTH
            score += 1

    # Check collisions
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            running = False

    # Check if the bird has hit the ground or ceiling
    if bird_rect.top <= 0 or bird_rect.bottom >= HEIGHT - GROUND_HEIGHT:
        running = False

    draw_window()
    
    clock.tick(30)

pygame.quit()
sys.exit()
