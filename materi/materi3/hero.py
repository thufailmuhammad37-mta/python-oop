# type nint : harus ada ini
from __future__ import annotations
from monster import Monster

class Hero:
    def __init__(self, name: str, hp: int, job: str):
        self.name = name
        self.job = job
        self.__hp = hp
        print(f"✨ Hero {self.name} telah di-summon!")

    # ===== PROPERTY (GETTER & SETTER MODERN) =====
    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    # ===== METHOD =====
    def heal(self):
        print(f"🧪 {self.name} meminum potion...")
        heal_amount = 20
        self.hp += heal_amount
        print(f"💚 HP {self.name} bertambah +{heal_amount}")

    def take_damage(self, damage: int):
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage")

        if self.hp == 0:
            print(f"🚫 {self.name} tereliminasi dari arena!")

    def attack(self, enemy: Monster, damage: int):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")
        enemy.take_damage(damage)

    def ultimate(self, enemy: Monster):
        print(f"🔥 {self.name} mengeluarkan ULTIMATE!")
        enemy.take_damage(50)

    def __str__(self):
        status = "🟢 HIDUP" if self.hp > 0 else "💀 MATI"
        return f"[{self.job}] {self.name} | HP: {self.hp} | {status}"

