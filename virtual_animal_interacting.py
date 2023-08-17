
"""Function to interact with the virtual alien pet through touch and voice commands."""
def interact(virtual_pet):
    print(f"Your pet's name is {virtual_pet['name']}! Say hi to your pet or use the touch screen to interact.")
    while True:
        action = input("> ")
        if action.lower() == "feed":
            feed(virtual_pet)
        elif action.lower() == "play":
            play(virtual_pet)
        elif action.lower() == "status":
            status(virtual_pet)
        elif action.lower() == "help":
            help_info()
        elif action.lower() == "quit":
            print("Goodbye!")
            break
        elif re.search(r'(?i)^change name to(?P<NewName>.*)', action):
            new_pet_name = re.search(r'(?i)^change name to(?P<NewName>.*)', action).groups(0)[0].strip()
            change_pet_name(virtual_pet, new_pet_name)
        else:
            print("Invalid command. Type 'help' for a list of valid commands.")