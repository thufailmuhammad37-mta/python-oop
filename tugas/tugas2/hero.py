class hero:
    def __init__(self, name, job, hp, hero_type="hero"):
        # constructor → dipanggil saat objek dibuat

        self.name = name          # nama karakter
        self.job = job            # role / pekerjaan (Prajurit, Penyihir, dll)
        self.type = hero_type     # tipe karakter (hero, normal, boss)
        self.max_hp = hp          # HP maksimal
        self.hp = hp              # HP saat ini
        self.rage = False         # status marah (khusus boss)

        print(f"✨ {self.name} memasuki arena!")  # efek masuk arena

    def is_alive(self):
        # ngecek apakah karakter masih hidup
        return self.hp > 0        # True kalau HP > 0

    def serangan(self, musuh, damage):
        # fungsi buat menyerang musuh

        if not self.is_alive():
            # kalau udah mati, gak bisa nyerang
            print(f"💀 {self.name} sudah mati dan tidak bisa menyerang.")
            return

        if damage <= 0:
            # validasi damage biar gak aneh
            print(f"⚠️ damage tidak valid.")
            return

        # cek kondisi boss buat masuk mode marah
        if self.type == "boss" and self.hp <= self.max_hp / 2 and not self.rage:
            self.rage = True
            print("😈 raja iblis memasuki MODE MARAH!")

        # kalau boss lagi rage, damage jadi 2x
        if self.type == "boss" and self.rage:
            damage *= 2
            print(f"🔥 SERANGAN KRITIS!")

        # tampilin info serangan
        print(f"⚔️ {self.name} menyerang {musuh.name} sebesar {damage} damage!")

        # panggil fungsi take_damage milik musuh
        musuh.take_damage(damage)

    def take_damage(self, damage):
        # fungsi saat karakter menerima damage

        if damage <= 0:
            # kalau damage tidak valid, langsung skip
            return

        self.hp -= damage          # kurangi HP

        if self.hp < 0:
            self.hp = 0            # HP gak boleh minus

        # tampilkan sisa HP
        print(f"💥 {self.name} menerima {damage} damage (HP: {self.hp}/{self.max_hp})")

        if self.hp == 0:
            # kalau HP habis, karakter mati
            print(f"💀 {self.name} telah gugur!")

    def heal(self):
        # fungsi buat menyembuhkan HP

        if not self.is_alive():
            # karakter mati gak bisa heal
            print(f"💀 {self.name} sudah mati dan tidak bisa menyembuhkan.")
            return

        # jumlah heal tergantung job
        if self.job == "Prajurit":
            heal_amount = 15
        elif self.job == "Penyihir":
            heal_amount = 20
        elif self.job == "Penyembuh":
            heal_amount = 40
        else:
            heal_amount = 10       # default heal

        self.hp += heal_amount     # tambahin HP

        if self.hp > self.max_hp:
            self.hp = self.max_hp  # HP gak boleh lebih dari max

        # tampilkan hasil heal
        print(f"💚 {self.name} memulihkan {heal_amount} HP (HP: {self.hp}/{self.max_hp})")


# ===== PEMBUATAN KARAKTER =====
prajurit = hero("Zilong", "Prajurit", 140)
penyihir = hero("Eudora", "Penyihir", 90)
healer = hero("Estes", "Penyembuh", 100)

goblin = hero("Goblin", "Monster", 60, "normal")
boss = hero("Raja Iblis", "Bos", 200, "boss")

# ===== LAWAN GOBLIN =====
print("\n===== PERTARUNGAN MELAWAN GOBLIN =====")
prajurit.serangan(goblin, 30)
penyihir.serangan(goblin, 40)
goblin.serangan(prajurit, 20)
prajurit.serangan(goblin, 50)

print("\n===== GOBLIN DIKALAHKAN =====")

# ===== LAWAN BOSS =====
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
