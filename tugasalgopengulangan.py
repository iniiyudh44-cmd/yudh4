mahasiswa = int(input("Masukkan Jumlah Mahasiswa :"))

if mahasiswa <= 10 and mahasiswa >= 5:
    nilai = 0
    
    for n in range(mahasiswa):
        nilai_inpt = int(input("Masukkan Nilai Mahasiswa :"))
        nilai = nilai + nilai_inpt
        
    nilai_rata_rata = nilai / mahasiswa
    print(f"nilai rata-ratanya : {nilai_rata_rata}")

    if nilai_rata_rata >= 95:
        predikat = "A"
    elif nilai_rata_rata >= 84:
        predikat = "B"
    elif nilai_rata_rata >= 68:
        predikat = "C"
    else:
        predikat = "D"
        
    print(predikat)