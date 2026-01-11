from data import Mahasiswa

class ManajemenNilai:
    def __init__(self):
        self.data_mahasiswa = []

    def tambah_mahasiswa(self, nim, nama, nilai):
        if nilai < 0 or nilai > 100:
            raise ValueError("Nilai harus di antara 0 sampai 100")
        mahasiswa = Mahasiswa(nim, nama, nilai)
        self.data_mahasiswa.append(mahasiswa)

    def get_semua_data(self):
        return self.data_mahasiswa