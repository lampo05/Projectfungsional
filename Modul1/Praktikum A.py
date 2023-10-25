class SistemInformasi:
    def __init__(self):
        self.peserta_data = []  # Inisialisasi daftar data peserta

    def tambah_peserta(self, nama, nilai):
        id_peserta = len(self.peserta_data)
        self.peserta_data.append({
            'ID': id_peserta,
            'Nama': nama,
            'Nilai': nilai,
            'Hasil Akhir': 'Lolos' if nilai >= 75 else 'Tidak Lolos'
        })
        print(f"Peserta {nama} berhasil ditambahkan.")

    def edit_nilai(self, id_peserta, nilai_baru):
        if id_peserta >= 0 and id_peserta < len(self.peserta_data):
            self.peserta_data[id_peserta]['Nilai'] = nilai_baru
            self.peserta_data[id_peserta]['Hasil Akhir'] = 'Lolos' if nilai_baru >= 75 else 'Tidak Lolos'
            print(f"Nilai peserta dengan ID {id_peserta} berhasil diubah menjadi {nilai_baru}.")
        else:
            print(f"ID peserta {id_peserta} tidak valid.")

    def tampilkan_data_peserta(self, id_peserta):
        if id_peserta >= 0 and id_peserta < len(self.peserta_data):
            peserta = self.peserta_data[id_peserta]
            return peserta
        else:
            print(f"ID peserta {id_peserta} tidak valid.")
            return None

def main():
    sistem_info = SistemInformasi()

    while True:
        print("\nMenu:")
        print("1. Tambah Peserta")
        print("2. Edit Nilai Peserta")
        print("3. Tampilkan Data Peserta")
        print("4. Keluar")
        pilihan = input("Pilih menu (1/2/3/4): ")

        if pilihan == '1':
            nama = input("Masukkan nama peserta: ")
            nilai = int(input("Masukkan nilai peserta: "))
            sistem_info.tambah_peserta(nama, nilai)
        elif pilihan == '2':
            id_peserta = int(input("Masukkan ID peserta yang ingin diubah nilainya: "))
            nilai_baru = int(input("Masukkan nilai baru: "))
            sistem_info.edit_nilai(id_peserta, nilai_baru)
        elif pilihan == '3':
            id_peserta = int(input("Masukkan ID peserta yang ingin ditampilkan datanya: "))
            peserta = sistem_info.tampilkan_data_peserta(id_peserta)
            if peserta:
                print(f"ID: {peserta['ID']}")
                print(f"Nama: {peserta['Nama']}")
                print(f"Nilai: {peserta['Nilai']}")
                print(f"Hasil Akhir: {peserta['Hasil Akhir']}")
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid. Silakan pilih menu yang benar.")

if __name__ == "__main__":
    main()
