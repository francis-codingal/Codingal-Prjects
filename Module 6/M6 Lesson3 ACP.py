import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BG_COLOR = (30, 30, 30)
PLAYER_COLOR = (0, 255, 150)
STATIC_COLOR = (255, 100, 100)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Multi-Sprite Movement")

class Box(pygame.sprite.Sprite):
    def __init__(self, color, width, height, pos):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

player = Box(PLAYER_COLOR, 50, 50, (100, 100))
static_sprite = Box(STATIC_COLOR, 60, 60, (370, 270))

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(static_sprite)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    screen.fill(BG_COLOR)
    all_sprites.draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()