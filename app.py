from breathing import Breathing
from grounding import Grounding
from pets import Pet, PetBehavior


class CalmingPetsApp:

  def __init__(self):
        self.pets = []
        self.breathing = Breathing()
        self.grounding = Grounding()

  def create_pet(self, name, appearance, personality):
    new_pet = Pet(name, appearance, personality)
    behavior = PetBehavior().get_behavior()
    print(f'Created {new_pet.name} with appearance {new_pet.appearance} and personality {new_pet.personality}.')
    print(f'{new_pet.name} is currently {behavior}.')
    self.pets.append(new_pet)

  def customize_breathing(self, duration, rhythm):
    self.breathing.breathe(duration, rhythm)


  def customize_grounding(self, technique):
    self.grounding.ground(technique)

  def interact_with_pet(self, pet_name, command):
        for p in self.pets:
            if p.name == pet_name:
                p.interact(command)

  def run(self):
    print('--- Calming Pets ---')
    print('The following pets are available: ')
    for pet in self.pets:
        print(f'- {pet.name}')
    print('What would you like to do?')
