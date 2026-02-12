from datetime import datetime
from typing import List, Optional


class User:
    def __init__(self, nama: str) -> None:
        self.nama = nama

    def get_role(self) -> str:
        return "User"


class Admin(User):
    def get_role(self) -> str:
        return "Admin"


class Santri(User):
    def get_role(self) -> str:
        return "Santri"


class Kitab:
    def __init__(self, judul: str, kategori: str, stok: int) -> None:
        self.judul = judul
        self.kategori = kategori
        self.__stok = stok

    @property
    def stok(self) -> int:
        return self.__stok

    def pinjam(self) -> bool:
        if self.__stok > 0:
            self.__stok -= 1
            return True
        return False

    def kembalikan(self) -> None:
        self.__stok += 1


class Perpustakaan:
    def __init__(self) -> None:
        self.__daftar_kitab: List[Kitab] = []

    def tambah_kitab(self, kitab: Kitab) -> None:
        self.__daftar_kitab.append(kitab)
        print("Kitab berhasil ditambahkan.")

    def tampilkan_semua(self) -> None:
        if not self.__daftar_kitab:
            print("Tidak ada kitab di perpustakaan.")
            return

        for kitab in self.__daftar_kitab:
            print(f"{kitab.judul} | {kitab.kategori} | Stok: {kitab.stok}")

    def cari_kitab(self, judul: str) -> Optional[Kitab]:
        for kitab in self.__daftar_kitab:
            if kitab.judul.lower() == judul.lower():
                return kitab
        return None


def main() -> None:
    perpustakaan = Perpustakaan()

    while True:
        print("\n===== SISTEM PERPUSTAKAAN KITAB SANTRI =====")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Santri")
        print("3. Keluar")

        try:
            pilihan = int(input("Pilih Menu: "))
        except ValueError:
            print("Input harus berupa angka.")
            continue

        if pilihan == 1:
            admin = Admin("Admin")
            print("\nSelamat datang Admin")
            print("1. Tambah Kitab")
            print("2. Tampilkan Semua Kitab")

            try:
                menu_admin = int(input("Pilih Menu: "))
            except ValueError:
                print("Input harus berupa angka.")
                continue

            if menu_admin == 1:
                judul = input("Masukan Judul Kitab: ")
                kategori = input("Masukan Kategori Kitab: ")

                try:
                    stok = int(input("Stok: "))
                    if stok < 0:
                        print("Stok tidak boleh negatif.")
                        continue
                except ValueError:
                    print("Stok harus berupa angka.")
                    continue

                kitab_baru = Kitab(judul, kategori, stok)
                perpustakaan.tambah_kitab(kitab_baru)

            elif menu_admin == 2:
                perpustakaan.tampilkan_semua()

            else:
                print("Menu tidak valid.")

        elif pilihan == 2:
            nama_santri = input("Masukan Nama Santri: ")
            santri = Santri(nama_santri)

            print(f"\nSelamat datang Santri {santri.nama}")
            print("1. Pinjam Kitab")
            print("2. Kembalikan Kitab")
            print("3. Tampilkan Semua Kitab")

            try:
                menu_santri = int(input("Pilih Menu: "))
            except ValueError:
                print("Input harus berupa angka.")
                continue

            if menu_santri == 1:
                judul = input("Masukan Judul Kitab yang ingin dipinjam: ")
                kitab = perpustakaan.cari_kitab(judul)

                if kitab:
                    if kitab.pinjam():
                        print(f"Berhasil meminjam kitab '{kitab.judul}'.")
                        print("Tanggal Pinjam:",
                              datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    else:
                        print(f"Kitab '{kitab.judul}' sedang tidak tersedia.")
                else:
                    print(f"Kitab dengan judul '{judul}' tidak ditemukan.")

            elif menu_santri == 2:
                judul = input("Masukan Judul Kitab yang ingin dikembalikan: ")
                kitab = perpustakaan.cari_kitab(judul)

                if kitab:
                    kitab.kembalikan()
                    print(f"Berhasil mengembalikan kitab '{kitab.judul}'.")
                    print("Tanggal Kembali:",
                          datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                else:
                    print(f"Kitab dengan judul '{judul}' tidak ditemukan.")

            elif menu_santri == 3:
                perpustakaan.tampilkan_semua()

            else:
                print("Menu tidak valid.")

        elif pilihan == 3:
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break

        else:
            print("Menu tidak valid.")


if __name__ == "__main__":
    main()