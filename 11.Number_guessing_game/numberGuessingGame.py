import random

def number_guessing_game(user_number, level):

#   Determine number of attemps 
    if (level == 'Hard'):
        attemp = 5
    else:
        attemp = 10

#   Generate random number between 1 and 100
    count = 0
    computer_guess = random.randint(1,100)

#   Determine if user attemp is correct
    game_end = False
    while not game_end:
        if (user_number == computer_guess):
            game_end = True
            count += 1
            print(f"You win in {count} attemp.")
            return True
        elif (user_number < computer_guess):
            count += 1
            attemp -=1
            print(f"Too low")
            print(f"You have {attemp} attemp remain")
        elif (user_number > computer_guess):
            count += 1
            attemp -=1
            print(f"Too high")
            print(f"You have {attemp} attemp remain")
        
        if (attemp == 0):
            print(f"You Lose. You have {attemp} remain")
            print(f"The guessing number is {computer_guess}")
            game_end = True
            return False
        
        user_number = int(input("Guess again: "))
        
