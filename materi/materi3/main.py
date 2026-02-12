from colorama import Fore, Back, Style, init
from monster import Monster
from mage import Mage
from warrior import Warrior
from archer import Archer
from assasin import Assasin

# auto reset warna (biar gk bocor ke bawah)
init(autoreset=True)
print(Fore.YELLOW + Back.GREEN + "")

aldos = Warrior("Aldos", 100)
nana = Mage("Nana", 100)
hanabi = Archer("Archer", 100)
hanzo = Assasin("Assasin", 100)
dragon = Monster("Dragon King", 1000)

# setter via @property
aldos.hp = 250
nana.hp = 150
# update attr hp
# nana.set_hp(50)
# aldos.set_hp(100)
# ambil attr hp
print(f"HP Nana: {nana.hp}")
print(f"HP Aldos: {aldos.hp}")
# print(aldos)
# print(nana)
# print(dragon)

# nana.heal()
# nana.cast_spell()
# nana.ultimate(dragon)
# aldos.ultimate(dragon)

print("=== ⚔️ RAID PARTY DI MULAI! ⚔️ ===")
# list hero di party
list_party = [aldos, nana, hanabi, hanzo]

running = True 
# loop/ulangi sampai status running jdi false
while running:
    print("=" * 32)
    print(dragon)
    print("=== 🛡️ PILIHAN AKSI: ")
    print("*** 1. ⚔️  ATTACK")
    print("*** 2. 🧪 HEAL")
    print("*** 3. 🔥 ULTIMATE")
    print("*** 4. 🏆 EXIT")
    print("=" * 32)

    while True:
        try:
            aksi = int(input("=== 🏹 AKSI MU : "))
            break
        except ValueError:
            print("❌ Input harus ANGKA! (contoh: 1, 2, 3)")

    if aksi == 1:
        atkDmg = 10
        for party in list_party:
            party.attack(dragon, atkDmg)

        if dragon.hp <= 0:
            running = False
            print("=== 🏆 END GAME, MUSUH KALAH!! ===\n")

    elif aksi == 2:
        nana.heal()

    elif aksi == 3:
        for party in list_party:
            party.ultimate(dragon)

    elif aksi == 4:
        running = False
        print("=== 🏆 END GAME, BYE BYE! ===\n")

    else:
        print("⚠️ Pilihan aksi salah, hanya 1-4!")
