import os
import csv
from tabulate import tabulate
import pyinputplus as pypi

# Nama berkas untuk menyimpan data pasien dalam format CSV
berkas_data_pasien = "C:/Users/HP/Documents/Purwadhika/capstone project/data_pasien.csv"

# Fungsi untuk memeriksa apakah berkas data pasien kosong
def is_berkas_data_kosong():
    try:
        with open(berkas_data_pasien, "r", newline="") as berkas:
            return len(berkas.read()) == 0
    except FileNotFoundError:
        return True

# Fungsi untuk memuat data pasien dari berkas CSV jika ada
def muat_data_pasien():
    data_pasien = []
    if not is_berkas_data_kosong():
        with open(berkas_data_pasien, "r", newline="") as berkas:
            pembaca_csv = csv.DictReader(berkas)
            for row in pembaca_csv:
                data_pasien.append(row)
    return data_pasien

# Fungsi untuk menyimpan data pasien ke berkas CSV
def simpan_data_pasien(data):
    with open(berkas_data_pasien, "w", newline="") as berkas:
        fieldnames = ["No Rekam Medic", "Nama", "Kamar Pasien", "Poliklinik", "Jenis Bayar"]
        penulis_csv = csv.DictWriter(berkas, fieldnames=fieldnames)
        penulis_csv.writeheader()
        penulis_csv.writerows(data)

# Inisialisasi data pasien dari berkas
data_pasien = muat_data_pasien()

# Fungsi untuk menampilkan data semua pasien dalam bentuk tabel
def tampilkan_semua_pasien():
    if len(data_pasien) == 0:
        print("Tidak ada data pasien.")
    else:
        headers = ["No Rekam Medic", "Nama", "Kamar Pasien", "Poliklinik", "Jenis Bayar"]
        rows = []
        for pasien in data_pasien:
            row = [pasien.get("No Rekam Medic", ""), pasien["Nama"], pasien["Kamar Pasien"], pasien["Poliklinik"], pasien["Jenis Bayar"]]
            rows.append(row)

        print(tabulate(rows, headers, tablefmt="pretty"))

    input("\nTekan Enter untuk kembali ke menu utama...")  # Tunggu input sebelum kembali

# Fungsi untuk menambahkan data pasien dengan konfirmasi
def tambah_pasien():
    while True:
        no_rekam_medic = pypi.inputInt(prompt="Masukkan No Rekam Medic (4 digit): ", min=1000, max=9999)
        nama = input("Masukkan nama pasien: ")
        kamar = input("Masukkan data kamar pasien: ")
        poliklinik = input("Masukkan nama poliklinik: ")
        jenis_bayar = input("Masukkan jenis pembayaran: ")
        pasien = {
            "No Rekam Medic": str(no_rekam_medic),
            "Nama": nama,
            "Kamar Pasien": kamar,
            "Poliklinik": poliklinik,
            "Jenis Bayar": jenis_bayar
        }
        print("\nData pasien yang akan ditambahkan:")
        print(tabulate([pasien], headers="keys", tablefmt="pretty"))

        konfirmasi = pypi.inputChoice(["ya", "tidak"], prompt="Apakah Anda yakin ingin MENAMBAHKAN data pasien ini? (ya/tidak): ").lower()
        if konfirmasi == "ya":
            data_pasien.append(pasien)
            print("Data pasien telah ditambahkan.")
        else:
            print("Penambahan data pasien dibatalkan.")
        
        kembali = pypi.inputChoice(["ya", "tidak"], prompt="Kembali ke menu tambah pasien? (ya/tidak): ").lower()
        if kembali != "ya":
            break

# Fungsi submenu untuk Tambah data pasien
def submenu_tambah_pasien():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== TAMBAH DATA PASIEN ===")
        print("1. Tambahkan pasien")
        print("2. Kembali ke menu utama")
        pilihan = input("Pilih opsi (1/2): ")

        if pilihan == "1":
            tambah_pasien()
        elif pilihan == "2":
            return  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk mengedit data pasien dengan konfirmasi
def edit_pasien():
    if len(data_pasien) == 0:
        print("Tidak ada data pasien.")
    else:
        no_rekam_medic = input("Masukkan No Rekam Medic pasien yang ingin diedit: ")
        pasien_ditemukan = False

        for pasien in data_pasien:
            if pasien["No Rekam Medic"] == no_rekam_medic:
                pasien_ditemukan = True
                print("\nData pasien yang ingin diedit:")
                print(tabulate([pasien], headers="keys", tablefmt="pretty"))

                field = input("Masukkan nama kolom yang ingin diedit (huruf kecil): ").capitalize()
                if field in pasien:
                    new_value = input(f"Masukkan nilai baru untuk kolom '{field}': ")
                    print("Data pasien yang akan diupdate:")
                    pasien[field] = new_value
                    print(tabulate([pasien], headers="keys", tablefmt="pretty"))

                    konfirmasi = pypi.inputChoice(["ya", "tidak"], prompt="Apakah Anda yakin ingin MENGEDIT data pasien ini? (ya/tidak): ").lower()
                    if konfirmasi == "ya":
                        print("Data pasien telah diupdate.")
                    else:
                        print("Update data pasien dibatalkan.")
                    
                    kembali = pypi.inputChoice(["ya", "tidak"], prompt="Kembali ke menu edit pasien? (ya/tidak): ").lower()
                    if kembali != "ya":
                        return  # Keluar dari fungsi setelah selesai mengedit data
                
                else:
                    print(f"Kolom '{field}' tidak valid. Update data pasien dibatalkan.")
                break

        if not pasien_ditemukan:
            print("No Rekam Medic tidak ditemukan.")
        
        kembali = pypi.inputChoice(["ya", "tidak"], prompt="Kembali ke menu edit pasien? (ya/tidak): ").lower()
        if kembali != "ya":
            return  # Keluar dari fungsi setelah selesai mengedit atau jika tidak ingin kembali

# Fungsi submenu untuk Edit data pasien
def submenu_edit_pasien():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== EDIT DATA PASIEN ===")
        print("1. Edit data pasien")
        print("2. Kembali ke menu utama")
        pilihan = input("Pilih opsi (1/2): ")

        if pilihan == "1":
            edit_pasien()
        elif pilihan == "2":
            return  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi submenu untuk Hapus data pasien
def submenu_hapus_pasien():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== HAPUS DATA PASIEN ===")
        print("1. Hapus data pasien")
        print("2. Kembali ke menu utama")
        pilihan = input("Pilih opsi (1/2): ")

        if pilihan == "1":
            hapus_pasien()
        elif pilihan == "2":
            return  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk menghapus data pasien dengan konfirmasi
def hapus_pasien():
    if len(data_pasien) == 0:
        print("Tidak ada data pasien.")
    else:
        no_rekam_medic = input("Masukkan No Rekam Medic pasien yang ingin dihapus: ")
        pasien_ditemukan = None

        for pasien in data_pasien:
            if pasien["No Rekam Medic"] == no_rekam_medic:
                pasien_ditemukan = pasien
                print("\nData pasien yang akan dihapus:")
                print(tabulate([pasien], headers="keys", tablefmt="pretty"))

                konfirmasi = pypi.inputChoice(["ya", "tidak"], prompt="Apakah Anda yakin ingin MENGHAPUS data pasien ini? (ya/tidak): ").lower()
                if konfirmasi == "ya":
                    data_pasien.remove(pasien)
                    print("Data pasien berikut telah dihapus:")
                    print(tabulate([pasien], headers="keys", tablefmt="pretty"))
                else:
                    print("Penghapusan data pasien dibatalkan.")
                
                kembali = pypi.inputChoice(["ya", "tidak"], prompt="Kembali ke menu hapus pasien? (ya/tidak): ").lower()
                if kembali != "ya":
                    return  # Keluar dari fungsi setelah selesai menghapus data

        if pasien_ditemukan is None:
            print("No Rekam Medic tidak ditemukan.")
        
        kembali = pypi.inputChoice(["ya", "tidak"], prompt="Kembali ke menu hapus pasien? (ya/tidak): ").lower()
        if kembali != "ya":
            return  # Keluar dari fungsi jika tidak ingin kembali

# Fungsi untuk menampilkan menu utama
def menu_utama():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n=== MENU UTAMA ===")
        print("1. Tampilkan data semua pasien")
        print("2. Tambah data pasien")
        print("3. Edit data pasien")
        print("4. Hapus data pasien")
        print("5. Keluar")
        pilihan = input("Pilih opsi (1/2/3/4/5): ")

        if pilihan == "1":
            tampilkan_semua_pasien()
        elif pilihan == "2":
            submenu_tambah_pasien()
        elif pilihan == "3":
            submenu_edit_pasien()
        elif pilihan == "4":
            submenu_hapus_pasien()  # Panggil submenu untuk hapus data pasien
        elif pilihan == "5":
            konfirmasi = pypi.inputChoice(["ya", "tidak"], prompt="Apakah Anda yakin ingin keluar? (ya/tidak): ").lower()
            if konfirmasi == "ya":
                print("Program selesai.")
                simpan_data_pasien(data_pasien)
                return
            else:
                print("Keluar dibatalkan.")
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    print('Program dimulai.')
    menu_utama()
