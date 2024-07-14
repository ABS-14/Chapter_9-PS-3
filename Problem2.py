# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score

import random

def game(): 
    print("You are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("C:/Users/Admin/OneDrive/Desktop/Computing Programms/Python/Chapter_9/Chapter_9-PS/hiscore.txt") as f:
        hiscore = f.read().strip() # Remove spaces at the beginning and at the end of the string:
        if(hiscore!=""):
             hiscore = max([int(s) for s in hiscore.split('\n')])
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("C:/Users/Admin/OneDrive/Desktop/Computing Programms/Python/Chapter_9/Chapter_9-PS/hiscore.txt", "w") as f:
            f.write(str(score))

    return score
game()

# Explanation :
'''
randint(1,62) = Returns a random number between the given range
This function passes the value in int() 

strip() = The strip() method removes any leading, and trailing whitespaces.
Leading means at the beginning of the string, trailing means at the end.
You can specify which character(s) to remove, if not, any whitespaces will be removed.
'''
# If hiscore is not empty, the following steps are performed:
# hiscore.split('\n')- splits the content of hiscore by newline characters, resulting in a list of strings. Each string represents a high score entry from the file.
# [int(s) for s in hiscore.split('\n')] - is a list comprehension that converts each string in the list to an integer.
# max([int(s) for s in hiscore.split('\n')]) - takes the maximum value from the list of integers. This ensures that if there are multiple high scores in the file, the highest one is selected.
'''
Example
Suppose the hiscore.txt file contains the following lines:
45
60
30
Here's how the code processes it:

f.read().strip() results in the string "45\n60\n30".
hiscore.split('\n') converts this string to the list ["45", "60", "30"].
The list comprehension [int(s) for s in hiscore.split('\n')] converts this list to [45, 60, 30].
max([int(s) for s in hiscore.split('\n')]) finds the maximum value, which is 60.
'''