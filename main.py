from pets import Pet
from settings import Settings
from grounding import Grounding


def main():
    pet_name = input('Please enter a name for your new pet: ')
    pet_appearance = input('Please select an appearance for your new pet:...n        if command == 'grounding':
            technique = input('Please select a grounding technique: ')
            grounding.ground(technique)
        else:
            print('Invalid command. Please try again...')
    

if __name__ == '__main__':
    main()
