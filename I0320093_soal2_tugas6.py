banyak_nilai = int(input('Input Banyak Data Nilai Anda : '))
list_nilai = []

i = 1
while i <= banyak_nilai:
    nilai = float(input("Masukkan Nilai Anda : "))
    list_nilai.append(nilai)
    i = i + 1

rata_rata = sum(list_nilai)/banyak_nilai
print("Nilai Rata-Rata Anda Adalah : ", rata_rata)