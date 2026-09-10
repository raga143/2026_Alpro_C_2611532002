# Buat file dengan nama Boolean_2611532002.py
# nama variabel ditambah 4 digit terakhir NIM contoh: a_1234
# Deklarasikan variabel dengan tipe data boolean
is_lulus= True
is_cumlaude= True

# Menggunakan Boolean
nilai_2002= 85
batal_lulus_2002= 75

# menentukan nilai boolean dari kondisi
status_kelulusan = nilai_2002>=batal_lulus_2002 # Hasilnya akan true

print("=== Check Kelulussn ===")
print("Nilai:",nilai_2002)
print("apakah lulus?:", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat anda lulus dengan predikat cumlaude")