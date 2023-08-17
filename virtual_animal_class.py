
"""Class to define virtual alien pets for the mobile app."""
class VirtualPet:
    def __init__(self, species, energy = 50, playfulness = 50, intelligence = 50):
        self.species = species
        self.energy = energy
        self.playfulness = playfulness
        self.intelligence = intelligence

    def rest(self):
        if self.energy >= 80:
            print("Your pet is already well-rested.")
        else:
            self.energy += 20
            print("Your pet is now well-rested.")