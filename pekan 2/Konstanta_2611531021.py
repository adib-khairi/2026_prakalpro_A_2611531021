# Buat file dengan nama Konstanta_2611531021
# Program ini menggunakan konstanta untuk menghitun luas lingkaran
# nama variabel ditambah 4 digit nim terakhir contoh: jari_1021

from typing import Final
PI: Final = 3.14
print("Pi: %f" % (PI))
jari_1021 = float(input("Masukkan nilai jari-jari: "))
luas_1021 = PI * jari_1021
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_1021,luas_1021))