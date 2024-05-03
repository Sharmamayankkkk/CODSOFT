import random

def collectUsersChoice():
    while True:
        usersChoice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if usersChoice in ['rock', 'paper', 'scissors']:
            return usersChoice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def collectComputersChoice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(usersChoice, computersChoice):
    if usersChoice == computersChoice:
        return "It's a tie!"
    elif (usersChoice == 'rock' and computersChoice == 'scissors') or \
         (usersChoice == 'scissors' and computersChoice == 'paper') or \
         (usersChoice == 'paper' and computersChoice == 'rock'):
        return "Hurray! You Won!"
    else:
        return "Oops! Computer Won!"

def main():
    user_score = 0
    computer_score = 0
    while True:
        usersChoice = collectUsersChoice()
        computersChoice = collectComputersChoice()
        
        print("Your choice:", usersChoice)
        print("Computer's choice:", computersChoice)
        
        result = determine_winner(usersChoice, computersChoice)
        print(result)
        
        if result == "Hurray! You Won!":
            user_score += 1
        elif result == "Oops! Computer Won!":
            computer_score += 1
        
        print("Score - You:", user_score, "Computer:", computer_score)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("See you soon!")
            break

if __name__ == "__main__":
    main()
