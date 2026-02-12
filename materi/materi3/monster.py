# return type data suatu method...
# kasihkan di akhir -> typedataNya
class Monster:
    def __init__(self, name: str, hp: int) -> None:
        self.name = name
        self.hp = hp
        print(f"✨ Monster {self.name} telah di summon!")

    def take_damage(self, damage: int) -> bool:
        self.hp -= damage
        print(f"💥 {self.name} terkena {damage} damage\n")
        if self.hp == 0:
            print(f"🚫 {self.name} tereliminasi dari arena!")

    def __str__(self) -> str:
        status = "🟢 HIDUP" 
        if self.hp == 0:
            status = "💀 MATI" 

        return f"[Monster] {self.name} | HP: {self.hp} | {status}"
