# Inisialisasi kurs mata uang global dan status konversi
kurs_global = {'usd_to_idr': 14000, 'idr_to_usd': 1 / 14000}
konversi_dilakukan = False  # Menyimpan informasi apakah konversi telah dilakukan

# Fungsi konversi untuk menghitung hasil konversi
def konversi(mata_uang, jumlah):
    global kurs_global  # Mengakses kurs mata uang global
    kurs_lokal = kurs_global  # Menggunakan variabel lokal untuk kurs mata uang
    if mata_uang == 'usd_to_idr':
        return jumlah * kurs_lokal['usd_to_idr']
    elif mata_uang == 'idr_to_usd':
        return jumlah * kurs_lokal['idr_to_usd']
    else:
        return None

# Fungsi untuk menampilkan daftar kurs mata uang
def tampilkan_kurs():
    global kurs_global  # Mengakses kurs mata uang global
    for key, value in kurs_global.items():
        from_currency, to_currency = key.split('_to_')
        print(f"1 {from_currency.upper()} = {value} {to_currency.upper()}")

# Fungsi untuk melakukan konversi pada daftar mata uang
def konversi_daftar(mata_uang, daftar):
    return list(map(lambda x: konversi(mata_uang, x), daftar))

# Program utama
while True:
    print("\nKonverter Mata Uang")
    print("Pilih operasi:")
    print("1. Konversi IDR ke USD")
    print("2. Konversi USD ke IDR")
    if konversi_dilakukan:
        print("3. Lihat Daftar Kurs")
    print("4. Konversi Daftar Mata Uang")
    print("5. Keluar")

    pilihan = input("Masukkan nomor operasi (1/2/3/4/5): ")

    if pilihan == '5':
        print("Terima kasih! Program selesai.")
        break

    if pilihan == '1' or pilihan == '2':
        mata_uang = 'idr_to_usd' if pilihan == '1' else 'usd_to_idr'
        jumlah = float(input(f"Masukkan jumlah mata uang ({mata_uang.split('_')[0].upper()}): "))
        hasil = konversi(mata_uang, jumlah)
        if hasil is not None:
            print(f"Hasil konversi: {jumlah} {mata_uang.split('_')[0].upper()} = {hasil} {mata_uang.split('_')[1].upper()}")
            konversi_dilakukan = True  # Menandai bahwa konversi telah dilakukan
        else:
            print("Pilihan mata uang tidak valid.")

    elif pilihan == '3':
        if konversi_dilakukan:
            while True:
                print("\nDaftar Kurs Mata Uang:")
                tampilkan_kurs()
                kembali = input("\nTekan 'Enter' untuk kembali ke menu utama: ")
                if kembali == '':
                    break
        else:
            print("Belum ada konversi yang dilakukan. Silakan pilih menu 1 atau 2 terlebih dahulu.")

    elif pilihan == '4':
        mata_uang = input("Masukkan tipe konversi (usd_to_idr / idr_to_usd): ")
        daftar_jumlah = input("Masukkan daftar jumlah dalam format pemisah koma (misalnya: 100,200,300): ")
        daftar_jumlah = [float(x.strip()) for x in daftar_jumlah.split(',')]
        hasil = konversi_daftar(mata_uang, daftar_jumlah)
        if hasil is not None:
            print(f"Hasil konversi daftar: {daftar_jumlah} {mata_uang.split('_')[0].upper()} = {hasil}")
        else:
            print("Pilihan mata uang tidak valid.")

    else:
        print("Pilihan tidak valid. Silakan pilih nomor operasi yang benar.")
