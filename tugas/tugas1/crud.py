from prettytable import PrettyTable

data = []

def tambah_data():
    print("\n===== TAMBAH DATA =====")
    id = int(input("Masukkan ID      : "))
    nama = input("Masukkan Nama    : ")
    kelas = input("Masukkan Kelas   : ")

    data.append({
        "id": id,
        "nama": nama,
        "kelas": kelas
    })

    print("✅ Data berhasil ditambahkan\n")

def tampil_data():
    print("\n===== DATA SISWA =====")

    if len(data) == 0:
        print("Data masih kosong\n")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Kelas"]

    for d in data:
        table.add_row([d["id"], d["nama"], d["kelas"]])

    print(table)
    print()

def ubah_data():
    print("\n===== UBAH DATA =====")
    id_cari = int(input("Masukkan ID yang ingin diubah: "))

    for d in data:
        if d["id"] == id_cari:
            d["nama"] = input("Nama baru  : ")
            d["kelas"] = input("Kelas baru : ")
            print("✅ Data berhasil diubah\n")
            return

    print("❌ Data tidak ditemukan\n")

def hapus_data():
    print("\n===== HAPUS DATA =====")
    id_hapus = int(input("Masukkan ID yang ingin dihapus: "))

    for d in data:
        if d["id"] == id_hapus:
            data.remove(d)
            print("✅ Data berhasil dihapus\n")
            return

    print("❌ Data tidak ditemukan\n")

while True:
    print("===== MENU =====")
    print("1. Tambah data")
    print("2. Tampilkan data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("0. Keluar")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 1:
        tambah_data()
    elif pilihan == 2:
        tampil_data()
    elif pilihan == 3:
        ubah_data()
    elif pilihan == 4:
        hapus_data()
    elif pilihan == 0:
        print("Program selesai. Terima kasih.")
        break
    else:
        print("❌ Menu tidak tersedia\n")
