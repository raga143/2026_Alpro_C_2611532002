# Buat file dengan nama assignment_2611532002.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_2002
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam Python

angka1_2002 = int(input("Input angka-1: "))
angka2_2002 = int(input("Input angka-2: "))

print("\nNilai awal angka1 =", angka1_2002)
print("Nilai angka2 =", angka2_2002)

# Assignment biasa
hasil_2002 = angka1_2002
print("\nAssignment biasa (=)")
print("Hasil =", hasil_2002)

# Assignment penambahan
hasil_2002 = angka1_2002
hasil_2002 += angka2_2002
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_2002)

# Assignment pengurangan
hasil_2002 = angka1_2002
hasil_2002 -= angka2_2002
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_2002)

# Assignment perkalian
hasil_2002 = angka1_2002
hasil_2002 *= angka2_2002
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_2002)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2002 != 0:
    hasil_2002 = angka1_2002
    hasil_2002 /= angka2_2002
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_2002)
    # Operator tambahan
    hasil_2002 = angka1_2002
    hasil_2002 //= angka2_2002
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_2002)
    hasil_2002 = angka1_2002
    hasil_2002 %= angka2_2002
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_2002)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_2002 = angka1_2002
hasil_2002 **= angka2_2002
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_2002)