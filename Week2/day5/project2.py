# ============================================
# MINI PROJECT : ROCK PAPER SCISSORS
# ============================================
# What you will learn:
# - OOP (Classes, Methods)
# - Random Number Generation
# - User Input and Validation
# - Loops and Dictionaries
# - Game Logic
# ============================================

import random


# ============================
# PART I - GAME CLASS
# ============================

class Game:
    """A simple Rock-Paper-Scissors game between the user and the computer."""

    def __init__(self):
        self.items = ["rock", "paper", "scissors"]

    def get_user_item(self):
        """Ask the user to choose between rock, paper, or scissors."""
        while True:
            choice = input("Choose rock, paper or scissors: ").lower().strip()
            if choice in self.items:
                return choice
            else:
                print("Invalid choice. Please type rock, paper or scissors.")

    def get_computer_item(self):
        """Randomly choose rock, paper, or scissors for the computer."""
        return random.choice(self.items)

    def get_game_result(self, user_item, computer_item):
        """Determine the game result: win, loss, or draw."""
        if user_item == computer_item:
            return "draw"
        elif (user_item == "rock" and computer_item == "scissors") or \
             (user_item == "scissors" and computer_item == "paper") or \
             (user_item == "paper" and computer_item == "rock"):
            return "win"
        else:
            return "loss"

    def play(self):
        """Play one round of the game."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        print(f"\nYou chose: {user_item}")
        print(f"The computer chose: {computer_item}")

        if result == "win":
            print("🎉 You win!")
        elif result == "loss":
            print("😢 You lose!")
        else:
            print("😐 It's a draw!")

        return result


# ============================
# PART II - MAIN GAME MENU
# ============================

def get_user_menu_choice():
    """Display the menu and get the user's choice."""
    print("\n===== MENU =====")
    print("(1) Play a new game")
    print("(2) Show scores")
    print("(3) Quit")

    while True:
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        if choice in ["1", "2", "3"]:
            return choice
        else:
            print("Invalid input. Please enter 1, 2, or 3.")


def print_results(results):
    """Display the user's final results."""
    print("\n===== GAME RESULTS =====")
    print(f"Wins:   {results['win']}")
    print(f"Losses: {results['loss']}")
    print(f"Draws:  {results['draw']}")
    print("\nThanks for playing! 👋")


def main():
    """Main program loop."""
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        user_choice = get_user_menu_choice()

        if user_choice == "1":
            # Play a new game
            game = Game()
            result = game.play()
            results[result] += 1

        elif user_choice == "2":
            # Show current scores
            print_results(results)

        elif user_choice == "3":
            # Exit the program
            print_results(results)
            break


# ============================
# ENTRY POINT
# ============================

if __name__ == "__main__":
    main()
