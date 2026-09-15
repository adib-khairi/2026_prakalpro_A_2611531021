# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print("======================================")
print("3. OPERATOR BITWISE")
print("======================================")

angka1_1021 = int(input("Masukkan angka bitwise-1: "))
angka2_1021 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =",angka1_1021,"| biner =",bin(angka1_1021))
print("angka1 =",angka2_1021,"| biner =",bin(angka2_1021))

# Bitwise AND
hasil_1021 = angka1_1021 & angka2_1021
print("\nBitwise AND (&)")
print(angka1_1021,"&",angka2_1021,hasil_1021)
print("Biner hasil =",bin(hasil_1021))
print("Biner hasil (8 bit) =",format(hasil_1021,"08b"))

# Bitwise OR
hasil_1021 = angka1_1021 | angka2_1021
print("\nBitwise OR (|)")
print(angka1_1021,"|",angka2_1021,hasil_1021)
print("Biner hasil =",bin(hasil_1021))
print("Biner hasil (8 bit) =",format(hasil_1021,"08b"))

# Bitwise XOR
hasil_1021 = angka1_1021 ^ angka2_1021
print("\nBitwise XOR (^)")
print(angka1_1021,"^",angka2_1021,hasil_1021)
print("Biner hasil =",bin(hasil_1021))
print("Biner hasil (8 bit) =",format(hasil_1021,"08b"))

# Bitwise NOT
hasil_1021 = ~angka1_1021
print("\nBitwise NOT (~)")
print(angka1_1021,"~",angka2_1021,hasil_1021)
print("Biner hasil =",bin(hasil_1021))
print("Biner hasil (8 bit) =",format(hasil_1021,"08b"))

# Bitwise geser kiri
jumlah_geser_1021 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_1021 = angka1_1021 << jumlah_geser_1021
print("\nBitwise geser kiri (<<)")
print(angka1_1021,"<<",jumlah_geser_1021,"=",hasil_1021)
print("Biner hasil =",bin(hasil_1021))
print("Biner hasil (8 bit) =",format(hasil_1021,"08b"))

# Bitwise geser kanan
hasil_1021 = angka1_1021 >> jumlah_geser_1021
print("\nBitwise geser kiri (>>)")
print(angka1_1021,">>",jumlah_geser_1021,"=",hasil_1021)
print("Biner hasil =",bin(hasil_1021))
print("Biner hasil (8 bit) =",format(hasil_1021,"08b"))