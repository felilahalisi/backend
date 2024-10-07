def hitung_gaji(nama, golongan, jam_kerja):
    if golongan == 'A':
        upah_per_jam = 5000
    elif golongan == 'B':
        upah_per_jam = 7000
    elif golongan == 'C':
        upah_per_jam = 8000
    elif golongan == 'D':
        upah_per_jam = 10000
    else:
        return f"Golongan {golongan} tidak valid."
     
    upah = jam_kerja * upah_per_jam

    if jam_kerja > 48:
        jam_lembur = jam_kerja - 48
        uang_lembur = jam_lembur * 4000
    else:
        uang_lembur = 0

    total_gaji = upah + uang_lembur
    return f"{nama} menerima gaji sebesar Rp{total_gaji}"

nama_karyawan = input("Masukkan nama karyawan:")
golongan_karyawan = input("Masukkan golongan karyawan (A/B/C/D): ").upper()
jam_kerja_karyawan = int(input("Masukkan jam kerja per minggu:"))

gaji = hitung_gaji(nama_karyawan, golongan_karyawan, jam_kerja_karyawan)

print(gaji)
