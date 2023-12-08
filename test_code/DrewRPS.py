import random
import sys
def get_player_choice():
    choice = input("Choose Rock, Paper, or Scissors: ")
    return choice

def get_computer_choice():
    choice = ["Rock", "Paper", "Scissors"]
    rand_cho = random.choice(choice)
    print("Computer Chose: ", rand_cho)
    return (rand_cho)

def find_results(player_choice, computer_choice):
    if player_choice == "Rock" and computer_choice == "Paper":
        print("Paper beats Rock, Computer Wins!")
    elif player_choice == "Paper" and computer_choice == "Rock":
        print("Paper beats Rock, Player Wins!")
    elif player_choice == "Scissors" and computer_choice == "Paper":
        print("Scissors beats Paper, Player Wins!")
    elif player_choice == "Paper" and computer_choice == "Scissors":
        print("Scissors beats Paper, Computer Wins!")
    elif player_choice == "Rock" and computer_choice == "Scissors":
        print("Rock beats Scissors, Player Wins!")
    elif player_choice == "Scissors" and computer_choice == "Rock":
        print("Rock beats Scissors, Computer Wins!")

def main():

    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    if player_choice == computer_choice:
        print("Outputs are the same: Good try!")
        sys.exit()
        

    find_results(player_choice, computer_choice)

if __name__ == "__main__":
    main()