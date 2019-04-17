from races.humanoid import Humanoid


class Human(Humanoid):
    def __init__(self, gender):
        super().__init__(self)
        self.race = "human"
        self.gender = gender
        if self.gender == "male":
            self.call = "he"
            self.genetive = "his"
        else:
            self.call = "she"
            self.genetive = "her"

    def __str__(self):
        self.check_condition()
        return f"""This is a human {self.gender}
{self.genetive} name is {self.name}
{self.call} is {self.condition}
"""


"""
a = Human("male", 55)
a.hp = 0
a.name = "Ser Knight"
#a.desc()
print(a)
"""
