
"""Guessing game function."""
def guessing_game(virtual_pet):
    print("Welcome to the guessing game!")
    print("The goal of the game is to guess a number between 1 and 10.")
    guesses_left = 3
    number_to_guess = random.randint(1, 10)
    while guesses_left > 0:
        print(f"You have {guesses_left} guesses left.")
        guess = input("Make a guess: ")
        if guess.isdigit() and int(guess) >= 1 and int(guess) <= 10:
            guess = int(guess)
            if guess == number_to_guess:
                print("Congratulations! You guessed correctly.")
                virtual_pet['happiness'] += 10
                break
            elif guess < number_to_guess:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")
        else:
            print("Invalid input. Please enter a number from 1 to 10.")
        guesses_left -= 1
    if guesses_left == 0:
        print(f"Sorry, you ran out of guesses. The number was {number_to_guess}.")
    print()
"""Rock-paper-scissors game function."""
def rock_paper_scissors(virtual_pet):
    print("Welcome to the rock-paper-scissors game!")
    print("You will be playing against your virtual pet. Each win or tie will increase your pet's happiness by 5.")
    print("Choose rock, paper, or scissors:")
    while True:
        player_choice = input("Enter your choice: ").lower()
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input. Please enter rock, paper, or scissors.")
            continue
        pet_choices = ["rock", "paper", "scissors"]
        pet_choice = random.choice(pet_choices)
        print(f"Your pet chose {pet_choice}.")
        if player_choice == pet_choice:
            print("It's a tie!")
            virtual_pet['happiness'] += 5
            break
        elif player_choice == "rock":
            if pet_choice == "scissors":
                print("You win!")
                virtual_pet['happiness'] += 5
                break
            else:
                print("Your pet wins!")
                break
        elif player_choice == "paper":
            if pet_choice == "rock":
                print("You win!")
                virtual_pet['happiness'] += 5
                break
            else:
                print("Your pet wins!")
                break
        elif player_choice == "scissors":
            if pet_choice == "paper":
                print("You win!")
                virtual_pet['happiness'] += 5
                break
            else:
                print("Your pet wins!")
                break
        else:
            print("Invalid input. Please enter rock, paper, or scissors.")
    print()