import pygame
import random
import sys


pygame.init()


WIDTH, HEIGHT = 1280,720
TARGET_RADIUS = 30
TARGET_COLOR = (168,206,131)
BACKGROUND_COLOR = (85,99,135)
FPS = 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

# Game variables
score = 0
target_pos = (random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS), 
               random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS))

# Font
font = pygame.font.Font(None, 46)

# Background music
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1) 

def draw_target(position):
    pygame.draw.circle(screen, TARGET_COLOR, position, TARGET_RADIUS)

def display_score(score):
    score_surface = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_surface, (10, 10))

def main():
    global target_pos, score
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if (target_pos[0] - TARGET_RADIUS < mouse_pos[0] < target_pos[0] + TARGET_RADIUS and
                    target_pos[1] - TARGET_RADIUS < mouse_pos[1] < target_pos[1] + TARGET_RADIUS):
                    score += 1
                    target_pos = (random.randint(TARGET_RADIUS, WIDTH - TARGET_RADIUS), 
                                  random.randint(TARGET_RADIUS, HEIGHT - TARGET_RADIUS))

        # background
        screen.fill(BACKGROUND_COLOR)

        # target and score
        draw_target(target_pos)
        display_score(score)

        # Update the display
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()