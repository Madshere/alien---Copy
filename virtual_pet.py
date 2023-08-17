class VirtualPet:
    
    def __init__(self, name, hunger=0, mood=0):
        self.name = name
        self.hunger = hunger
        self.mood = mood
        
    def feed(self):
        # decrease the virtual pet's hunger attribute
        self.hunger -= 1


pet_name = input("Enter a name for your virtual pet: ")
my_pet = VirtualPet(pet_name)




class AlienPet(VirtualPet):
    def __init__(self, name, img=None, sound=None, attributes=None):
        super().__init__(name)
        if img and sound and attributes:
            self._img = img
            self._sound = sound
            self._attributes = attributes
        else:
            raise ValueError('Invalid AlienPet attributes')

    def interact(self):
        pass

    def feed(self):
        super().feed()
        self.mood += 5

    def play(self):
        super().play()
        self.mood += 10

    def care(self):
        self.cleanliness = 100

    def get_img(self):
        return self._img

    def get_sound(self):
        return self._sound

    def get_attributes(self):
        return self._attributes
