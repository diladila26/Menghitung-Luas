def persegi():
    
    sisi = int(input("Masukkan Nilai sisi :  "))
    

    # Masukkan ke dalam rumus luas persegi
    persegi = (sisi * sisi) 
    #hasil
    print("Luas persegi adalah: %d" %persegi)
    
def segitiga():
    alas = int(input("Masukkan Nilai alas :  "))
    tinggi = int(input("Masukkan Nilai Tinggi :  "))
    
    #Rumus Luas Segitiga
    segitiga = ((1/2) * alas * tinggi)
    
    # Hasil Luas Segitiga
    print("Luas Segitiga adalah: %d" %segitiga)
    

def luas_lingkaran():
    #Membuat variabel pi dan r atau jari jaari
    pi = 3.14;
    r = int(input("Masukkan Nilai jari-jari :  "))

    #masukkan ke dalam rumus luas lingkaran
    luas_lingkaran= (pi * r * r) 

    #hasil
    panjang = int(input("Masukkan Nilai PI : "))
    lebar = int(input("Masukkan Nilai jari jari : "))
    
    print("Luas Lingkaran adalah: %d" %luas_lingkaran)
    

print("✍︎✍︎✍︎✍︎Tugas 3 PBO KELAS H✍︎✍︎✍︎✍︎")
print("PROGRAM SEDERHANA MENGHITUNG LUAS")
print("==SEGITIIGA PERSEGI DAN LINGKARAN==")
print(" ")
print("➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪➪")
print("☻︎☻︎☻︎☻︎NAMA : NURPADILAH☻︎☻︎☻︎☻︎")
print("✔︎✔︎✔︎✔︎NIM : D0220340✔︎✔︎✔︎✔︎")
print("☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎☟︎︎︎")
print(" ")
print("~~~~MENU PILIHAN~~~~~~")
print("=================")
print("1. Persegi")
print("2. Segitiga")
print("3. Lingkaran")
print("============")
print(" ")


masukkan = int(input("masukkan menu: "))
if masukkan == 1:
    persegi()
elif masukkan == 2:
    segitiga()
elif masukkan == 3:
    luas_lingkaran()
else:
    print("Terima Kasih")