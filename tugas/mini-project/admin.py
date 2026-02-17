from buku import tambah_buku, tampilkan_semua

def menu_admin(daftar_buku):
    print("\n=== MENU ADMIN ===")
    print("1. Tambah Kitab")
    print("2. Tampilkan Semua Kitab")

    try:
        pilihan = int(input("Pilih Menu: "))
    except ValueError:
        print("Input harus angka.")
        return

    if pilihan == 1:
        judul = input("Masukan Judul Kitab: ")
        kategori = input("Masukan Kategori Kitab: ")

        try:
            stok = int(input("Stok: "))
            if stok < 0:
                print("Stok tidak boleh negatif.")
                return
        except ValueError:
            print("Stok harus angka.")
            return

        tambah_buku(daftar_buku, judul, kategori, stok)
        print("Kitab berhasil ditambahkan.")

    elif pilihan == 2:
        tampilkan_semua(daftar_buku)

    else:
        print("Menu tidak valid.")
