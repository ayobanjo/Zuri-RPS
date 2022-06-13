
import random

print('Welcome to a game of Rock Paper Scissors')
    
validate = True

while validate:
    playerChoice = input('Select your move "R" "P" or "S": ').strip().lower()

    if playerChoice == "r":
        playerChoice = "Rock"
    elif playerChoice == "s":
        playerChoice = "Scissors"
    elif playerChoice == "p":
        playerChoice = "Paper"
    else:
        print('Invalid move selected, try again')
        continue
    
    options = ['Rock', 'Paper', 'Scissors']
    computerChoice   = random.choice(options)

    print(f'`Player ({playerChoice}) : CPU ({computerChoice})`')
 

    if playerChoice == computerChoice:
        print("Same move, It's a tie!")
    elif playerChoice == "Rock":
        if computerChoice == "Scissors":
            print("Rock crushes Scissors! You win")
        else:
            print("Paper covers Rock! You lose!")
    elif playerChoice == "Scissors":
        if computerChoice == "Paper":
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock crushes Scissors! You lose!")
    elif playerChoice == "Paper":
        if computerChoice == "Rock":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose!")

    play_again = input("Would you like to play another round? (Y/N): ")
    if play_again.lower() == "y":
        pass

    elif play_again.lower() == "n":
        validate = False
    
    else: 
        validate = False
    

    