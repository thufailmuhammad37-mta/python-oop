from hero import Hero

class Archer(Hero):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, target, dmg):
        target.hp -= dmg
        print(f"{self.name} menyerang {target.name} sebesar {dmg} damage")
