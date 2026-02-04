from hero import Hero

class Assasin(Hero):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self, enemy, damage):   # ✅ TAMBAHKAN INI
        enemy.take_damage(damage)
        print(f"{self.name} menyerang {enemy.name} sebesar {damage} damage")

