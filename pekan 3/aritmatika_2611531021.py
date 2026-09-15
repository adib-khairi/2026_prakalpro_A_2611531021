# Buat file dengan nama aritmatika_NIM.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_1021 = int(input("Input angka-1: "))
angka2_1021 = int(input("Input angka-2: "))

# Penjumlahan
hasil_1021 = angka1_1021 + angka2_1021
print("\nOperator Penjumlahan")
print("Hasil =",hasil_1021)

# Pengurangan
hasil_1021 = angka1_1021 - angka2_1021
print("\nOperator Pengurangan")
print("Hasil =",hasil_1021)

# Perkalian
hasil_1021 = angka1_1021 * angka2_1021
print("\nOperator Perkalian")
print("Hasil =",hasil_1021)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_1021 != 0:
    hasil_1021 = angka1_1021 / angka2_1021
    print("\nOperator Pembagian")
    print("Hasil =",hasil_1021)

    hasil_1021 = angka1_1021 // angka2_1021
    print("\nOperator Pembagian Bulat")
    print("Hasil =",hasil_1021)

    hasil_1021 = angka1_1021 % angka2_1021
    print("\nOperator Sisa Bagi")
    print("Hasil =",hasil_1021)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_1021 = angka1_1021 ** angka2_1021
print("\nOperator Pangkat")
print("Hasil =",hasil_1021)