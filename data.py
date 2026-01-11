class Mahasiswa:
    def __init__(self, nim, nama, nilai):
        self.nim = nim
        self.nama = nama
        self.nilai = nilai

    def grade(self):
        if self.nilai >= 85:
            return "A"
        if self.nilai >= 70:
            return "B"
        if self.nilai >= 60:
            return "C"
        if self.nilai >= 50:
            return "D"
        else:
            return "E"