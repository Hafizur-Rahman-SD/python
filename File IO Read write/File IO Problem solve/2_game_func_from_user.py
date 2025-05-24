# '''2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi_score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score. '''


import random 

def game():
    print("You are playing the game...")
    score = random.randint(1, 62)

    # Fetch the game hi-score
    try:
        with open("Hi_score.txt", "r") as f:
            Hi_score = f.read()
            if Hi_score != "":
                Hi_score = int(Hi_score)
            else:
                Hi_score = 0
    except FileNotFoundError:
        Hi_score = 0

    print(f"Your Score: {score}")

    if score > Hi_score:
        print("Congratulations! New High Score!")
        with open("Hi_score.txt", "w") as f:
            f.write(str(score))
    else:
        print("Try again to beat the high score.")

    return score

# Call the function to play the game
game()
