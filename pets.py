class Pet:

    def __init__(self, name, appearance):
        self.name = name
        self.appearance = appearance
        self.hunger = 0
        self.mood = 'happy'

    def feed(self):
        self.hunger -= 1
        self.update_moo...n    def update_mood(self):
        if self.hunger <= 2:
            self.mood = 'unhappy'
        else:
            self.mood = 'happy'
        print(f'{self.name} is feeling {self.mood}...')

