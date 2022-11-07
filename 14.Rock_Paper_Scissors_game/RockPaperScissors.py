import random

def rockPaperScissorsPlay():

    # Create list with play's elements
    rules = ["rock", "paper", "Scissors"]


    score_player = 0
    score_machine = 0

    end_game = False
    while not end_game:
        
        machine_choice = random.randint(0,2)
        user_choice = int(input("(0)-Rock, (1)-Paper, (2)-Scissors?, (3)-Exit: "))

        if (user_choice == 3):
            end_game = True
            continue

        print(f"Player: {rules[user_choice]} - Machine: {rules[machine_choice]}" )
        
        # Win's options for player
        if ((user_choice == 0) and (machine_choice == 2)) or \
            ((user_choice == 1) and (machine_choice == 0)) or \
            ((user_choice == 2) and (machine_choice == 1)):
            print("You win!")
            score_player += 1
        # Win's options for computer
        elif ((user_choice == 2) and (machine_choice == 0)) or \
            ((user_choice == 0) and (machine_choice == 1)) or \
            ((user_choice == 1) and (machine_choice == 2)):
            print("You lose!")
            score_machine += 1
        else:
            print("Play again.")
    
    print(f"Player Score: {score_player}")
    print(f"Computer Score: {score_machine}")