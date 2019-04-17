from races.humanoid import Humanoid


class Elf(Humanoid):
    def __init__(self, gender, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.race = "elf"
        self.gender = gender
        self.origin_hp = 8
        if self.gender == "male":
            self.call = "he"
            self.genetive = "his"
        else:
            self.call = "she"
            self.genetive = "her"

    def __str__(self):
        self.check_condition()
        return f"""This is an elf {self.gender}
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
