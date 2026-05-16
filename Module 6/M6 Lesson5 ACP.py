import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Custom Event: Color Change")

COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(COLOR_EVENT, 1500)

class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update_color(self):
        new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.image.fill(new_color)

sprite1 = CustomSprite(pygame.Color('red'), 150, 170)
sprite2 = CustomSprite(pygame.Color('blue'), 350, 170)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == COLOR_EVENT:
            sprite1.update_color()
            sprite2.update_color()

    screen.fill((40, 40, 40))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
