import os
import pygame


# main window
pygame.init()
win_height, win_width = 500, 900
res = (win_width, win_height)
window = pygame.display.set_mode((res))
pygame.display.set_caption("Stellar Solver")

# Constant Variables
FPS = 60


# RGB colour values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# makes new button rectangles using teh button class
class Button:
    def __init__(self, x, y, width, height, colour, button_func):
        
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.func = button_func

    def make_button(self):
        button = pygame.Rect(self.x, self.y, self.width, self.height)
        return button

# base balck rectangle
baseplate = Button(0,0, win_width, win_height, BLACK, "")

# all the buttons on the main menu
play_button = Button(390, 100, 120, 50, WHITE, "gameplay_main()")
highscore_button = Button(390, 175,  120, 50, WHITE, "highscore_main_draw()")
controls_button = Button(390, 250, 120, 50, WHITE, "controls_main_draw()")
main_menu_exit_button = Button(390, 325,  120, 50, WHITE, "pygame.quit()")

menu_rect_list = [baseplate, play_button, highscore_button, controls_button
             ,main_menu_exit_button]

# all the button in the gameplay window
gameplay_back_menu = Button(0, 0,  120, 50, WHITE, "main_menu_run()")

gameplay_rect_list = [baseplate, gameplay_back_menu]

# makes new text boxes through the Text class
class Text:
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

# all the text on the main menu
title_text = Text(230, 0,"", 100, WHITE, "Stellar Solver")
play_button_text = Text(390, 110, "ariel", 30, BLACK, "Play Game")
highscore_button_text = Text(390, 175, "ariel", 30, BLACK, "Highscores")
controls_button_text = Text(390, 250, "ariel", 30, BLACK, "Controls")
main_menu_exit_text = Text(390, 325, "ariel", 30, BLACK, "Exit")

menu_text_list = [title_text, play_button_text, highscore_button_text
             , controls_button_text, main_menu_exit_text]

gameplay_back_menu_text = Text(0, 0, "ariel", 30, BLACK, "Main Menu")

gameplay_text_list = [gameplay_back_menu_text]


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

            # checking for mouse clicks to activate buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button in menu_rect_list:
                    if button.x + button.width > x > button.x and button.y + button.height > y > button.y:
                        run = False
                        try:
                            eval(button.func)
                        except SyntaxError:
                            True
                        


        draw(menu_rect_list, menu_text_list)

"""draws all items in the inputted lists"""
def draw(rect_list, text_list):

    # rendering buttons themselves
    for rect in rect_list: 
        pygame.draw.rect(window, rect.colour, rect.make_button())

    # rendering text for the buttons
    for text in text_list:
        button_text = text.make_text().render(text.char, True, text.colour)
        window.blit(button_text, (text.x, text.y))

    pygame.display.update()

"""the handling center the gameplay features"""
def gameplay_main():
    # Timer making the game run 60 times each second.
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Allowing the program to stop more cleanly 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                for button in gameplay_rect_list:
                    if button.x + button.width > x > button.x and button.y + button.height > y > button.y:
                        run = False
                        try:
                            eval(button.func)
                        except SyntaxError:
                            True

        draw(gameplay_rect_list, gameplay_text_list)

    
"""Handles showing highscore when the button is clicked from main menu."""
def highscore_main_draw():
    print("highscore")

"""Draws a help image for users when button is clicked."""
def controls_main_draw():
    print("controls")

main_menu_run()