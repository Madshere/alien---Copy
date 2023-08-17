
"""Function to feed the virtual animal pet."""
def feed(virtual_pet):
    if virtual_pet["hunger"] >= 80:
        print("Your pet is already full!")
    else:
        virtual_pet["hunger"] += 30
        print("Your pet has been fed!")
"""Function to feed the virtual alien pet."""
def feed(virtual_pet):
    if virtual_pet["energy"] >= 80:
        print("Your pet is not hungry at this time.")
    else:
        virtual_pet["energy"] += 20
        print(f"Your pet has been fed and gained 20 energy points. Current energy level: {virtual_pet['energy']}")
"""Function to feed the virtual alien pet."""
def feed(virtual_pet):
    if virtual_pet["hunger"] <= 20:
        print("Your pet is too full to eat right now.")
    else:
        virtual_pet["hunger"] -= 20
        print(f"Your pet ate and its hunger decreased by 20 points. Current hunger level: {virtual_pet['hunger']}")
"""Function to feed the virtual alien pet."""
def feed(virtual_pet):
    if virtual_pet['hunger'] >= virtual_pet['max_hunger']:
        print(f"{virtual_pet['name'].title()} is not hungry!")
    else:
        print(f"You feed {virtual_pet['name'].title()}. Yum!")
        virtual_pet['hunger'] += 1
        if virtual_pet['hunger'] > virtual_pet['max_hunger']:
            virtual_pet['hunger'] = virtual_pet['max_hunger']
        virtual_pet['happiness'] += 1
        if virtual_pet['happiness'] > virtual_pet['max_happiness']:
            virtual_pet['happiness'] = virtual_pet['max_happiness']
        virtual_pet['energy'] -= 1
        if virtual_pet['energy'] < 0:
            virtual_pet['energy'] = 0