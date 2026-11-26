#PROGRAM REKAP NILAI KELAS
#AUTHOR: M. ALVIN JAUHARI

#Pendefinisian nilai KKM
KKM = 70

# Fungsi untuk menghitung rata-rata
def hitung_rata(data):
    total = 0
    for x in data:
        total += x
    return round(total / len(data), 2)

# Fungsi untuk mencari nilai tertinggi
def cari_tertinggi(data):
    tinggi = data[0]
    posisi = 0
    for i in range(len(data)):
        if data[i] > tinggi:
            tinggi = data[i]
            posisi = i
    return (tinggi, posisi)

#Fungsi untuk mencari nama 
def cari_nama(daftar, target):
    posisi = -1
    for i in range(len(daftar)):
        if daftar[i] == target:
            posisi = i
            break
    return posisi

#Awalnya, menginput berapa jumlah mahasiswa
jumlah = int(input("Jumlah mahasiswa: "))

#buat variabel tampungan
nama = []
nilai = []

for mhs in range(jumlah):
    nama.append(input("Nama: "))
    nilai.append(float(input("Nilai: ")))

print()
# Rata rata kemudian di tampilkan
print("Rata-rata kelas:", hitung_rata(nilai))

# Nilai tertinggi muncul
tinggi, posisi = cari_tertinggi(nilai)
print(f"Nilai tertinggi: {tinggi} oleh {nama[posisi]}")

# Validasi, apakah diperlukan remidial. jika <70 maka remidial
print("Perlu remedial (nilai < 70):")
ada = False
for i in range(jumlah):
    if nilai[i] < KKM:
        print(f"- {nama[i]} ({nilai[i]})")
        ada = True
if not ada:
    print("- tidak ada")

# Mencari nama mahasiswa berdasarkan data yang sudah diinputkan
cari = input("Cari nama mahasiswa: ")
posisi = cari_nama(nama, cari)
if posisi != -1:
    print(f"{cari} mendapat nilai {nilai[posisi]}")
else:
    print(f"{cari} tidak terdaftar")