Seorang dosen ingin merekap nilai mahasiswanya. Program membaca jumlah mahasiswa, lalu nama
dan nilai setiap mahasiswa disimpan dalam dua list yang sejajar: nama[i] adalah pemilik nilai[i].
Program kemudian menampilkan rata-rata kelas, nilai tertinggi beserta pemiliknya, daftar mahasiswa
yang perlu remedial, dan nilai seorang mahasiswa yang dicari berdasarkan nama.
Ketentuan:

KKM -> 70, nilai dibawah 70 perlu remidial
Rata rata -> dibulatkan angka desimal
Fungsi bawaan -> Tidak boleh memakai sum(), max(), atau index()

Program wajib memakai fungsi-fungsi berikut:

hitung_rata| Data| rata-rata| akumulator
cari_tertinggi| data | Tuple (nilai, indeks) |Nilai ekstrem
cari_nama| daftar, target | Indeks, atau -1 jika tidak ada | Pencarian linier
berpenanda