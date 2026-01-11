class Tampilan:
    @staticmethod
    def tampilkan_tabel(data):
        print("\n=== DAFTAR NILAI MAHASISWA ===")
        print("-" * 50)
        print(f"{'NIM':<10}{'Nama':<20}{'Nilai':<10}{'Grade'}")
        print("-" * 50)

        for mhs in data:
            print(f"{mhs.nim:<10}{mhs.nama:<20}{mhs.nilai:<10}{mhs.grade()}")

        print("-" * 50)