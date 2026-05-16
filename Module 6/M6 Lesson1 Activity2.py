import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pygame Visuals')

bg = pygame.transform.scale(
    pygame.image.load('polar region.jpg').convert(),
    (WIDTH, HEIGHT))

sprite = pygame.transform.scale(
    pygame.image.load('Little Penguin.png').convert_alpha(), (150, 150))
sprite_pos = sprite.get_rect(center=(WIDTH // 2, HEIGHT // 3))

label = pygame.font.Font(None, 50).render('Pygame Scene', True,
    pygame.Color('white'))
label_pos = label.get_rect(center=(WIDTH // 2, HEIGHT - 100))

def run():
    timer = pygame.time.Clock()
    active = True
    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False

        screen.blit(bg, (0, 0))
        screen.blit(sprite, sprite_pos)
        screen.blit(label, label_pos)

        pygame.display.update()
        timer.tick(60)

    pygame.quit()

if __name__ == '__main__':
    run()