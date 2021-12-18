import pygame
Mouse_Pos_X=0
Mouse_Pos_Y=0
def Press_Close():
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                
def Click():
    for event in pygame.event.get():
        if event.type == pygame.mouse.get_pressed:
                return False