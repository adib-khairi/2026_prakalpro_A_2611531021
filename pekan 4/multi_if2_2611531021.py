# Buat file dengan nama multi_if2_nim.py
# Buat program untuk kodisional if
# Nama variabel ditambah 4 digit terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()
# Program Menghitung Diskon Belanja

# Input dan user
total_belanja_1021 = float(input("Input Total Belanja (Rp): "))

# Input status member (mengecek apakah user mengetik 'y atau 't')
input_member_1021 = input("Apakah Anda Member (y/t): ").strip().lower()
is_member_1021 = input_member_1021 in ["y", "t"]

# Input satus kode promo (mengecek apakah user mengetik 'y atau 't')
input_promo_1021 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_1021 = input_promo_1021 in ["y", "t"]

total_diskon_persen_1021 = 0

# Multi-if terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi beberapa syarat sekaligus

if total_belanja_1021 > 1000000:
    total_diskon_persen_1021 += 10  # Diskon total besar

if is_member_1021:
    total_diskon_persen_1021 += 5  # Diskon member

if kode_promo_valid_1021:
    total_diskon_persen_1021 += 15  # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_1021 = total_belanja_1021 * (total_diskon_persen_1021 / 100)
total_bayar_1021 = total_belanja_1021 - nominal_diskon_1021

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon  : {total_diskon_persen_1021} (Rp {nominal_diskon_1021:.0f})")
print(f"Total Bayar   : Rp {total_bayar_1021:.0f}")

print(f"Total diskon yang Anda dapatkan: {total_diskon_persen_1021}%")
# Output: Total diskon yang Anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid