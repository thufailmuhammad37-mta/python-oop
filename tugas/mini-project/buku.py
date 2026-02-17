def tambah_buku(daftar_buku, judul, kategori, stok):
    buku = {
        "judul": judul,
        "kategori": kategori,
        "stok": stok
    }
    daftar_buku.append(buku)

def tampilkan_semua(daftar_buku):
    if len(daftar_buku) == 0:
        print("Tidak ada kitab di perpustakaan.")
        return

    for buku in daftar_buku:
        print(f"{buku['judul']} | {buku['kategori']} | Stok: {buku['stok']}")

def cari_buku(daftar_buku, judul):
    for buku in daftar_buku:
        if buku["judul"].lower() == judul.lower():
            return buku
    return None


def pinjam_buku(buku):
    if buku["stok"] > 0:
        buku["stok"] -= 1
        return True
    return False


def kembalikan_buku(buku):
    buku["stok"] += 1
