import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?:").lower()

    if player == computer:
        print("player:", player)
        print("computer:", computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("player:", player)
            print("computer:", computer)
            print("You Lose!")
        if computer == "scissors":
            print("player:", player)
            print("computer:", computer)
            print("You Win!")
    elif player == "paper":
        if computer == "rock":
            print("player:", player)
            print("computer:", computer)
            print("You Win!")
        if computer == "scissors":
            print("player:", player)
            print("computer:", computer)
            print("You Lose!")
    elif player == "scissors":
        if computer == "rock":
            print("player:", player)
            print("computer:", computer)
            print("You Lose!")
        if computer == "paper":
            print("player:", player)
            print("computer:", computer)
            print("You Win!")

    play_again = input("Play again? (yes/no):").lower()
    if play_again != "yes":
        break
print("Bye!")
