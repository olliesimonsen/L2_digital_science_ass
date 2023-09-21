# How to run my program:
- Download the game folder titled L2_digital_science_ass and open this folder in visual studios. Before running the program make sure the below requirements are met. If all is correct, on the main.py python file, hit run (ctrl + f5). 

## requirements
- The program relies on the pygame library so for the program to run the pygame library must be installed locally (on the computer the game is being played on). 
Additionally, the folder in which the game is run from should have a python file named “main.py” a text file named “Highscore.txt” and three png files named “asteroid.png”, “spaceship_red.png” and “updated_controls_screen.png”. Otherwize the program will not run. 

# Basics of the program exculding the gameplay
- When the program is run the main menu screen will be opened where there are four buttons for the user to click: play game, highscores, help and exit.

- ‘play game’ starts the game (instructions for the game are below), 'highscores' open a window where all recorded highscores, 'help' opens an image which helps teach the user the game as well as the controls and 'exit' exits the program not before confirming if the user really wanted to exit the program. 


# How to play the game:
- You play as the spaceship in the game. You can move your spaceship up(W), left(A), down(S) and right(D) by pressing W, A, S and D keys. You can shoot a bullet from your spaceship by pressing the spacebar - shooting a bullet has a cooldown and the bullet travels in a straight line, be careful. 

- The aim of the game is to answer as many questions correctly before you run out of lives. At the top of the screen you will see a question area which starts blank. When the game starts the question will change to a times table question between 1 and 12 (for example 5x7). With each question 5 enemies spawn where each one has a possible answer to the question (for the question 5x7 they could be 12, 42, 56, 9, 35). You need to move your spaceship and shoot the enemy with the corresponding correct answer (in the example question it would be 35).

- Another item at the top of the screen is your score starting at 0. When the correct enemy is shot it will give you +1 score then remove that enemy.
Another item at the top of the screen is the characters lives which starts at 3. your lives cannot be increased. Lives can be decreased in two ways. First, if you shoot an enemy that has the incorrect answer (from the example case of 7x5 enemies of 12, 42, 56 or 9) your ‘lives’ count will be reduced by 1 - the enemy will still be removed from the game. Second, if you contact any enemy your ‘lives’ count will be reduced by 1 and the enemy will be removed from the game. Most importantly if your ‘lives’ count hits zero you lose the game and it ends.

- The last item on the top of the screen is the pause button. This can be pressed at any time to stop the gameplay until the new resume button is pressed. This can be indefinitely and for as long as you want.

- When you run out of lives the highscore name input will appear. Here you should type a name or nickname then press the enter/return key to enter this name. Then your score and name will be added to the highscore list for you and others to view.
