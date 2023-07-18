"""An educational game"""
import pygame

# pylint: disable=no-member, W0123

# global variables


# main window
pygame.init()
win_height, win_width = 1080, 1920
res = (win_width, win_height)
window = pygame.display.set_mode((res))
pygame.display.set_caption("Stellar Solver")

# Constant Variables.
FPS = 1

# Changing variables.
LIVES = 3


# RGB colour values
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# added events
PLAYER_HIT = pygame.USEREVENT + 1

# making event last for 500ms


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
play_button = Button(win_width/2 - 60, 100, 120, 50, WHITE, "gameplay_main()")
highscore_button = Button(
    win_width/2 - 60, 175,  120, 50, WHITE, "highscore_main_draw()")
controls_button = Button(win_width/2 - 60, 250, 120,
                         50, WHITE, "controls_main_draw()")
main_menu_ex_cordit_button = Button(
    win_width/2 - 60, 325,  120, 50, WHITE, "sys.exit()")

menu_rect_list = [baseplate, play_button, highscore_button,
                  controls_button, main_menu_ex_cordit_button]

# all the button in the gameplay window
gameplay_back_menu = Button(0, 0,  200, 50, WHITE, "main_menu_run()")

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


class Enemy:
    """ Eneemy class to create enemies for the player to interact with"""

    def __init__(self, x_cord, y_cord, width, height, colour, value, activated, speed):

        self.x_cord = x_cord
        self.y_cord = y_cord
        self.width = width
        self.height = height
        self.colour = colour
        self.value = value
        self.activated = activated
        self.speed = speed

    def make_enemy(self):
        """makes a new enemy"""
        enemy_hitbox = pygame.Rect(
            self.x_cord, self.y_cord, self.width, self.height)
        return enemy_hitbox


gp_enemy_list = []


class Bullets:
    """Bullets for both enemies and the player to shoot."""

    def __init__(self, x_cord, y_cord, width, height, colour, team, speed):

        self.x_cord = x_cord
        self.y_cord = y_cord
        self.width = width
        self.height = height
        self.colour = colour
        self.team = team
        self.speed = speed

    def make_bullet(self):
        """makes a new bullet"""
        bullet_hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

gp_bullet_list = []

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
title_text = Text(win_width/2 - 225, 0, "", 100, WHITE, "Stellar Solver")
play_button_text = Text(win_width/2 - 60, 110, "ariel", 30, BLACK, "Play Game")
highscore_button_text = Text(
    win_width/2 - 60, 175, "ariel", 30, BLACK, "Highscores")
controls_button_text = Text(win_width/2 - 60, 250,
                            "ariel", 30, BLACK, "Controls")
main_menu_exit_text = Text(
    win_width/2 - 60, 325, "ariel", 30, BLACK, "Exit")

menu_text_list = [title_text, play_button_text,
                  highscore_button_text, controls_button_text, main_menu_exit_text]

# all the text on the main menu
gameplay_back_menu_text = Text(0, 0, "ariel", 50, BLACK, "Main Menu")
gameplay_lives_text = Text(1700, 0, "ariel", 50, WHITE, "Lives: 3")

gameplay_text_list = [gameplay_back_menu_text, gameplay_lives_text]


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
                        try:
                            eval(rect.func)
                        except SyntaxError:
                            pass

        draw(menu_rect_list, menu_text_list, [], [])


def draw(rect_list, text_list, char_list, enemy_list):
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

    # drawing all enemies
    for enemy in enemy_list:
        pygame.draw.rect(window, enemy.colour, enemy.make_enemy())

    pygame.display.update()


def gameplay_main():
    """the handling center the gameplay features"""
    time = 0
    cooldown = 0

    # Timer making the game run 60 times each second.
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        keys_pressed = pygame.key.get_pressed()

        # Allowing the program to stop more cleanly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # checking where the mouse has clicked and if a button is present
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_cord, y_cord = pygame.mouse.get_pos()
                for rect in gameplay_rect_list:
                    if rect.x_cord + rect.width > x_cord > rect.x_cord and\
                            rect.y_cord + rect.height > y_cord > rect.y_cord:
                        try:
                            eval(rect.func)
                        except SyntaxError:
                            pass
            if keys_pressed[pygame.K_SPACE]:
                for char in gp_char_list:
                    friend_bullet = Bullets(char.x_cord, char.y_cord + char.height/2, 40, 20, BLUE, 1, 20)
                    gp_bullet_list.append(friend_bullet)

            if event.type == PLAYER_HIT and cooldown <= 0:
                gp_character.lives = gp_character.lives - 1
                gameplay_lives_text.char = "Lives: " + str(gp_character.lives)
                cooldown = 1 * FPS

        # Creating 5 enemies every 3 seconds.
        if time >= 3 * FPS:
            time = 0

            for i in range(5):
                enemy = Enemy(win_width - 50, (100 + ((win_height-50) /
                              5) * i), 50, 50, RED, 0, False, 10)
                gp_enemy_list.append(enemy)

        # Running other essential functions for the gameplay to function.
        gameplay_movement(gp_char_list, gp_enemy_list, keys_pressed)
        collision_decttion(gp_char_list, gp_enemy_list)
        draw(gameplay_rect_list, gameplay_text_list, gp_char_list, gp_enemy_list)
        time += 1
        cooldown -= 1


def gameplay_movement(char_list, enemy_list, keys_pressed):
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
    for enemy in enemy_list:
        enemy.x_cord -= enemy.speed


def collision_decttion(char_list, enemy_list):
    """handles the collisions between players, bullets and enemies"""
    for char in char_list:
        for enemy in enemy_list:
            # detects if any charatcer is inside any enemy
            if char.y_cord < (enemy.y_cord + enemy.height) \
                and (char.y_cord + char.height) > enemy.y_cord:
                if char.x_cord > enemy.x_cord \
                    and char.x_cord < (enemy.x_cord + enemy.width) \
                    or (char.x_cord + char.width) > enemy.x_cord \
                    and (char.x_cord + char.width) < (enemy.x_cord + enemy.width):
                    pygame.event.post(pygame.event.Event(PLAYER_HIT))
                    return enemy_list.remove(enemy)

def highscore_main_draw():
    """Handles showing highscore when the button is clicked from main menu."""
    print("highscore")


def controls_main_draw():
    """Draws a help image for users when button is clicked."""
    print("controls")


main_menu_run()
