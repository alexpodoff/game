

class Humanoid:

    def __init__(self, name="unknown"):
        self.hands = 4
        self.legs = 4
        self.head = 1
        self.age = None
        self.origin_hp = 10
        self.hp = self.origin_hp
        self.race = None
        self.condition = "healthy"
        self.name = name
        self.nickname = ""
        self.height = None
        self.weight = None

    def check_condition(self):
        if self.hp < self.origin_hp:
            self.condition = "wounded"
        if self.hp <= 0:
            self.condition = "dead"

    def desc(self):
        self.check_condition()
        print(f'This is a {self.race}\n'
              f'his name is {self.name}\n'
              f'his nickname: {self.nickname}\n'
              f'he is {self.condition}')
