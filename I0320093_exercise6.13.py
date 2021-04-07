def tambah(a,b) :
    c = a + b
    return c
x = int(input("Masukkan Bilangan ke-1 : "))
y = int(input("Masukkan Bilangan ke-2 : "))

hasil = tambah(x,y)
print("%d + %d = %d" %(x, y, hasil))