import pygame
import random

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Custom Event: Color Change")

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

COLORS = [
    pygame.Color('crimson'), 
    pygame.Color('chartreuse'), 
    pygame.Color('dodgerblue'), 
    pygame.Color('gold'), 
    pygame.Color('darkorchid')
]

class ColoredBox(pygame.sprite.Sprite):
    def __init__(self, color, size, pos):
        super().__init__()
        self.image = pygame.Surface(size)
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=pos)

    def change_color(self):
        self.color = random.choice(COLORS)
        self.image.fill(self.color)

sprite1 = ColoredBox(pygame.Color('white'), (80, 80), (200, 200))
sprite2 = ColoredBox(pygame.Color('white'), (80, 80), (400, 200))

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    screen.fill((20, 20, 20))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()