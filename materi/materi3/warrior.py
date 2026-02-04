from hero import Hero

class Warrior(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, "Warrior")

    # timpa ultimate skill
    def ultimate(self, enemy):
        dmg = 125
        print(f"{self.name} menggunakan ultimate skill: EXCALIBUR! | {dmg} DMG")
        # monster kena damage
        enemy.take_damage(dmg)   