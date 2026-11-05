banyak_mhs = int(input("Masukkan Jumlah Mahasiswa :"))

if banyak_mhs >= 5 and banyak_mhs <= 10:
    akumulasi_nilai = 0
    
    for idx in range(banyak_mhs):
        skor_masuk = int(input("Masukkan Nilai Mahasiswa :"))
        akumulasi_nilai = akumulasi_nilai + skor_masuk
        
    rerata_nilai = akumulasi_nilai / banyak_mhs
    print(f"nilai rata-ratanya : {rerata_nilai}")

    if rerata_nilai >= 95:
        hasil_huruf = "A"
    elif rerata_nilai >= 84:
        hasil_huruf = "B"
    elif rerata_nilai >= 68:
        hasil_huruf = "C"
    else:
        hasil_huruf = "D"
        
    print(f"Predikat: {hasil_huruf}")