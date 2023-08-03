"""An educational game"""
import random
import re
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
FPS = 60

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
ENEMY_HIT = pygame.USEREVENT + 2

# defining an image to be used in the game
imp = pygame.image.load(
    "Disc_Controls_Screen.png").convert()



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
    win_width/2 - 60, 175,  120, 50, WHITE, "highscore_main()")
controls_button = Button(win_width/2 - 60, 250, 120,
                         50, WHITE, "control_main()")
main_menu_ex_cordit_button = Button(
    win_width/2 - 60, 325,  120, 50, WHITE, "sys.exit()")

menu_rect_list = [baseplate, play_button, highscore_button,
                  controls_button, main_menu_ex_cordit_button]
# All the buttons in the control window.
control_back_button = Button(0, 0,  200, 50, WHITE, "main_menu_run()")

control_rect_list = [control_back_button] # DO NOT PUT BASEPLATE IN HERE

# All the buttons in the highscore window.
highscore_back_button = Button(0, 0, 200, 50, WHITE, "main_menu_run()")

highscore_rect_list = [baseplate, highscore_back_button]

# all the button in the gameplay window
gameplay_back_menu = Button(0, 0,  200, 50, WHITE, "main_menu_run()")

gameplay_rect_list = [baseplate, gameplay_back_menu]


class Character:
    """character class for the character the user will play as"""

    def __init__(self, x_cord, y_cord, width, height, colour, lives, speed, answer, score):

        self.x_cord = x_cord
        self.y_cord = y_cord
        self.width = width
        self.height = height
        self.colour = colour
        self.lives = lives
        self.speed = speed
        self.answer = answer
        self.score = score

    def make_player(self):
        """makes the players hitbox"""
        hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        return hitbox


# the gameplay character
gp_character = Character(200, 100, 50, 50,  YELLOW, 3, 13, 0, 0)

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

    def make_enemy_answer(self):
        """makes enemies text answers"""
        enemy_text = pygame.font.SysFont("ariel", 100)
        return enemy_text


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
        return bullet_hitbox

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
# All the text in the contorl window.
control_back_text = Text(0, 0, "ariel", 50, BLACK, "Main Menu")

control_text_list = [control_back_text]

# All the text in the highscore window.
highscore_back_text = Text(0, 0, "ariel", 50, BLACK, "Main Menu")

highscore_text_list = [highscore_back_text]

# all the text on the main menu
gameplay_back_menu_text = Text(0, 0, "ariel", 50, BLACK, "Main Menu")
gameplay_lives_text = Text(1700, 0, "ariel", 50, WHITE, "Lives: 3")
gameplay_question_text = Text(400, 0, "ariel", 100, WHITE, "Question: " )
gameplay_score_text = Text(1400, 0, "ariel", 50, WHITE, "Score: 0")

gameplay_text_list = [gameplay_back_menu_text, gameplay_lives_text,
                       gameplay_question_text, gameplay_score_text]

def draw(rect_list, text_list, char_list, enemy_list, bullet_list):
    """draws all items in the inputted lists"""
    # rendering buttons themselves
    for rect in rect_list:
        pygame.draw.rect(window, rect.colour, rect.make_button())

    # displaying all characters
    for char in char_list:
        pygame.draw.rect(window, char.colour, char.make_player())

    # drawing all enemies
    for enemy in enemy_list:
        pygame.draw.rect(window, enemy.colour, enemy.make_enemy())
        enemy_text = enemy.make_enemy_answer()
        button_text = enemy_text.render(str(enemy.value), True, WHITE)
        window.blit(button_text, (enemy.x_cord, enemy.y_cord))

    # drawing all enemies
    for bullet in bullet_list:
        pygame.draw.rect(window, bullet.colour, bullet.make_bullet())

    # rendering all text items
    for text in text_list:
        button_text = text.make_text().render(
            text.char, True, text.colour)
        window.blit(button_text, (text.x_cord, text.y_cord))
    pygame.display.update()

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
                            print(highscore_list)
                            eval(rect.func)
                        except SyntaxError:
                            pass

        draw(menu_rect_list, menu_text_list, [], [], [])

def control_main():
    """helps the user learn the game"""
    draw([baseplate], [], [], [], [])

    window.blit(imp, (450,100))
    pygame.display.update()

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Allowing the program to stop more cleanly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # checking for mouse clicks to activate buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_cord, y_cord = pygame.mouse.get_pos()
                for rect in control_rect_list:
                    if rect.x_cord + rect.width > x_cord > rect.x_cord and\
                            rect.y_cord + rect.height > y_cord > rect.y_cord:
                        try:
                            eval(rect.func)
                        except SyntaxError:
                            pass

        draw(control_rect_list, control_text_list, [], [], [])


def highscore_main():
    """shows the users the current best scores"""
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Allowing the program to stop more cleanly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # checking for mouse clicks to activate buttons
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_cord, y_cord = pygame.mouse.get_pos()
                for rect in highscore_rect_list:
                    if rect.x_cord + rect.width > x_cord > rect.x_cord and\
                            rect.y_cord + rect.height > y_cord > rect.y_cord:
                        try:
                            eval(rect.func)
                        except SyntaxError:
                            pass

        font_size = 50
        i = 0
        for item in highscore_list:
            highscore = Text(win_width/2 - 100, i*font_size, "ariel", font_size, WHITE, str(item))
            highscore_text_list.append(highscore)
            i += 1

        draw(highscore_rect_list, highscore_text_list, [], [], [])

        draw(highscore_rect_list, highscore_text_list, [], [], [])

def gameplay_main():
    """the handling center the gameplay features"""
    enemy_speed = 7
    time = (18.9558 * (0.753947)**enemy_speed + 2.375) * FPS - 3 * FPS
    cooldown = 0
    bullet_reload = 0
    score_update = FPS
    spawn_enemies = True

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
            
            # Creating a Bullet when the spacebar is pressed.
            if keys_pressed[pygame.K_SPACE] and bullet_reload <= 0:
                bullet_reload = 0.7 * FPS
                for char in gp_char_list:
                    friend_bullet = Bullets(
                        char.x_cord, char.y_cord + char.height/2 - 10, 40, 20, BLUE, 1, 20)
                    gp_bullet_list.append(friend_bullet)

            # Making player lose a life when nessercary.
            if event.type == PLAYER_HIT and cooldown <= 0:
                gp_character.lives = gp_character.lives - 1
                gameplay_lives_text.char = "Lives: " + str(gp_character.lives)
                # Stopping all processes when the player loses.
                if gp_character.lives <= 0:
                    loser_text = Text(win_width/2 - 225, win_height/2 - 50, "", 100, WHITE,
                                       "You Lost your score is: " + str(gp_character.score))
                    gameplay_text_list.append(loser_text)
                    run_highscore_input()
                    highscore_main()

                cooldown = FPS

        # Creating 5 enemies every 3 seconds.
        if time >= (18.9558 * (0.753947)**enemy_speed + 2.375) * FPS and spawn_enemies:
            time = 0
            create_enemies(enemy_speed)
        if score_update <= 0:
            score_update = FPS
            gp_character.score += 1
            gameplay_score_text.char = "Score: " + str(gp_character.score)

        # Running other essential functions for the gameplay to function.
        gameplay_movement(gp_char_list, gp_enemy_list, keys_pressed, gp_bullet_list)
        collision_decttion(gp_char_list, gp_enemy_list, gp_bullet_list)
        draw(gameplay_rect_list, gameplay_text_list, gp_char_list, gp_enemy_list, gp_bullet_list)
        time += 1
        cooldown -= 1
        bullet_reload -= 1
        score_update -= 1

def run_highscore_input():
    """Records the users highscore name"""
    text = ""
    input_box = Button(400, 200, 500, 150, WHITE, "")
    gameplay_rect_list.append(input_box)
    input_text = Text(400, 200, "ariel", 50, BLACK, text)
    gameplay_text_list.append(input_text)

    # Timer making the game run 60 times each second.
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Allowing the program to stop more cleanly
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Adding the players score to the highscore database.
                    highscore_info = str(input_text.char + " " + str(gp_character.score))
                    highscore_list.append(highscore_info)
                    print(highscore_list)
                    for item in highscore_list:
                        item = item + "\n"
                    with open ("G:\\My Drive\\L2 Digital Science 2023\\L2_digital_science_ass\\Highscore.txt", "w", encoding="utf-8") as highscore:
                        # need a way to rank scores
                        for item in highscore_list:
                            highscore.write(item)
                    return highscore_list

                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    input_text.char = text
                else:
                    text += event.unicode
                    input_text.char = text
                

        draw(gameplay_rect_list, gameplay_text_list, gp_char_list, [], [])


def create_enemies(enemy_speed):
    """changes the question when asners are correct or inncorrect"""
    for enemy in gp_enemy_list:
        enemy.value = None

    rand_int_1 = random.randint(1, 12)
    rand_int_2 = random.randint(1, 12)


    rand_correct_answer = random.randint(0, 4)

    duplicate_answer_check = []

    for i in range(5):
        rand_int_1 = random.randint(1, 12)
        rand_int_2 = random.randint(1, 12)
        value = rand_int_1 * rand_int_2
        while True:
            if value not in duplicate_answer_check:
                duplicate_answer_check.append(value)
                break
            else:
                rand_int_1 = random.randint(1, 12)
                rand_int_2 = random.randint(1, 12)
                value = rand_int_1 * rand_int_2

        if rand_correct_answer == i:
            question = str(rand_int_1) + " X " + str(rand_int_2)
            gameplay_question_text.char = "Question: " + str(question)
            gp_character.answer = value

        enemy = Enemy(win_width - 50, (100 + ((win_height-50) /
                        5) * i), 150, 150, RED, value, False, enemy_speed)
        gp_enemy_list.append(enemy)




def gameplay_movement(char_list, enemy_list, keys_pressed, bullet_list):
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
        if enemy.x_cord < 0 - enemy.width:
            return enemy_list.remove(enemy)

    for bullet in bullet_list:
        bullet.x_cord += bullet.speed
        if bullet.x_cord > win_width:
            return bullet_list.remove(bullet)

def collision_decttion(char_list, enemy_list, bullet_list):
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

            # detects if any bullets is hits any enemy
            for bullet in bullet_list:
                if (bullet.x_cord + bullet.width) > enemy.x_cord:
                    if bullet.y_cord > enemy.y_cord \
                        and bullet.y_cord < (enemy.y_cord + enemy.height) \
                        or (bullet.y_cord + bullet.height) > enemy.y_cord \
                        and (bullet.y_cord + bullet.height) < (enemy.y_cord + enemy.height):
                        
                        if enemy.value == gp_character.answer:
                            enemy.x_cord = 0 -enemy.width
                            gameplay_question_text.char = "Correct!"
                        
                        else:
                            pygame.event.post(pygame.event.Event(PLAYER_HIT))
                            enemy.x_cord = 0 - enemy.width
                            gameplay_question_text.char = gameplay_question_text.char + " Incorrect"
                        return enemy_list.remove(enemy), bullet_list.clear()
if __name__ == '__main__':
    # grabbing highscores
    highscore_list = []
    with open("G:\\My Drive\\L2 Digital Science 2023\\L2_digital_science_ass\\Highscore.txt", "r", encoding="utf-8") as highscores:
        highscore_list = highscores.readlines()

        fixing_list = []
        for line in highscore_list:
            fixing_list.append(re.sub('\n', '', line))
        highscore_list = fixing_list
    main_menu_run()
