# Dice Game

from numpy import random # pattern 3.1
import sys # pattern 4.5
import dice_game_function # function I made for dice rolling and counting, pattern 3.2
import time
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# these comments on patterns are notes for myself on what to include, I put comments next to what I saw as fulfilling each pattern, pattern 8.1, commits are pattern 8.3, README is pattern 8.4

# patterns completed based on wc 2.0 (last graded assignment)
# pattern 1.1, 1.2, 2.1, 2.2, 3.1, 4.1, 4.2, 4.3, 4.4, 5.3, 8.1

# patterns needed to include based on wc 2.0 (last graded assignment)
# pattern 2.3, 2.4, 3.2, 4.5, 5.1, 5.2, 6.1, 6.2, 6.3, 7.1, 7.2, 7.3, 7.4, 8.2, 8.3, 8.4

print(f"Starting {sys.argv[0]} in 3 seconds...") # pattern 4.5
time.sleep(1)
print(f"Starting {sys.argv[0]} in 2 seconds...") # pattern 4.5
time.sleep(1)
print(f"Starting {sys.argv[0]} in 1 second...") # pattern 4.5
time.sleep(1)
print("Welcome to a game called 'Tuple Out!'\n") # printed on different lines to not make it crowded, created a space into each line since I find it easier to read
time.sleep(.5)
print("\nThe goal is simple: get the most amount of points in 10 rounds to beat the high score of 75!\n") 
time.sleep(.5)
print("\nBut be careful! If you roll 3 of the same number, you'll get a score of 0 for that turn!\n")
time.sleep(.5)
print("\nIf you roll 2 of one number, those die are fixed and cannot be re-rolled!\n")
time.sleep(.5)
print("\nYou can roll the non-fixed die as often as you want, but be careful to not get 3 of one! Let's begin!\n")
time.sleep(.5)

#initializing variables, pattern 1.1, 1.2
highscore = (75) # highscore in a tuple so it can be iterated to without needing a list, but immutable so it cannot be changed, pattern 7.4
total_score = 0 #their scores
final_score = [0] #what i am appending to (list so it is iterable), pattern 6.3, 7.1
turns = 10

while turns > 0: # pattern 6.1
    for index in range(turns): # pattern 5.1, 5.2, 2.1
        turns -= 1
        print(f"This process took {time.process_time()} seconds. Efficient!")
        print(f"Turn {turns}")
        time.sleep(.5)
        start_game = input("Would you like to start a new roll? Please respond with yes or no in all lowercase accordingly") # pattern 4.2
        if start_game == "yes":
            time.sleep(1)
            dice_game_function.dice_checker(dice_game_function.dice_roll()) # dice checker function checks to see what numbers are the same, dice roll initializes the dice rolling action
            if (dice_game_function.dice_roll()[0]) == (dice_game_function.dice_roll()[1]) and (dice_game_function.dice_roll()[1]) == (dice_game_function.dice_roll()[2]) and (dice_game_function.dice_roll()[0]) == (dice_game_function.dice_roll()[2]): # if all numbers are the same, score is 0
                print("Your score for this round is 0! You have Tupled Out!")
                total_score += 0
            elif (dice_game_function.dice_roll()[0]) == (dice_game_function.dice_roll()[1]): # gives different outcomes based on the numbers rolled and the amount & if any number repeats, rerolls the dice based on its placemen, pattern 7.2
                (dice_game_function.dice_roll()[2]) = random.randint(1,7) #pattern 7.2
                total_score += (dice_game_function.dice_roll()[0]) + (dice_game_function.dice_roll()[1]) + (dice_game_function.dice_roll()[2]) #pattern 7.2
            elif (dice_game_function.dice_roll()[1]) == (dice_game_function.dice_roll()[2]): #pattern 7.2
                (dice_game_function.dice_roll()[0]) = random.randint(1,7) #pattern 7.2
                total_score += (dice_game_function.dice_roll()[0]) + (dice_game_function.dice_roll()[1]) + (dice_game_function.dice_roll()[2]) #pattern 7.2
            elif (dice_game_function.dice_roll()[0]) == (dice_game_function.dice_roll()[2]): #pattern 7.2
                (dice_game_function.dice_roll()[1]) = random.randint(1,7) #pattern 7.2
                total_score += (dice_game_function.dice_roll()[0]) + (dice_game_function.dice_roll()[1]) + (dice_game_function.dice_roll()[2]) #pattern 7.2
            else:
                total_score += (dice_game_function.dice_roll()[0]) + (dice_game_function.dice_roll()[1]) + (dice_game_function.dice_roll()[2]) #pattern 7.2
            if total_score > 75:
                highscore_dictionary = {"Ultimate highscore" : highscore, "New highscore" : (max(final_score))} # pattern 7.3
                print(highscore_dictionary)
                final_score.append(total_score) # appending the high score into a lsit to keep track
                print(f"Final scores: {final_score}. Congrats! You beat the highscore with a score of {highscore_dictionary["New highscore"]}!") # loops and gives score
                print(f"The difference between your score and the highscore is {highscore_dictionary["New highscore"] - highscore_dictionary["Ultimate highscore"]}") # pattern 7.2
            else: 
                highscore_dictionary = {"Ultimate highscore" : highscore, "New highscore" : (max(final_score))} # pattern 7.3
                print(f"Final scores: {final_score}. Keep going to beat the highscore! Your current highest is {highscore_dictionary["New highscore"]}") # loops and gives score
                print(f"The difference between your score and the highscore is {highscore_dictionary["Ultimate highscore"] - highscore_dictionary["New highscore"]}") # pattern 7.2
                print(highscore_dictionary)
                final_score.append(total_score) # appending the high score into a lsit to keep track
            for value in final_score: # pattern 6.2
                with open("dice_results.csv", mode = "a") as write_connection: # pattern 2.2, 4.1
                    write_connection.write(str(value)) # gave an error saying I was using an integer, so did this as a workaround
                    write_connection.write("\n") # pattern 4.4
        elif start_game == "no":
            time.sleep(1)
            highscore_dictionary = {"Ultimate highscore" : highscore, "New highscore" : (max(final_score))} # pattern 7.3
            print(highscore_dictionary)
            final_score.append(total_score) # appending the high score into a lsit to keep track
            print(f"Final scores: {final_score}. Keep going to beat the highscore! Your current highest is {highscore_dictionary["New highscore"]}") # loops and gives score
            print(f"The difference between your score and the highscore is {highscore_dictionary["Ultimate highscore"] - highscore_dictionary["New highscore"]}") #pattern 7.2
            for value in final_score:
                with open("dice_results.csv", mode = "a") as write_connection: #pattern 2.2, 4.1
                    write_connection.write(str(value)) # gave an error saying I was using an integer, so did this as a workaround
                    write_connection.write("\n") # pattern 4.4
            break
        else:
            raise ValueError ("Must respond with yes/no in all lowercase") # pattern 5.3

repeat_game = True
while repeat_game: #pattern 6.1
    replay = input("Play again! Please respond yes or no in all lowercase. Typing 'yes' will end the loop")
    if replay == "yes":
        print("Please go into the terminal and repeat the process")
        repeat_game = False
    elif replay == "no":
        print("You sure? It's fun! Typing 'yes' will end the loop")
    else:
        print("Please type yes or no in all lowercase as instructed")

print("Now, let's take your scores so you can see them visually in a chart from the terminal, histogram you can save, and a swarmplot you can save from the csv!")
with open("dice_results.csv", "r") as file_connections:
    file_connections.read() # pattern 4.3
dice_df = pd.read_csv('dice_results.csv')
dice_df.columns = ['Scores']
dice_df.sort_index()
dice_data = pd.DataFrame(dice_df, columns=['Scores'])
print(pd.DataFrame(dice_df))
dice_df.plot(kind='hist', bins=10, edgecolor='black', color='#ff5733')
plt.title('Histogram of Scores')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.show() # I looked up different Seaborn plots and chose the one I found most appealing. https://www.geeksforgeeks.org/types-of-seaborn-plots/ and https://www.geeksforgeeks.org/data-visualization-with-python-seaborn/ 
sns.set_theme("paper")
sns.swarmplot(dice_data, color="#f54272")
plt.title('Swarmplot of Scores')
plt.ylabel('Scores')
plt.xlabel('Frequency')
plt.show()