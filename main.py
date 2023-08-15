"""An educational game."""
import random
import re
import sys
import pygame

# pylint: disable=no-member, W0123, W0621

# The main window specifications.
pygame.init()
win_height, win_width = 1080, 1920
res = (win_width, win_height)
window = pygame.display.set_mode((res))
pygame.display.set_caption("Stellar Solver")

# Constant Variables.
FPS = 60

# RGB colour values.
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (183, 83, 75)
YELLOW = (255, 255, 0)
BLUE = (93, 135, 194)
GREEN = (0, 255, 0)

# Events added to more fluidly run the program.
PLAYER_HIT = pygame.USEREVENT + 1
ENEMY_HIT = pygame.USEREVENT + 2

# Defining an image to be used in the game.
control_image = pygame.image.load(
    "Controls_Screen.png").convert()

spaceship = pygame.image.load("spaceship_red.PNG").convert()

asteroid = pygame.image.load("asteroid.png").convert()

# Altering these images to fit the games dimensions.
spaceship = pygame.transform.scale(spaceship, (60, 60))
spaceship = pygame.transform.rotate(spaceship, 90)

asteroid = pygame.transform.scale(asteroid, (150, 150))
asteroid = pygame.transform.rotate(asteroid, 180)

class Button:
    """Classes for rectanglualr objects that have a desired function when clicked."""

    def __init__(self, x_cord, y_cord, width, height, colour, button_func):

        self.x_cord = x_cord
        self.y_cord = y_cord
        self.width = width
        self.height = height
        self.colour = colour
        self.func = button_func

    def make_button(self):
        """Makes and returns a rectangle for the button class."""
        button = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        return button


# The Basic Black backround every window is built on.
baseplate = Button(0, 0, win_width, win_height, BLACK, "")

# All the button and rectangles on the main menu.
button_width, button_height = 200, 100
play_button = Button(
    win_width/2 - button_width/2, 200, button_width, button_height, WHITE, "gameplay_main()")

highscore_button = Button(
    win_width/2 - button_width/2, 350,  button_width, button_height, WHITE, "highscore_main()")

help_button = Button(win_width/2 - button_width/2, 500, button_width,
                         button_height, WHITE, "help_main()")

main_menu_ex_cordit_button = Button(
    win_width/2 - button_width/2, 650,  button_width, button_height, WHITE, "sys.exit()")

menu_rect_list = [baseplate, play_button, highscore_button,
                  help_button, main_menu_ex_cordit_button]
# All the button and rectangles in the control window.
control_back_button = Button(0, 0,  200, 50, WHITE, "main_menu_run()")

control_rect_list = [control_back_button] #! DO NOT PUT BASEPLATE IN HERE!!!

# All the button and rectangles in the highscore window.
highscore_back_button = Button(0, 0, 200, 50, WHITE, "main_menu_run()")

highscore_rect_list = [baseplate, highscore_back_button]

# All the button and rectangles in the gameplay window.
gameplay_pause_menu = Button(0, 0,  200, 70, WHITE, "p_true")

gameplay_header_rect = Button(210, 0, win_width - 210, 70, WHITE, "")

gameplay_rect_list = [baseplate, gameplay_pause_menu, gameplay_header_rect]

# All the buttons and rectangles in the pause game menu.
pause_resume_button = Button(
    win_width/2 - 200, 300, button_width, button_height, WHITE, "p_false")

pause_rect_list = [pause_resume_button]

class Character:
    """Character class for the character the user will play as."""

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
        """Creates and returns a rectangle used as the players hitbox."""
        hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        return hitbox


# The character used by the user.
gp_character = Character(200, 100, 50, 50,  YELLOW, 3, 13, 0, 0)

gp_char_list = [gp_character]


class Enemy:
    """Enemy class to create enemies for the player to interact with."""

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
        """Makes and returns a rectangle hitbox used by enemies."""
        enemy_hitbox = pygame.Rect(
            self.x_cord, self.y_cord, self.width, self.height)

        return enemy_hitbox

    def make_enemy_answer(self):
        """Makes the font used on the enemies answer text."""
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
        """Makes and returns a bullets hitbox."""
        bullet_hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        return bullet_hitbox

gp_bullet_list = []

class Text:
    """Makes new text boxes through the Text class."""

    def __init__(self, x_cord, y_cord, font, font_size, colour, char):

        self.x_cord = x_cord
        self.y_cord = y_cord
        self.font = font
        self.font_size = font_size
        self.colour = colour
        self.char = char

    def make_text(self):
        """Creates and returns a font for a text object."""
        text = pygame.font.SysFont(self.font, self.font_size)
        return text


# All the text on the main menu represented as the 'Text' class.
title_text = Text(450, 0, "", 100, WHITE, "Math Devout, Figuring It Out")
play_button_text = Text(win_width/2 - button_width/2 + 10, 230, "ariel", 50, BLACK, "Play Game")
highscore_button_text = Text(
    win_width/2 - button_width/2 + 5, 380, "ariel", 50, BLACK, "Highscores")
help_button_text = Text(win_width/2 - 35, 530,
                            "ariel", 50, BLACK, "Help")
main_menu_exit_text = Text(
    win_width/2 - 35, 680, "ariel", 50, BLACK, "Exit")

menu_text_list = [title_text, play_button_text,
                  highscore_button_text, help_button_text, main_menu_exit_text]
# All the text in the help window represented as the 'Text' class.
help_back_text = Text(0, 0, "ariel", 50, BLACK, "Main Menu")

control_text_list = [help_back_text]

# All the text in the highscore window represented as the 'Text' class.
highscore_back_text = Text(0, 0, "ariel", 50, BLACK, "Main Menu")

highscore_text_list = [highscore_back_text]

# All the text on the main menu represented as the 'Text' class.
gameplay_pause_text = Text(5, 15, "ariel", 50, BLACK, "Pause")
gameplay_lives_text = Text(1700, 0, "ariel", 75, BLACK, "Lives: 3")
gameplay_question_text = Text(400, 0, "ariel", 100, BLACK, "Question: ")
gameplay_score_text = Text(1400, 0, "ariel", 75, BLACK, "Score: 0")

gameplay_text_list = [gameplay_pause_text, gameplay_lives_text,
                       gameplay_question_text, gameplay_score_text]

# All the text on the pause game menu represented as the 'Text' class.
pause_title_text = Text(win_width/2 - 250, 200, "", 100, WHITE, "Game Paused")
pause_resume_text = Text(win_width/2 -200, 300, "ariel", 50, BLACK, "Resume")

pause_text_list = [pause_title_text, pause_resume_text]

def draw(rect_list, text_list, char_list, enemy_list, bullet_list):
    """Draws all items in the inputted lists."""
    # Rendering the buttons themselves.
    for rect in rect_list:
        pygame.draw.rect(window, rect.colour, rect.make_button())

    # Drawing all bullets.
    # This is done before charcters and bullets so they appear under them.
    for bullet in bullet_list:
        pygame.draw.rect(window, bullet.colour, bullet.make_bullet())

    # Displaying all characters.
    for char in char_list:
        window.blit(spaceship, (char.x_cord, char.y_cord))

    # Drawing all enemies.
    for enemy in enemy_list:
        window.blit(asteroid, (enemy.x_cord, enemy.y_cord))
        enemy_text = enemy.make_enemy_answer()
        button_text = enemy_text.render(str(enemy.value), True, WHITE)
        window.blit(button_text, (enemy.x_cord + 20, enemy.y_cord + enemy.height/2 - 30))

    # Rendering all text items.
    for text in text_list:
        button_text = text.make_text().render(
            text.char, True, text.colour)
        window.blit(button_text, (text.x_cord, text.y_cord))

    # Refreshing the pygame window to show the new drawings.
    pygame.display.update()

def main_menu_run():
    """Updates and runs the main menu"""
    # Timer making the game run 60 times each second.
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Allowing the program to stop more cleanly.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Checking for mouse clicks to activate buttons.
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_cord, y_cord = pygame.mouse.get_pos()
                for rect in menu_rect_list:
                    if rect.x_cord + rect.width > x_cord > rect.x_cord and\
                            rect.y_cord + rect.height > y_cord > rect.y_cord:
                        try:
                            eval(rect.func)
                        except SyntaxError:
                            pass

        draw(menu_rect_list, menu_text_list, [], [], [])

def help_main():
    """Helps the user learn the game."""
    draw([baseplate], [], [], [], [])

    window.blit(control_image, (250, 0))
    pygame.display.update()

    # Timer making the game run 60 times each second.
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Allowing the program to stop more cleanly.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Checking for mouse clicks to activate buttons.
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
    """Shows the users the current best scores."""
    highscore_text_list.clear()
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Allowing the program to stop more cleanly.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Checking for mouse clicks to activate buttons.
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_cord, y_cord = pygame.mouse.get_pos()
                for rect in highscore_rect_list:
                    if rect.x_cord + rect.width > x_cord > rect.x_cord and\
                            rect.y_cord + rect.height > y_cord > rect.y_cord:
                        try:
                            eval(rect.func)
                        except SyntaxError:
                            pass
        
        # Generating the text objects for each highscore item.
        font_size = 50
        i = 0
        for item in highscore_list:
            highscore = Text(win_width/2 - 100, i*font_size, "ariel", font_size, WHITE, str(item))
            highscore_text_list.append(highscore)
            i += 1
        highscore_text_list.append(highscore_back_text)
        draw(highscore_rect_list, highscore_text_list, [], [], [])

def gameplay_main():
    """The handling center the gameplay features."""
    # Resetting the gameplay variables when opened each time.
    enemy_speed = 8
    time = ((18.9558 * (0.753947)**enemy_speed + 2.375) - 3) * FPS
    cooldown = 0
    bullet_reload = 0
    gp_character.lives = 3
    gp_character.score = 0
    spawn_enemies = True
    paused = False

    gameplay_rect_list = [baseplate, gameplay_pause_menu, gameplay_header_rect]

    gameplay_text_list = [gameplay_pause_text, gameplay_lives_text,
                        gameplay_question_text, gameplay_score_text]

    gp_enemy_list.clear()

    gameplay_question_text.char = "Question: "
    gameplay_lives_text.char = "Lives: "+ str(gp_character.lives)

    # Timer making the game run 60 times each second.
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        keys_pressed = pygame.key.get_pressed()

        # Allowing the program to stop more cleanly.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # Checking where the mouse has clicked and if a button is present.
            if event.type == pygame.MOUSEBUTTONDOWN and not paused:
                x_cord, y_cord = pygame.mouse.get_pos()
                for rect in gameplay_rect_list:
                    if rect.x_cord + rect.width > x_cord > rect.x_cord and\
                            rect.y_cord + rect.height > y_cord > rect.y_cord:
                        if rect.func == "p_true":
                            paused = True
                        else:
                            try:
                                eval(rect.func)
                            except SyntaxError:
                                pass
            # Making the resume button get detected.
            elif event.type == pygame.MOUSEBUTTONDOWN and paused:
                x_cord, y_cord = pygame.mouse.get_pos()
                for rect in pause_rect_list:
                    if rect.x_cord + rect.width > x_cord > rect.x_cord and\
                            rect.y_cord + rect.height > y_cord > rect.y_cord:
                        if rect.func == "p_false":
                            paused = False
                        else:
                            try:
                                eval(rect.func)
                            except SyntaxError:
                                pass

            # Creating a Bullet when the spacebar is pressed.
            if keys_pressed[pygame.K_SPACE] and bullet_reload <= 0:
                bullet_reload = 0.7 * FPS
                for char in gp_char_list:
                    friend_bullet = Bullets(char.x_cord + char.width - 25, \
                                            char.y_cord + char.height/2, 30, 10, BLUE, 1, 20)
                    gp_bullet_list.append(friend_bullet)

            # Making player lose a life when nessercary.
            if event.type == PLAYER_HIT and cooldown <= 0:
                gp_character.lives = gp_character.lives - 1
                gameplay_lives_text.char = "Lives: " + str(gp_character.lives)
                # Stopping all processes when the player loses.
                if gp_character.lives <= 0:
                    run_highscore_input()
                    highscore_main()

                cooldown = FPS

        # Creates a new set of enemies when the enemies disapear of screen.
        if time >= (18.9558 * (0.753947)**enemy_speed + 2.375) * FPS and spawn_enemies:
            time = 0
            create_enemies(enemy_speed)

        # Running other essential functions for the gameplay to function.
        if paused:
            draw(pause_rect_list, pause_text_list, [], [], [])
        else:
            gameplay_movement(
                gp_char_list, gp_enemy_list, keys_pressed, gp_bullet_list)
            collision_decttion(
                gp_char_list, gp_enemy_list, gp_bullet_list)
            draw(
                gameplay_rect_list, gameplay_text_list, gp_char_list, gp_enemy_list, gp_bullet_list)
            time += 1
            cooldown -= 1
            bullet_reload -= 1


def run_highscore_input():
    """Records the users highscore name."""
    text = ""

    # Creating new nessercary rectangles and text objects to make the input box work.
    loser_text = Text(win_width/2 - 300, win_height/2 - 200, "", 100, WHITE,
                    "You Lost, your score is: " + str(gp_character.score))
    gameplay_text_list.append(loser_text)
    input_help_text = Text(
        win_width/2 - 250, win_height/2 - 125, "", 40, WHITE, "Enter your name here, Name must not be no longer than 10 characters")
    gameplay_text_list.append(input_help_text)
    input_box = Button(win_width/2 - 250, win_height/2 - 75, 500, 150, WHITE, "")
    gameplay_rect_list.append(input_box)
    input_text = Text(win_width/2 - 250, win_height/2 - 75, "ariel", 50, BLACK, text)
    gameplay_text_list.append(input_text)

    # Timer making the game run 60 times each second.
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)

        # Allowing the program to stop more cleanly.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                # Adding the users highscore to the database.
                if event.key == pygame.K_RETURN:
                    # Finding the numerical value of each score.
                    highscore_info = str(input_text.char + " " + str(gp_character.score))
                    highscore_list.append(highscore_info)
                    score_dict = {

                    }
                    for item in highscore_list:
                        score = ""
                        for char in item:
                            if char.isdigit():
                                score = score + char

                        score_dict[item] = int(score)
                    # Sorting the scores from highest to lowest.
                    sorted_score_dict = sorted(score_dict.items(), key=lambda x:x[1], reverse=True)

                    highscore_list.clear()

                    # Adding the players score to the highscore database.
                    for item in sorted_score_dict:
                        highscore_list.append(item[0])

                    # Writing the newly sorted scores to the highscore file.
                    with open ("Highscore.txt", "w", encoding="utf-8") as highscore:
                        # need a way to rank scores - DONE

                        for item in highscore_list:
                            highscore.write(str(item))
                            highscore.write("\n")
                        highscore.flush()
                    gameplay_text_list.remove(input_text)
                    return highscore_list

                # If the users hits backspace it removes the last character.
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    input_text.char = text
                # stopping numbers being inputted
                elif event.key == pygame.K_0 or event.key ==pygame.K_1 \
                    or event.key == pygame.K_2 or event.key == pygame.K_3 \
                    or event.key == pygame.K_4 or event.key == pygame.K_5 \
                    or event.key == pygame.K_6 or event.key == pygame.K_7 or \
                    event.key == pygame.K_8 or event.key == pygame.K_9:
                    pass
                # Every other character is inputted as text.
                else:
                    text += event.unicode
                    input_text.char = text


        draw(gameplay_rect_list, gameplay_text_list, gp_char_list, [], [])


def create_enemies(enemy_speed):
    """Changes the question when asners are correct or incorrect."""
    for enemy in gp_enemy_list:
        enemy.value = None

    # Creating 2 random numbers to make the questions and answers.
    rand_int_1 = random.randint(1, 12)
    rand_int_2 = random.randint(1, 12)


    rand_correct_answer = random.randint(0, 4)

    duplicate_answer_check = []

    # Making the rest of the answers making sure no two answers are the same.
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

        # Making a random answer the question asked to the user.
        if rand_correct_answer == i:
            question = str(rand_int_1) + " X " + str(rand_int_2)
            gameplay_question_text.char = "Question: " + str(question)
            gp_character.answer = value

        enemy = Enemy(win_width - 50, (100 + ((win_height-50) /
                        5) * i), 150, 150, RED, value, False, enemy_speed)
        gp_enemy_list.append(enemy)
    return question


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
                and char.y_cord - char.speed > 70:  # up
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
                            enemy.x_cord = 0 - enemy.width
                            gameplay_question_text.char = "Correct!"
                            gp_character.score += 1
                            gameplay_score_text.char = "Score: " + str(gp_character.score)  

                        else:
                            pygame.event.post(pygame.event.Event(PLAYER_HIT))
                            enemy.x_cord = 0 - enemy.width
                            already_inncorrect = False
                            for char in gameplay_question_text.char:
                                if char == "I":
                                    already_inncorrect = True
                                    break
                                else:
                                    pass
                            
                            if not already_inncorrect:
                                gameplay_question_text.char = gameplay_question_text.char + " Incorrect"
                        return enemy_list.remove(enemy), bullet_list.clear()

if __name__ == "__main__":
    # Grabbing highscore values for the highscore file.
    highscore_list = []
    with open("Highscore.txt", "r", encoding="utf-8") as highscores:
        highscore_list = highscores.readlines()

        fixing_list = []
        for line in highscore_list:
            fixing_list.append(re.sub("\n", "", line))
        highscore_list = fixing_list
        highscores.flush()
    main_menu_run()
