jumlah = int(input("Masukkan jumlah mahasiswa: "))

data_mahasiswa = []
lulus = 0
tidak_lulus = 0

for i in range(jumlah):
    print("\nMahasiswa ke-", i + 1)

    nama = input("Masukkan nama: ")
    nilai = int(input("Masukkan nilai: "))

    if nilai >= 85:
        kategori = "A (Sangat Baik)"
        lulus += 1
    elif nilai >= 75:
        kategori = "B (Baik)"
        lulus += 1
    elif nilai >= 60:
        kategori = "C (Cukup)"
        lulus += 1
    else:
        kategori = "D (Tidak Lulus)"
        tidak_lulus += 1

    data_mahasiswa.append((nama, nilai, kategori))

print("\n===== HASIL PENILAIAN =====")

for mahasiswa in data_mahasiswa:
    print("Nama:", mahasiswa[0])
    print("Nilai:", mahasiswa[1])
    print("Kategori:", mahasiswa[2])
    print("--------------------")

print("Jumlah mahasiswa lulus:", lulus)
print("Jumlah mahasiswa tidak lulus:", tidak_lulus)
