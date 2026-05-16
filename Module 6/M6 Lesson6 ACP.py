import pygame
import random

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Background and Sound Integration")


background = pygame.image.load("Space Background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.mixer.music.load("Motivational Background Music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)  # -1 makes it loop indefinitely

collision_sound = pygame.mixer.Sound("effect.wav")

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((70, 70))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))

    def update_color(self):
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(new_color)
        collision_sound.play() # Trigger sound effect

sprite1 = CustomSprite(pygame.Color('cyan'), 250, 300)
sprite2 = CustomSprite(pygame.Color('magenta'), 550, 300)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.update_color()
            sprite2.update_color()

    
    screen.blit(background, (0, 0))
    
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()