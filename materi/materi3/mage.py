from hero import Hero

class Mage(Hero):
    def __init__(self, name, hp):
        super().__init__(name, hp, "Mage")

    def cast_spell(self):
        print(f"🔥 {self.name} melempar sihir api!")

    # timpa ultimate skill
    def ultimate(self, enemy):
        dmg = 100
        print(f"{self.name} menggunakan ultimate skill: ATOMIC BOMB! | {dmg} DMG")
        # monster kena damage
        enemy.take_damage(dmg)   