from races.human import Human
from races.elf import Elf


class Construct:

    def __init__(self, race, gender, name):
        self.race = race
        self.gender = gender
        self.name = name

    def player_build(self):
        if self.race == "human":
            player = Human(self.gender)
            player.name = self.name
            return player
        if self.race == "elf":
            player = Elf(self.gender)
            player.name = self.name
            return player
