# Pembuatan Program Penilaian Rata-Rata
banyak_nilai = int(input('Input Banyak Data Nilai Anda : '))
list_nilai = []

# Pemrogramman While
i = 1
while i <= banyak_nilai:
    nilai = float(input("Masukkan Nilai Anda : "))
    list_nilai.append(nilai)
    i = i + 1

# Penghitungan Rata-Rata
rata_rata = sum(list_nilai)/banyak_nilai

# Menampilkan Rata-Rata pada Layar
print("Nilai Rata-Rata Anda Adalah : ", rata_rata)