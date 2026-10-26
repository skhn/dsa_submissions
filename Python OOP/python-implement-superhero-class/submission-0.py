class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health
        pass


# TODO: Create Superhero instances
bman = SuperHero("Batman", "Intelligence", 100)
sman = SuperHero("Superman", "Strength", 150)


# TODO: Print out the attributes of each superhero
print(bman.name)
print(bman.power)
print(bman.health)
print(sman.name)
print(sman.power)
print(sman.health)
