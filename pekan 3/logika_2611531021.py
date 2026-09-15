# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
# Program ini menngunakan fungsi input()
# Program operator logika dalam Python

# Memasukan nilai boolean
# Input tidak peka terhadap huruf besar dan kecil
a1_1021 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_1021 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 = ",a1_1021)
print("A2 = ",a2_1021)

# Konjungsi: bernilai True jika keduanya True
hasil_1021 = a1_1021 and a2_1021
print("\nKonjungsi (AND)")
print("A1 and A2 =",hasil_1021)

# Disjungsi: bernilai True jika salah satunya False
hasil_1021 = a1_1021 or a2_1021
print("\nDisjungsi (OR)")
print("A1 or A2 =",hasil_1021)

# Negasi A1: membalik nilai A1
hasil_1021 = not a1_1021
print("\nNegasi A1(NOT)")
print("not A1",hasil_1021)

# Negasi A2: membalik nilai A2
hasil_1021 = not a2_1021
print("\nNegasi A2(NOT)")
print("not A2",hasil_1021)

# XOR: bernilai True jika kedua nilai berbeda
hasil_1021 = a1_1021 != a2_1021
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2",hasil_1021)