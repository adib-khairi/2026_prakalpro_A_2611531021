# Buar file dengan nama Boolean_2611531021
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data Boolean
is_lulus_1021 = True
is_cumlaude_1021 = True

# Menggunakan Boolean
nilai_1021 = 85
batas_lulus_1021 = 75

# Menantukan nilai Boolean dari kondisi
status_kelulusan_1021 = nilai_1021 >= batas_lulus_1021 # Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai: ",nilai_1021)
print("Apakah lulus?: ",status_kelulusan_1021)
if is_lulus_1021 and is_cumlaude_1021:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")