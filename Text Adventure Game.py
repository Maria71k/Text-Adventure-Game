import time

# Function to simulate typing effect
def print_with_typing_effect(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Function to handle the player's input and make decisions
def play_game():
    print_with_typing_effect("Welcome to the Text Adventure Game!")
    print_with_typing_effect("You find yourself in a dark room.")
    print_with_typing_effect("There are two doors in front of you: one on the left and one on the right.")

    while True:
        choice = input("Which door do you choose? (left/right): ").lower()

        if choice == 'left':
            print_with_typing_effect("You open the left door and find a treasure chest!")
            print_with_typing_effect("Congratulations! You win!")
            break
        elif choice == 'right':
            print_with_typing_effect("You open the right door and fall into a pit!")
            print_with_typing_effect("Game over. Better luck next time!")
            break
        else:
            print_with_typing_effect("Please choose either 'left' or 'right'.")

# Main function to start the game
def main():
    play_game()

if __name__ == "__main__":
    main()
