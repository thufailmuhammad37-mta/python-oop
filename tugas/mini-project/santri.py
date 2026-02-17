from buku import cari_buku, tampilkan_semua, pinjam_buku, kembalikan_buku
from datetime import datetime

def menu_santri(daftar_buku):
    nama = input("Masukan Nama Santri: ")
    print(f"\nSelamat datang {nama}")

    print("1. Pinjam Kitab")
    print("2. Kembalikan Kitab")
    print("3. Tampilkan Semua Kitab")

    try:
        pilihan = int(input("Pilih Menu: "))
    except ValueError:
        print("Input harus angka.")
        return

    if pilihan == 1:
        judul = input("Masukan Judul Kitab yang ingin dipinjam: ")
        buku = cari_buku(daftar_buku, judul)

        if buku:
            if pinjam_buku(buku):
                print(f"Berhasil meminjam '{buku['judul']}'")
                print("Tanggal Pinjam:",
                      datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            else:
                print("Stok tidak tersedia.")
        else:
            print("Kitab tidak ditemukan.")

    elif pilihan == 2:
        judul = input("Masukan Judul Kitab yang ingin dikembalikan: ")
        buku = cari_buku(daftar_buku, judul)

        if buku:
            kembalikan_buku(buku)
            print(f"Berhasil mengembalikan '{buku['judul']}'")
            print("Tanggal Kembali:",
                  datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        else:
            print("Kitab tidak ditemukan.")

    elif pilihan == 3:
        tampilkan_semua(daftar_buku)

    else:
        print("Menu tidak valid.")
