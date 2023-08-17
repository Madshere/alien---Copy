
"""Function to check the status of the virtual alien pet."""
def status(virtual_pet):
    print(f"{virtual_pet['name'].title()}'s stats:")
    print(f"Happiness Level: {virtual_pet['happiness']} out of {virtual_pet['max_happiness']} | Hunger Level: {virtual_pet['hunger']} out of {virtual_pet['max_hunger']} | Energy Level: {virtual_pet['energy']} out of {virtual_pet['max_energy']}")