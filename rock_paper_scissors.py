import random

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    """Decide the winner based on user and computer choices."""
    if user == computer:
        return "It's a tie!"
    
    if (user == "rock" and computer == "scissors") or \
       (user == "scissors" and computer == "paper") or \
       (user == "paper" and computer == "rock"):
        return "You win!"
    
    return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    print("\nWelcome to Rock-Paper-Scissors Game!")
    
    while True:
        user_choice = input("\nChoose Rock, Paper, or Scissors (or type 'exit' to quit): ").strip().lower()
        
        if user_choice == "exit":
            print("\nFinal Score:")
            print(f"You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing! Goodbye!")
            break
        
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    main()
