import os
import pygame


# main window
pygame.init()
win_height, win_width = 900, 500
res = (win_width, win_height)
window = pygame.display.set_mode((res))
pygame.display.set_caption("Stellar Solver")

# Constant Variables
FPS = 60


# RGB colour values
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

# button class
class button:
    def __init__(self, x, y, width, height, colour):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour

    def make_button(self):
        button = pygame.Rect(self.x, self.y, self.width, self.height)
        return button

play_button = button(0, 0, 390, 100, white)
rect_list = [play_button]

class text:
    def __init__(self, x, y, font, font_size, colour, char):

        self.x = x
        self.y = y
        self.font = font
        self.font_size = font_size
        self.colour = colour
        self.char = char
    
    def make_text(self):
        text = pygame.font.SysFont(self.font, self.font_size)
        return text


title_text = text(230, 0,"briel", 100, white, "Stellar")
play_button_text = text(390, 110, "ariel", 30, white, "Play")

text_list = [title_text, play_button_text]


"""Updates and runs the main menu"""
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
        main_menu_draw(rect_list, text_list)

"""handles drawing objects on the main menu"""
def main_menu_draw(rect_list, text_list):

    # rendering buttons themselves
    for rect in rect_list: 
        pygame.draw.rect(window, rect.colour, rect.make_button())

    # rendering text for the buttons
    for text in text_list:
        button_text = text.make_text().render(text.char, True, text.colour)
        window.blit(button_text, (text.x, text.y))

    pygame.display.update()

main_menu_run()