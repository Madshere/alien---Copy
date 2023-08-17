
"""Function to interact with and play with the virtual animal pet."""
def play(virtual_pet):
    if virtual_pet["playfulness"] >= 80:
        print("Your pet is already very playful!")
    else:
        virtual_pet["playfulness"] += 20
        print("Your pet is more playful now!")
"""Function to play with the virtual alien pet."""
def play(virtual_pet):
    if virtual_pet["playfulness"] >= 80:
        print("Your pet is not in the mood to play right now.")
    else:
        virtual_pet["playfulness"] += 20
        print(f"Your pet had fun playing and gained 20 playfulness points. Current playfulness level: {virtual_pet['playfulness']}")
"""Function to play with the virtual alien pet."""
def play(virtual_pet):
    action = input("What game would you like to play with your pet? ")
    if not action:
        print("Your pet didn't hear anything. Try again later.")
    else:
        if action in virtual_pet["likes"]:
            print(f"Your pet loves {action}!")
            virtual_pet["happiness"] += 20
            virtual_pet["hunger"] -= 10
            print(f"Playing {action} made your pet happy! Happiness level: {virtual_pet['happiness']}, hunger level: {virtual_pet['hunger']}\n")
        elif action in virtual_pet["dislikes"]:
            print(f"Your pet hates {action}.")
            virtual_pet["happiness"] -= 10
            virtual_pet["hunger"] -= 10
            print(f"Playing {action} made your pet unhappy. Happiness level: {virtual_pet['happiness']}, hunger level: {virtual_pet['hunger']}\n")
        else:
            print(f"Your pet has no interest in {action}.")
            virtual_pet["hunger"] -= 10
            print(f"Playing {action} had no effect on your pet's happiness. Hunger level: {virtual_pet['hunger']}\n")
"""Function to play with the virtual alien pet."""
def play(virtual_pet):
    print(f"You play a game of fetch with {virtual_pet['name'].title()}.")
    virtual_pet['happiness'] += 2
    if virtual_pet['happiness'] > virtual_pet['max_happiness']:
        virtual_pet['happiness'] = virtual_pet['max_happiness']
    virtual_pet['energy'] -= 2
    if virtual_pet['energy'] < 0:
        virtual_pet['energy'] = 0