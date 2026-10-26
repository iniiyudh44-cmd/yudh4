print("== ==latihan= -")
 #input 
nama_barang = input("masukkan nama barang:")

harga_barang = int(input("masukkan harga barang:"))
#`proses
if nama_barang-lower()== "kulkas":
diskon =0.10 *harga_barang
elif nama_barang.lower()== "tv":
diskon =0.05 *harga_barang
elif nama_barang-lower() =="radio":
diskon 0
else:
print("nama barang tidak tersedia")
diskon = 0
jumlah_bayar = harga_barang - diskon
#output
print("========")
print("nama_barang:", nama_barang)
print("harga_barang:", harga_barang)
print("diskon :", diskon, diskon)
print("jumlah bayar:",jumlah_bayar)
print("=======")
