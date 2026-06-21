import pygame 

pygame.init()

screen = pygame.display.set_mode((640, 640))

text_font = pygame.font.SysFont("Arial", 30)

def draw_text(text, font, text_col, x, y):
    
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

running = True
while running:

    screen.fill((255, 255, 255)) 
    
    
    draw_text("Hi Game", text_font, (0, 100, 50), 220, 150)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.display.flip()

pygame.quit()