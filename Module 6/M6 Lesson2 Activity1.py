import pygame  
  
pygame.init()  
window = pygame.display.set_mode((600, 400))  
exit_game = False  
  
while not exit_game:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            exit_game = True  
            
    pygame.draw.rect(window, (255, 100, 0), pygame.Rect(100, 50, 120, 80))    
  
    pygame.display.flip()