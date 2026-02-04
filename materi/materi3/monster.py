from hero import Hero

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, damage):   # ✅ TAMBAHKAN INI
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
