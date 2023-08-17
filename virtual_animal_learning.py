
"""Function to teach virtual animal pet a new trick."""
def teach_trick(virtual_pet):
    if virtual_pet["intelligence"] >= 80:
        print("Your pet already knows all the tricks it can learn!")
    else:
        virtual_pet["intelligence"] += 20
        print("Your pet has learned a new trick!")