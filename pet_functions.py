class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.happiness = 0.5
        self.potty_counter = 0


    def play(self):
        chance = random.random()
        if chance <= (self.happiness/2):
            self.happiness += 0.1
        else:
            self.happiness -= 0.1
        if self.happiness > 1.0:
            self.happiness = 1.0
        elif self.happiness < 0:
            self.happiness = 0

    def feed(self):
        chance = random.random()
        if chance <= (1 - self.hunger):
            self.hunger -= 0.1
        else:
            self.hunger += 0.1
        if self.hunger > 1.0:
            self.hunger = 1.0
        elif self.hunger < 0:
            self.hunger = 0

    def clean(self):
        if self.potty_counter <= 3:
            self.happiness -= 0.1
            self.potty_counter = 0
        else:
            self.potty_counter = 0
            self.hunger += 0.1
        if self.happiness < 0:
            self.happiness = 0
        elif self.hunger > 1.0:
            self.hunger = 1.0
