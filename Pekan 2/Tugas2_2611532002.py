print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_2002 = input("Masukkan Nama Mahasiswa : ")
kelamin_2002 = input("Masukkan Jenis Kelamin (L/P): ")
umur_2002 = int(input("Masukkan Umur : "))
skor_2002 = float(input("Masukkan Skor Tes Awal : "))

alamat_2002 = """
Koto Luar,
Kecamatan Pauh,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_2002: Final = 75.0
token_2002 = 100+3j
lulus_2002 = skor_2002 > kkm_2002

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_2002," | ",type(nama_2002))
print("Jenis Kelamin : ",kelamin_2002," | ",type(kelamin_2002))
print("Alamat Domisili : ",alamat_2002," | ",type(alamat_2002))
print("Umur : ",umur_2002," tahun | ",type(umur_2002))
print("Skor Tes Awal : ",skor_2002," | ",type(skor_2002))
print("ID Token Sinyal: ",token_2002," | ",type(token_2002))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_2002," | ",type(kkm_2002))
print("Apakah Dinyatakan Lulus?: ",lulus_2002," | ",type(lulus_2002))