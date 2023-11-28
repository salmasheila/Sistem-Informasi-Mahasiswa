class Nilai:
    def __init__(self, mata_kuliah, nilai):
        self.mata_kuliah = mata_kuliah
        self.nilai = nilai

    def __str__(self):
        return f"{self.mata_kuliah}: {self.nilai}"


class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.nilai = []

    def tambah_nilai(self, mata_kuliah, nilai):
        self.nilai.append(Nilai(mata_kuliah, nilai))

    def __str__(self):
        return f"Mahasiswa {self.nim}: {self.nama}"

class MataKuliah:
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

    def __str__(self):
        return f"{self.kode} - {self.nama}"