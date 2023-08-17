
"""Function to talk to the virtual alien pet."""
def talk(virtual_pet):
    response = input("What would you like to say to your pet? ")
    if not response:
        print("Your pet didn't hear anything. Try again later.")
    else:
        print(f"Your pet heard you say '{response}' and seems to understand.")
        virtual_pet["intelligence"] += 10
        print(f"Your pet's intelligence increased by 10. Current intelligence level: {virtual_pet['intelligence']}")