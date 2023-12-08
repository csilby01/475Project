import random

# Function to get player's choice
def get_player_choice():
    """Get the player's choice for rock, paper, or scissors."""
    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if player_choice in ['rock', 'paper', 'scissors']:
            return player_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

# Function to generate computer's choice
def get_computer_choice():
    """Generate the computer's choice for rock, paper, or scissors."""
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    """Determine the winner based on the choices made by the player and computer."""
    print(f"Player chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "Player wins!"
    else:
        return "Computer wins!"

def main():
    """Main function to play rock-paper-scissors game."""
    print("Let's play Rock-Paper-Scissors!")
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Execute the main function
if __name__ == "__main__":
    main()