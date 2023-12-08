import random

# Function to get player's choice
def player_choice():
    """Get the player's choice for rock, paper, or scissors."""
    while 1:
        player_choice = input("Enter your choice (rock, paper, or scissors): ")
        players_choice = player_choice.lower()
        choices = ['rock', 'paper', 'scissors']
        if players_choice in choices:
            return players_choice
        print("Invalid choice. Please enter rock, paper, or scissors.")

# Function to generate computer's choice
def computer_choice():
    """Generate the computer's choice for rock, paper, or scissors."""
    choice = random.choice(['rock', 'paper', 'scissors'])
    return choice

# Function to determine the winner
def find_winner(player_choice, computer_choice):
    """Determine the winner based on the choices made by the player and computer."""
    print("Player chooses: " + player_choice)
    print("Computer chooses: " + computer_choice)

    if player_choice == computer_choice:
        return "Tie!"
    elif (player_choice == 'rock') & (computer_choice == 'scissors'):
        return "Player wins!"
    elif (player_choice == 'paper') & (computer_choice == 'rock'):
        return "Player wins!"
    elif (player_choice == 'scissors') & (computer_choice == 'paper'):
        return "Player wins!"
    return "Computer wins!"

def main():
    """Main function to play rock-paper-scissors game."""
    print("Let's play Rock-Paper-Scissors!")
    print(find_winner(player_choice(), computer_choice()))

# Execute the main function
if __name__ == "__main__":
    main()