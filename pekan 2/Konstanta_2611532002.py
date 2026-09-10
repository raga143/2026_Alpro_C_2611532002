# Buat file baru dengan nama Konstanta_2611532002.py
# program ini menggunakan konstanta untuk menghitung luas lingkaran
# nama variabel ditambah 4 digit terakhir NIM contoh: phi_1234

from typing import Final
PI_2002: Final = 3.14
print("pi: %f" % (PI_2002))
jari_2002 = float(input('Masukkan jari-jari: '))
Luas_2002 = PI_2002 * jari_2002 * jari_2002
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2002, Luas_2002))