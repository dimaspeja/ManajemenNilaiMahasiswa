from proses import ManajemenNilai
from view import Tampilan

def main():
    manajemen = ManajemenNilai()

    while True:
        try:
            nim = input("Masukkan NIM (atau 'exit' untuk selesai): ")
            if nim.lower() == "exit":
                break
            if not nim.isdigit():
                raise ValueError("NIM hanya boleh berisi angka")
            
            nama = input("Masukkan Nama: ")
            nilai = int(input("Masukkan Nilai: "))
            manajemen.tambah_mahasiswa(nim, nama, nilai)
            print("Data berhasil ditambahkan!\n")

        except ValueError as e:
            print(f"Error: {e}\n")

    Tampilan.tampilkan_tabel(manajemen.get_semua_data())

if __name__ == "__main__":
    main()