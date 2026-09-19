# Buat file dengan nama perbandingan_2611532002.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_2002
# Program ini menggunakan fungsi input()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam Python

angka1_2002 = int(input("Input angka-1: "))
angka2_2002 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_2002 = angka1_2002 > angka2_2002
print("\nOperator lebih besar dari")
print("angka1 > angka2 =", hasil_2002)

# Lebih kecil dari
hasil_2002 = angka1_2002 < angka2_2002
print("\nOperator lebih kecil dari")
print("angka1 < angka2 =", hasil_2002)

# Lebih besar dari atau sama dengan
hasil_2002 = angka1_2002 >= angka2_2002
print("\nOperator lebih besar dari atau sama dengan")
print("angka1 >= angka2 =", hasil_2002)

# Lebih kecil dari atau sama dengan
hasil_2002 = angka1_2002 <= angka2_2002
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1 <= angka2 =", hasil_2002)

# Sama dengan
hasil_2002 = angka1_2002 == angka2_2002
print("\nOperator sama dengan")
print("angka1 == angka2 =", hasil_2002)

# Tidak sama dengan
hasil_2002 = angka1_2002 != angka2_2002
print("\nOperator tidak sama dengan")
print("angka1 != angka2 =", hasil_2002)

# Tambahan: perbandingan berantai dalam Python
hasil_2002 = 0 < angka1_2002 < 100
print("\nPerbandingan berantai")
print("0 < angka1 < 100 =", hasil_2002)

hasil_2002 = 0 < angka2_2002 < 100
print("0 < angka2 < 100 =", hasil_2002)