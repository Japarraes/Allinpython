from numberGuessingGame import *

# User have to guess computer generated random number (this number is not visible to user)
# if user guess is correct in given attempt then user win otherwise user lose a game.
# Computer generate one random number using random module (this number is not visible to user or player).
# User have to guess one number.
# if user guess is equal to computer generated random number than user win.
# if user guess is greater than computer generated random number than you have to print message "too High".
# if user guess is less than computer generated random number than you have to print message "too low".
# Create a counter that count number of attempt.

def main():
    
    print("Welcome to number guessing game!")
    level = input("Select dificulty level type 'Hard' o 'Easy': ")

    if (level == 'Hard'):
        print("You have only 5 attemp to guess a number \n")
    else:
        print("You have 10 attemp to guess a number \n")
    
    user_guess = int(input("Guess the number between 1 to 100: "))

    number_guessing_game(user_number = user_guess, level = level)


    
if __name__ == "__main__":
    main()
