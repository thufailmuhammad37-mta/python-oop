class Hero:
    # pertama kali dipanggil (summon)
    # self = dirinya sendiri / internal
    def __init__(self, name, hp, job):
        self.name = name
        self.job = job
        # multi-select = ctrl+d (ganti jdi__hp)
        self.__hp = hp # __namaAttr = private
        print(f"✨ Hero {self.name} telah di summon!")
    
    # getter (ambil attr private)
    # pola penulisan: get_namaAttr
    def get_hp(self):
        return self.__hp

    # setter (ubah attr private)
    # pola penulisan: set_namaAttr
    def set_hp(self, addHp):
        self.__hp += addHp

    def heal(self):
        print(f"🧪 {self.name} meminum potion...")
        heal_amount = 20
        self.__hp += heal_amount
        print(f"💚 HP {self.name} bertambah +{heal_amount}")

    def take_damage(self, damage):
        # self.__hp = self.__hp - damage (aslinya)
        self.__hp -= damage
        print(f"💥 {self.name} terkena {damage} damage\n")
        # print(f"💚 Sisa HP: {self.__hp}")
        if self.__hp == 0:
            print(f"🚫 {self.name} tereliminasi dari arena!")
    
    def attack(self, enemy, damage):
        print(f"⚔️ {self.name} menyerang {enemy.name}!")
        # panggil method lain dari dalam
        enemy.take_damage(damage)

    # fungsi cek status terkini 
    def __str__(self):
        status = "🟢 HIDUP" 
        if self.__hp == 0:
            status = "💀 MATI" 

        return f"[{self.job}] {self.name} | HP: {self.__hp} | {status}"
    
    # ultimate attack
    def ultimate(self, enemy):
        print(f"{self.name} bengong...")
