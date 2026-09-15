# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan identitas

print("======================================")
print("1. OPERATOR KEANGGOTAAN")
print("======================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_1021 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_1021 = [int(angka.strip() for angka in input_data_1021.split(','))]

nilai_dicari_1021 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_1021 = nilai_dicari_1021 in data_1021
print("\nOperator keanggotaan IN")
print(nilai_dicari_1021,"in",data_1021,"=",hasil_1021)

# Operator not in
hasil_1021 = nilai_dicari_1021 not in data_1021
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_1021,"not in",data_1021,"=",hasil_1021)

print("======================================")
print("2. OPERATOR IDENTIAS")
print("======================================")

# objek1 menggunakan list dari input perngguna
object1_1021 = data_1021

# objek2 merujuk pada objek yang sama dengan objek1
object2_1021 = object1_1021

# objek3 memiliki isi sama, tetapi merupakan objek baru
object3_1021 = data_1021.copy()

print("object1 =",object1_1021)
print("object2 =",object2_1021)
print("object3 =",object3_1021)

# Operator is
hasil_1021 = object1_1021 is object2_1021
print("\nOperator identitas IS")
print("objek1 is objek2 =",hasil_1021)

# Operator is not
hasil_1021 = object1_1021 is not object2_1021
print("\nOperator identitas IS NOT")
print("objek1 is not objek2 =",hasil_1021)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =",object1_1021 is object3_1021)
print("objek1 == objek3 =",object1_1021 == object3_1021)