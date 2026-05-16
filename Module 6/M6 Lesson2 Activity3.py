import pygame

def main():
    pygame.init()
    sw, sh = 600, 600
    screen = pygame.display.set_mode((sw, sh))
    pygame.display.set_caption('Adaptive Sprite')

    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'gold': (255, 215, 0),
        'white': (255, 255, 255)
    }
    
    current_color = colors['white']
    x, y = 100, 100
    size = 50
    clock = pygame.time.Clock()
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: x -= 5
        if keys[pygame.K_RIGHT]: x += 5
        if keys[pygame.K_UP]: y -= 5
        if keys[pygame.K_DOWN]: y += 5

        x = min(max(0, x), sw - size)
        y = min(max(0, y), sh - size)

        if x == 0:
            current_color = colors['blue']
            size = max(20, size - 1)
        elif x == sw - size:
            current_color = colors['gold']
            size = max(20, size - 1)
        elif y == 0:
            current_color = colors['red']
            size = min(150, size + 1)
        elif y == sh - size:
            current_color = colors['green']
            size = min(150, size + 1)
        else:
            current_color = colors['white']

        screen.fill((20, 20, 20))
        pygame.draw.rect(screen, current_color, (x, y, size, size))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()