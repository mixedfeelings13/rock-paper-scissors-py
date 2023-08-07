import random

user_wins = 0
computer_wins = 0

while True:
    user_choice = input("Type Rock, Paper, or Scissors or Q to quit: ").lower()
    if user_choice == "q":
        break
    
    random_number = random.randint(0, 2)
    
    if random_number == 0:
        computer_choice = "rock"
    elif random_number == 1:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"
        
    print("Computer picked", computer_choice + ".")
    
    if user_choice == computer_choice:
        print("You tied!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
            user_wins += 1
        else:
            print("You lose!")
            computer_wins += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
            user_wins += 1
        else:
            print("You lose!")
            computer_wins += 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
            user_wins += 1
        else:
            print("You lose!")
            computer_wins += 1
    else:
        print("Please enter a valid move!")
        
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("Goodbye!")