from admin import menu_admin
from santri import menu_santri

def main():
    daftar_buku = []

    while True:
        print("\n===== SISTEM PERPUSTAKAAN KITAB SANTRI =====")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Santri")
        print("3. Keluar")

        try:
            pilihan = int(input("Pilih Menu: "))
        except ValueError:
            print("Input harus angka.")
            continue

        if pilihan == 1:
            menu_admin(daftar_buku)

        elif pilihan == 2:
            menu_santri(daftar_buku)

        elif pilihan == 3:
            print("Terima kasih telah menggunakan sistem.")
            break

        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()
