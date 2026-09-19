# Buat file dengan nama lainnya_2611532002.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_2002
# Program ini menggunakan fungsi input()
# Program operator keanggotaan dan  identitas

print("========================================")
print("1. OPERATOR KEANGGOTAAN")
print("========================================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2002 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2002 = [int(angka_2002.strip()) for angka_2002 in input_data_2002.split(",")]

nilai_dicari_2002 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_2002 = nilai_dicari_2002 in data_2002
print("\nOperator keanggotaan IN")
print(nilai_dicari_2002, "in", data_2002, "=", hasil_2002)

# Operator not in
hasil_2002 = nilai_dicari_2002 not in data_2002
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2002, "not in", data_2002, "=", hasil_2002)

print("\n========================================")
print("2. OPERATOR IDENTITAS")
print("========================================")

# objek1 menggunakan list dari input pengguna
objek1_2002 = data_2002

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2002 = objek1_2002

# objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_2002 = data_2002.copy()

print("objek1 =", objek1_2002)
print("objek2 =", objek2_2002)
print("objek3 =", objek3_2002)

# Operator is
hasil_2002 = objek1_2002 is objek2_2002
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_2002)

# Operator is not
hasil_2002 = objek1_2002 is not objek3_2002
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_2002)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_2002 is objek3_2002)
print("objek1 == objek3 =", objek1_2002 == objek3_2002)