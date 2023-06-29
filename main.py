"""an educational game"""
import pygame

# pylint: disable=no-member, W0123


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

# makes new button rectangles using the Button class


class Button:
    """makes rectangles for buttons"""

    def __init__(self, x_cord, y_cord, width, height, colour, button_func):

        self.x_cord = x_cord
        self.y_cord = y_cord
        self.width = width
        self.height = height
        self.colour = colour
        self.func = button_func

    def make_button(self):
        """makes the rectangles for the button class"""
        button = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        return button


# base balck rectangle
baseplate = Button(0, 0, win_width, win_height, BLACK, "")

# all the buttons on the main menu
play_button = Button(390, 100, 120, 50, WHITE, "gameplay_main()")
highscore_button = Button(
    390, 175,  120, 50, WHITE, "highscore_main_draw()")
controls_button = Button(390, 250, 120, 50, WHITE, "controls_main_draw()")
main_menu_ex_cordit_button = Button(390, 325,  120, 50, WHITE, "pygame.quit()")

menu_rect_list = [baseplate, play_button, highscore_button,
                  controls_button, main_menu_ex_cordit_button]

# all the button in the gameplay window
gameplay_back_menu = Button(0, 0,  120, 50, WHITE, "main_menu_run()")

gameplay_rect_list = [baseplate, gameplay_back_menu]


class Character:
    """character class for the character the user will play as"""

    def __init__(self, x_cord, y_cord, width, height, colour, lives, speed):

        self.x_cord = x_cord
        self.y_cord = y_cord
        self.width = width
        self.height = height
        self.colour = colour
        self.lives = lives
        self.speed = speed

    def make_player(self):
        """makes the players hitbox"""
        hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        return hitbox


# the gameplay character
gp_character = Character(200, 100, 50, 50,  YELLOW, 3, 5)

gp_char_list = [gp_character]


class Text:
    """makes new text boxes through the Text class"""

    def __init__(self, x_cord, y_cord, font, font_size, colour, char):

        self.x_cord = x_cord
        self.y_cord = y_cord
        self.font = font
        self.font_size = font_size
        self.colour = colour
        self.char = char

    def make_text(self):
        """creates the text font"""
        text = pygame.font.SysFont(self.font, self.font_size)
        return text


# all the text on the main menu
title_text = Text(230, 0, "", 100, WHITE, "Stellar Solver")
play_button_text = Text(390, 110, "ariel", 30, BLACK, "Play Game")
highscore_button_text = Text(
    390, 175, "ariel", 30, BLACK, "Highscores")
controls_button_text = Text(390, 250, "ariel", 30, BLACK, "Controls")
main_menu_exit_text = Text(
    390, 325, "ariel", 30, BLACK, "Exit")

menu_text_list = [title_text, play_button_text,
                  highscore_button_text, controls_button_text, main_menu_exit_text]

gameplay_back_menu_text = Text(0, 0, "ariel", 30, BLACK, "Main Menu")

gameplay_text_list = [gameplay_back_menu_text]


def main_menu_run():
    """Updates and runs the main menu"""
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
                x_cord, y_cord = pygame.mouse.get_pos()
                for rect in menu_rect_list:
                    if rect.x_cord + rect.width > x_cord > rect.x_cord and\
                            rect.y_cord + rect.height > y_cord > rect.y_cord:
                        run = False
                        try:
                            eval(rect.func)
                        except SyntaxError:
                            pass

        menu_char_list = []
        draw(menu_rect_list, menu_text_list, menu_char_list)


def draw(rect_list, text_list, char_list):
    """draws all items in the inputted lists"""
    # rendering buttons themselves
    for rect in rect_list:
        pygame.draw.rect(window, rect.colour, rect.make_button())

    # rendering text for the buttons
    for text in text_list:
        button_text = text.make_text().render(
            text.char, True, text.colour)
        window.blit(button_text, (text.x_cord, text.y_cord))

    # displaying all characters
    for char in char_list:
        pygame.draw.rect(window, char.colour, char.make_player())

    pygame.display.update()


def gameplay_main():
    """the handling center the gameplay features"""
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
                x_cord, y_cord = pygame.mouse.get_pos()
                for rect in gameplay_rect_list:
                    if rect.x_cord + rect.width > x_cord > rect.x_cord and\
                            rect.y_cord + rect.height > y_cord > rect.y_cord:
                        run = False
                        try:
                            eval(rect.func)
                        except SyntaxError:
                            pass
        keys_pressed = pygame.key.get_pressed()
        gameplay_movement(gp_char_list, keys_pressed)
        draw(gameplay_rect_list, gameplay_text_list, gp_char_list)


def gameplay_movement(char_list, keys_pressed):
    """handleing movemnt of objects in gameplay"""
    for char in char_list:
        if keys_pressed[pygame.K_a] \
                and char.x_cord - char.speed > 0:  # left
            char.x_cord -= char.speed
        if keys_pressed[pygame.K_d] \
                and char.x_cord + char.speed + char.width < win_width:  # right
            char.x_cord += char.speed
        if keys_pressed[pygame.K_w] \
                and char.y_cord - char.speed > 50:  # up
            char.y_cord -= char.speed
        if keys_pressed[pygame.K_s] \
                and char.y_cord + char.speed + char.height < win_height - 15:  # down
            char.y_cord += char.speed


def highscore_main_draw():
    """Handles showing highscore when the button is clicked from main menu."""
    print("highscore")


def controls_main_draw():
    """Draws a help image for users when button is clicked."""
    print("controls")


main_menu_run()
