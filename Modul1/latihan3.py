# sistem penilaian akhir mahasiswa
# tambahkan fungsi untuk menghitung nilai akhir
#tambahkan fungsi untuk menghitung nilai akhir semua mahasiswa


def hitung_nilai_akhir(nilai_uts, nilai_uas):
    return (nilai_uts + nilai_uas) / 2

def hitung_nilai_akhir_semua(data_mahasiswa):
    data_nilai_akhir = {}
    for nama, nilai in data_mahasiswa.items():
        nilai_akhir = hitung_nilai_akhir(nilai["uts"], nilai["uas"])
        data_nilai_akhir[nama] = nilai_akhir
    return data_nilai_akhir
def tampilkan_nilai_akhir(data_nilai_akhir):
    print("hasil nilai akhir mahasiswa : ")
    for nama, nilai_akhir in data_nilai_akhir.items():
        print("nama : {}\tNilai Akhir : {: .2f}".format(nama, nilai_akhir))

def main():
    data_mahasiswa = {
        "Andika": {"uts": 80, "uas": 85},
        "Fathul": {"uts": 85, "uas": 90},
        "Bima.." : {"uts": 70, "uas": 85},
        "Galvan": {"uts": 72, "uas": 78},
        "Abdul" : {"uts": 75, "uas": 82}
        #data mahasiswa (nama sebagai key dan nilai UTS serta UAS sebagai value dalam bentuk dictionary)
    }

    data_nilai_akhir = hitung_nilai_akhir_semua(data_mahasiswa)

    tampilkan_nilai_akhir(data_nilai_akhir)

if  __name__ == "__main__":
    main()