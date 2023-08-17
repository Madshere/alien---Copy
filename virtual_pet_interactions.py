
"""Function to allow users to interact with their adopted virtual pet."""
def interact_with_pet(virtual_pet):
    while True:
        print(f"What would you like to do with {virtual_pet['name'].title()}?\n")
        print("[1] Feed your virtual pet")
        print("[2] Play with your virtual pet")
        print("[3] Check your virtual pet's status")
        print("[4] Take your virtual pet to the virtual 3D breathing and grounding")
        print("[5] Quit")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            feed(virtual_pet)
        elif choice == "2":
            play(virtual_pet)
        elif choice == "3":
            check_status(virtual_pet)
        elif choice == "4":
            virtual_3D_breathing()
        elif choice == "5":
            break
        else:
            print("Invalid input. Please enter a number from 1 to 5.")
        print()
"""Function to allow users to check their virtual pet's status."""
def check_status(virtual_pet):
    print(f"{virtual_pet['name'].title()}'s current status:\n")
    print(f"Hunger: {virtual_pet['hunger']}")
    print(f"Happiness: {virtual_pet['happiness']}\n")
"""Function to allow users to play games with their virtual pet."""
def play(virtual_pet):
    print(f"What game would you like to play with {virtual_pet['name'].title()}?\n")
    print("[1] Guessing Game")
    print("[2] Rock-Paper-Scissors")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        guessing_game(virtual_pet)
    elif choice == "2":
        rock_paper_scissors(virtual_pet)
    else:
        print("Invalid input. Please enter a number from 1 to 2.")
    print(f"{virtual_pet['name'].title()}'s happiness increased!\n")
    virtual_pet['happiness'] += 10