# Buat file dengan nama assigment_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menngunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assigment dalam Python

angka1_1021 = int(input("Input angka-1: "))
angka2_1021 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =",angka1_1021)
print("Nilai angka2 =",angka2_1021)

# Assigment biasa
hasil_1021 = angka1_1021 
print("\nAssigment biasa (=)")
print("Hasil =",hasil_1021)

# Assigment penambahan
hasil_1021 = angka1_1021 
hasil_1021 += angka2_1021 
print("\nAssigment penambahan (+=)")
print("Hasil =",hasil_1021)

# Assigment pengurangan
hasil_1021 = angka1_1021 
hasil_1021 -= angka2_1021 
print("\nAssigment pengurangan (-=)")
print("Hasil =",hasil_1021)

# Assigment perkalian
hasil_1021 = angka1_1021 
hasil_1021 *= angka2_1021
print("\nAssigment perkalian (*=)")
print("Hasil =",hasil_1021)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_1021 != 0:
    hasil_1021 = angka1_1021 
    hasil_1021 /= angka2_1021
    print("\nAssigment pembagian (/=)")
    print("Hasil =",hasil_1021)
    # Operator tambahan
    hasil_1021 = angka1_1021 
    hasil_1021 //= angka2_1021
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =",hasil_1021)
    hasil_1021 = angka1_1021 
    hasil_1021 %= angka2_1021
    print("\nOperator sisa bagi (%=)")
    print("Hasil =",hasil_1021)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil_1021 = angka1_1021 
hasil_1021 **= angka2_1021
print("\nOperator perpangkatan (**=)")
print("Hasil =",hasil_1021)