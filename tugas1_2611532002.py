# Program menghitung keliling persegi

def hitung_keliling_persegi(sisi):
    """Menghitung keliling persegi berdasarkan panjang sisi."""
    keliling = 4 * sisi
    return keliling

# Meminta input dari pengguna
sisi = float(input("Masukkan panjang sisi persegi: "))

# Menghitung keliling
hasil = hitung_keliling_persegi(sisi)

# Menampilkan hasil
print(f"Keliling persegi dengan sisi {sisi} adalah {hasil}")