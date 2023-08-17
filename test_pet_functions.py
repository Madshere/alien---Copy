import unittest
from pet_functions import *

class TestPetFunctions(unittest.TestCase):
    
    def setUp(self):
        self.pet = Pet('Test Pet')
        self.pet2 = Pet('Test Pet 2')
        self.pet3 = Pet('Test Pet 3')

    def test_pet_name(self):
        self.assertEqual(str(self.pet), 'Test Pet')
        self.assertEqual(str(self.pet2), 'Test Pet 2')
        self.assertEqual(str(self.pet3), 'Test Pet 3')

    def test_pet_play(self):
        for i in range(20):
            self.pet.play()
        self.assertEqual(self.pet.happiness, 1.0)
        self.pet.play()
        self.assertLessEqual(self.pet.happiness, 1.0)

    def test_pet_feed(self):
        for i in range(20):
            self.pet.feed()
        self.assertEqual(self.pet.hunger, 0.0)
        self.pet.feed()
        self.assertGreater(self.pet.hunger, 0.0)

    def test_pet_clean(self):
        for i in range(20):
            self.pet.potty_counter += 1
        self.pet.clean()
        self.assertEqual(self.pet.potty_counter, 0)
        self.pet.clean()
        self.assertEqual(self.pet.happiness, 1.0)
        self.assertEqual(self.pet.hunger, 0.0)

if __name__ == '__main__':
    unittest.main()
