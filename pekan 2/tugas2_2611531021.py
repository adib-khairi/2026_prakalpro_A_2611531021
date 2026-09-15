print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_1021 = input("Masukkan Nama Mahasiswa : ")
kelamin_1021 = input("Masukkan Jenis Kelamin (L/P): ")
umur_1021 = int(input("Masukkan Umur : "))
skor_1021 = float(input("Masukkan Skor Tes Awal : "))

alamat_1021 = """
Kampung dalam,
Kecamatan Pauh,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_1021: Final = 75.0
token_1021 = 100+3j
lulus_1021 = skor_1021 > kkm_1021

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_1021," | ",type(nama_1021))
print("Jenis Kelamin : ",kelamin_1021," | ",type(kelamin_1021))
print("Alamat Domisili : ",alamat_1021," | ",type(alamat_1021))
print("Umur : ",umur_1021," tahun | ",type(umur_1021))
print("Skor Tes Awal : ",skor_1021," | ",type(skor_1021))
print("ID Token Sinyal: ",token_1021," | ",type(token_1021))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_1021," | ",type(kkm_1021))
print("Apakah Dinyatakan Lulus?: ",lulus_1021," | ",type(lulus_1021))