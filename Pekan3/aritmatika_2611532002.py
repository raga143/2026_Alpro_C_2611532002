# Buat file dengan nama aritmatika_2611532002.py
# Buat program untuk operator aritmatika dalam Python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_2002
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2002 = int(input("Input angka-1: "))
angka2_2002 = int(input("Input angka-2: "))

# Penjumlahan
hasil_2002 = angka1_2002 + angka2_2002
print("\nOperator Penjumlahan")
print("Hasil =", hasil_2002)

# Pengurangan
hasil_2002 = angka1_2002 - angka2_2002
print("\nOperator Pengurangan")
print("Hasil =", hasil_2002)

# Perkalian
hasil_2002 = angka1_2002 * angka2_2002  
print("\nOperator Perkalian")
print("Hasil =", hasil_2002)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2002 != 0:
    hasil_2002 = angka1_2002 / angka2_2002
    print("\nOperator Pembagian")
    print("Hasil =", hasil_2002)

    hasil_2002 = angka1_2002 // angka2_2002
    print("\nOperator Pembagian Bulat")
    print("Hasil =", hasil_2002)

    hasil_2002 = angka1_2002 % angka2_2002
    print("\nOperator Sisa Bagi")
    print("Hasil =", hasil_2002)
else:
    print("Angka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2002 = angka1_2002 ** angka2_2002
print("\nOperator Pangkat")
print("Hasil =", hasil_2002)

