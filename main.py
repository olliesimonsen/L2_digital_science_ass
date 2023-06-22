import os
import pygame

# main window
pygame.init()
res = (900, 500)
window = pygame.display.set_mode((res))
pygame.display.set_caption("Stellar Solver")

# Constant Variables
FPS = 60


# button class
class button:
    def __init__(self, height, width):

        self.width = width
        self.height = height

b1 = button(100,100)
print(b1.height, b1.width)

def main_menu_run():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Allowing the program to stop more cleanly 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()


def main_menu_draw():
    pygame.display.update()