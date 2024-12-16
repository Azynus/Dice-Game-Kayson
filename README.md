# Dice Game README

## Introduction & Functions of the Game
Welcome to the Dice Game! This program is designed to go through 10 rounds (labeled 9 to 0) with a goal of beating a predetermined highscore of 75. The specific rules of the game are listed below. 

Additionally, after the game is over, you will be prompted to respond if you'd like to continue the game, with the "desirable" outcome being yes (because who doesn't love this game?). After responding yes to replay, you will be given a dataframe and histogram (in a new window) of the previous games results. **As long as you do not make edits to the .csv file made for the game, your new game history will be added onto the old one.** If you would not like to save your history, simply delete the .csv file when it is created. 

To use the program "Dice_Game.py" you need to have a terminal and find the folder you downloaded it in, then type "python Dice_Game.py" to run it. The program has time increments in it to ensure that gameplay does not go by too fast and is enjoyable. Interact with the inputs as necessary, most will be simple yes/no answers to them. Make sure to also download the file titles "dice_game_functions.py" to get the original dice game program to work. These functions are crucial to the dice playing!

If you indicate that you do not want to re-roll when prompted, the game will still continue and you'll have to answer 'no' to the prompt to roll or not until all rounds have been completed. Your highscore will be kept the same for all rounds and will be reflected as such in your dataframe, swarmplot, & histogram that is made at the end. You cannot opt out of the data visualizations as it is part of the game's core component to give you data on your games for your satisfaction. 

## Rules of the Game
- 3 dice of the same number (ex: 3,3,3) = a score of 0 for that turn. You will not be able to re-roll the dice if this outcome happens, and you will automatically be moved to the next turn. 
- 2 dice are the same (ex: 3,3,6) = add up all the scores, but those 2 dice that are the same number cannot be rerolled, only the "odd-man-out" can be re-rolled. In the example above, you would only be able to re-roll 6. 
    - Additionally, to prevent someone's turn from lasting too long, **you can only re-roll the dice once.** If you choose to re-roll the 6, you would be stuck with the number you re-rolled and move onto the next turn. 
- No dice are the same (ex: 1,2,3) = you may re-roll all of the dice, and you are limited to this action **once,** similarly with the 2-pair outcome. You cannot choose to re-roll, for example, just 1 and 3, you have to re-roll all of 1,2, and 3. 