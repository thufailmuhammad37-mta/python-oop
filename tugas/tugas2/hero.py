class hero:
    def __init__(self, name, job, hp, hero_type="hero"):
        self.name = name
        self.job = job
        self.type = hero_type
        self.max_hp = hp
        self.hp = hp
        self.rage = False

        print(f"✨ {self.name} memasuki arena!")

    def is_alive(self):
        return self.hp > 0

    def serangan(self, musuh, damage):
        if not self.is_alive():
            print(f"💀 {self.name} sudah mati dan tidak bisa menyerang.")
            return

        if damage <= 0:
            print(f"⚠️ damage tidak valid.")
            return

        if self.type == "boss" and self.hp <= self.max_hp / 2 and not self.rage:
            self.rage =  True
            print("😈 raja iblis memasuki MODE MARAH!")

        if self.type == "boss" and self.rage:
            damage *= 2
            print(f"🔥 SERANGAN KRITIS!")

        print(f"⚔️ {self.name} menyerang {musuh.name} sebesar {damage} damage!")
        musuh.take_damage(damage)

    def take_damage(self, damage):
        if damage <= 0:
            return

        self.hp -= damage 

        if self.hp < 0:
            self.hp = 0

        print(f"💥 {self.name} menerima {damage} damage (HP: {self.hp}/{self.max_hp})")          

        if self.hp == 0:
            print(f"💀 {self.name} telah gugur!")

    def heal(self):
        if not self.is_alive():
            print(f"💀 {self.name} sudah mati dan tidak bisa menyembuhkan.")
            return

        if self.job == "Prajurit":
            heal_amount = 15
        elif self.job == "Penyihir":
            heal_amount = 20
        elif self.job == "Penyembuh":
            heal_amount = 40
        else:
            heal_amount = 10

        self.hp += heal_amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(f"💚 {self.name} memulihkan {heal_amount} HP (HP: {self.hp}/{self.max_hp})")

prajurit = hero("Zilong", "Prajurit", 140)
penyihir = hero("Eudora", "Penyihir", 90)
healer = hero("Estes", "Penyembuh", 100)

goblin = hero("Goblin", "Monster", 60, "normal")
boss = hero("Raja Iblis", "Bos", 200, "boss")

print("\n===== PERTARUNGAN MELAWAN GOBLIN =====")
prajurit.serangan(goblin, 30)
penyihir.serangan(goblin, 40)
goblin.serangan(prajurit, 20)
prajurit.serangan(goblin, 50)

print("\n===== GOBLIN DIKALAHKAN =====")

print("\n===== PERTARUNGAN MELAWAN RAJA IBLIS =====")
prajurit.serangan(boss, 40)
penyihir.serangan(boss, 60)

boss.serangan(penyihir, 80)
boss.serangan(penyihir, 80)

healer.heal()
prajurit.serangan(boss, 50)

boss.serangan(prajurit, 70)
boss.serangan(prajurit, 70)

print("\n===== PERTEMPURAN BERLANJUT =====")
penyihir.serangan(boss, 60)                    