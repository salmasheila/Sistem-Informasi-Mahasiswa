from mahasiswa import Mahasiswa,MataKuliah


# Buat beberapa mahasiswa
mahasiswa1 = Mahasiswa("M001", "John Doe")
mahasiswa2 = Mahasiswa("M002", "Jane Smith")

# Buat beberapa mata kuliah
matkul1 = MataKuliah("MK001", "Matematika Dasar")
matkul2 = MataKuliah("MK002", "Bahasa Inggris")

# Tambahkan nilai mahasiswa
mahasiswa1.tambah_nilai(matkul1, 90)
mahasiswa1.tambah_nilai(matkul2, 85)

mahasiswa2.tambah_nilai(matkul1, 78)
mahasiswa2.tambah_nilai(matkul2, 92)

# Tampilkan informasi mahasiswa dan nilai
print(mahasiswa1)
for nilai in mahasiswa1.nilai:
    print(nilai)

print("\n")

print(mahasiswa2)
for nilai in mahasiswa2.nilai:
    print(nilai)
