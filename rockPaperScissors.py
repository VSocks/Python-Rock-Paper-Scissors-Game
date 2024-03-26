import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper, or scissors?:").lower()

    print("Computer: ",computer)
    print("Player: ",player)

    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif player == "paper":
        if computer == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif player == "scissors":
        if computer == "paper":
            print("You win!")
        else:
            print("You lose!")
            
    play_again = input("Play again? (y/n):").lower()
    if play_again == "n":
        break
print("Bye!")