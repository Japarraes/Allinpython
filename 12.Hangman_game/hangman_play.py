from hangmanStages import *

def hangmanPlay():

    # Get play's stages
    stages = getStages()

    # Generate random word
    random_choice = getRandomChoice()

    # Print len(random word) blanks
    blank = ["_" for i in range(len(random_choice))]
    print(" ".join(blank))

    end_game = False
    lives = 6
    stages = stages[::-1]

    while not end_game:

        user_choice = input("\nEnter your choice: ")

        # Check if user's option the letter before
        if (user_choice in blank):
            print(f"\nYou already guessed {user_choice}")
        
        # Check if user's option is in random word
        for i in range(len(random_choice)):
            if (user_choice == random_choice[i]):
                blank[i] = user_choice
        
        print(f"\n{''.join(blank)}\n")

        # If user's letter is not in random word, substract 1 live
        if (user_choice not in random_choice):
            lives -= 1
            if (lives == 0):
                print(f"You lose. The word is {random_choice}")
                end_game = True
        
        print(stages[lives])

        if "_" not in blank:
            end_game = True
            print("You win!")