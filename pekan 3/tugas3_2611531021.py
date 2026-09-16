print("=== SISTEM TRANSAKSI TOKO ===")
nama_1021 = input("Masukkan Nama Pelanggan : ")
status_1021 = input("Masukkan Status Pelanggan (member/nonmember) : ")
total_1021 = int(input("Masukkan Total Belanja : "))
jumlah_1021 = int(input("Masukkan Jumlah Barang : "))
promo_1021 = input("Masukkan Kode Promo : ")

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan       : {nama_1021}")
print(f"Status Pelanggan     : {status_1021}")
print(f"Total Belanja        : Rp{total_1021}")
print(f"Jumlah Barang        : {jumlah_1021}")
print(f"Kode Promo           : {promo_1021}")

kode_promo_1021 = ["HEMAT10", "HEMAT20", "HIDUPMAHASISWA", "HIDUPFTI"]

syarat_total_1021 = total_1021 >= 200000
syarat_jumlah_1021 = jumlah_1021 >= 3
status_valid_1021 = status_1021 == "member"
promo_valid_1021 = promo_1021 in kode_promo_1021

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {syarat_total_1021}")
print(f"Jumlah Barang >= 3         : {syarat_jumlah_1021}")
print(f"Status Member              : {status_valid_1021}")
print(f"Kode Promo Tersedia        : {promo_valid_1021}")
print(f"Mendapatkan Diskon         : {syarat_jumlah_1021 or syarat_total_1021}")
print(f"Mendapatkan Promo          : {promo_valid_1021}")

diskon_1021 = 0.05

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                      : Rp{diskon_1021 * total_1021}")
print(f"Total Pembayaran            : Rp{total_1021 - total_1021 * diskon_1021}")
print(f"Rata-rata Harga Barang      : Rp{(total_1021 - total_1021 * diskon_1021)/jumlah_1021}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses              : ...")
print(f"Member Access               : {status_valid_1021}")
print(f"Promo Access                : {promo_valid_1021}")
print(f"Free Shipping Access        : ...")

kode_transaksi_1021 = int(status_valid_1021) << 0 | int(syarat_total_1021) << 1 | int(syarat_jumlah_1021) << 2 | int(promo_valid_1021) << 3
kode_referensi_1021 = int(status_valid_1021) << 0 | int(syarat_total_1021) << 1 | int(promo_valid_1021) << 3

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print(f"{format(int(status_valid_1021) << 0,"04b")} | {format(int(syarat_total_1021) << 1,"04b")} | {format(int(syarat_jumlah_1021) << 2,"04b")} | {format(int(promo_valid_1021) << 3,"04b")}")
print(f"Kode Biner   : {format(kode_transaksi_1021,"04b")}")
print(f"Kode Desimal : {kode_transaksi_1021}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{format(kode_transaksi_1021,"04b")} & {format(int(status_valid_1021) << 0,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_1021) & int(status_valid_1021) << 0,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_1021) & int(status_valid_1021) << 0}")

print("Cek Promo")
print(f"{format(kode_transaksi_1021,"04b")} & {format(int(promo_valid_1021) << 3,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_1021) & int(promo_valid_1021) << 3,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_1021) & int(promo_valid_1021) << 3}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {format(kode_transaksi_1021,"04b")}")
print(f"Kode Referensi : {format(kode_referensi_1021,"04b")}")
print(f"{format(kode_transaksi_1021,"04b")} ^ {format(kode_referensi_1021,"04b")}")
print(f"Hasil Biner   : {format((kode_transaksi_1021) ^ 11,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_1021) ^ (kode_referensi_1021)}")

print("\n=== Shift ===")
print(f"{format(kode_transaksi_1021,"04b")} << 1")
print(f"Hasil Biner   : {format((kode_transaksi_1021) << 1,"04b")}")
print(f"Hasil Desimal : {(kode_transaksi_1021) << 1}") 
print("=== SELESAI ===")