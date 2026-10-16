# Pertemuan 07 Fungsi Python
Nama: Wulan Nur'aini
NIM: 2225250131
Kelas: 3E
## Tujuan
Menggunakan fungsi, parameter, return value, dan scope untuk membuat program modular.
## Cara Menjalankan
python3 praktik/utilitas_matematika.py
## Struktur Fungsi
1. luas_persegi_panjang(p, l)
Parameter: p (float/int, panjang), l (float/int, lebar)
Return Value: float atau int (hasil perkalian p * l)
Deskripsi: Menghitung dan mengembalikan luas persegi panjang berdasarkan panjang dan lebar.
2. luas_segitiga(a, t)
Parameter: a (float/int, alas), t (float/int, tinggi)
Return Value: float (hasil perkalian 0.5 * a * t)
Deskripsi: Menghitung dan mengembalikan luas segitiga berdasarkan alas dan tinggi.
3. jumlah_n(n)
Parameter: n (int, bilangan bulat)
Return Value: int (total penjumlahan $1 + 2 + \dots + n$) atau str (pesan error jika $n < 0$)
Deskripsi: Menghitung total deret angka 1 sampai $n$ dengan validasi bahwa $n$ adalah bilangan bulat nonnegatif.
4. faktorial(n)
Parameter: n (int, bilangan bulat)
Return Value: int (hasil perkalian $n!$) atau str (pesan error jika $n < 0$)
Deskripsi: Menghitung nilai faktorial dari $n$ menggunakan perulangan dengan validasi bahwa $n$ adalah bilangan bulat nonnegatif.
5. tampilkan_menu()
Parameter: Tidak ada (None)
Return Value: Tidak ada (None)
Deskripsi: Menampilkan daftar opsi menu operasi matematika ke layar terminal.
## Hasil Pengujian

| No | Fungsi / Latihan | Input / Test Case | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | `salam` | `nama="Alya"`, `kelas="10A"` | `Halo, Alya dari kelas 10A...` | `Halo, Alya dari kelas 10A...` | Berhasil |
| 2 | `luas_persegi_panjang` | `p = 8`, `l = 5` | `40` | `40` | Berhasil |
| 3 | `luas_persegi_panjang` | `p = 2.5`, `l = 4` | `10` | `10.0` | Berhasil |
| 4 | `luas_persegi_panjang` | `p = 0`, `l = 7` | `0` | `0` | Berhasil |
| 5 | `luas_segitiga` | `a = 6`, `t = 4` | `12.0` | `12.0` | Berhasil |
| 6 | `jumlah_n` | `n = 1` | `1` (Rumus: `1`) | `1` | Berhasil |
| 7 | `jumlah_n` | `n = 5` | `15` (Rumus: `15`) | `15` | Berhasil |
| 8 | `jumlah_n` | `n = 10` | `55` (Rumus: `55`) | `55` | Berhasil |
| 9 | `jumlah_n` | `n = 100` | `5050` (Rumus: `5050`) | `5050` | Berhasil |
| 10 | `jumlah_n` (validasi) | `n = -5` | Pesan Error | Error: n harus berupa bilangan bulat nonnegatif! | Berhasil |
| 11 | `faktorial` | `n = 0` | `1` | `1` | Berhasil |
| 12 | `faktorial` | `n = 5` | `120` | `120` | Berhasil |

## Refleksi
Bagian program yang menjadi jauh lebih sederhana setelah dipisah menjadi fungsi adalah alur perulangan utama (main) dan logika perhitungan matematika. Sebelum menggunakan fungsi, logika perhitungan (seperti algoritma perulangan faktorial dan penjumlahan $1 \dots n$) harus ditulis langsung di dalam blok if-elif pada menu utama. Hal ini membuat kode program di dalam menu utama menumpuk, sulit dibaca, dan berisiko tinggi saat ingin melakukan perbaikan.
Dengan memisahkannya ke dalam fungsi tersendiri (seperti faktorial(n) dan jumlah_n(n)):
1. Menu Utama Lebih Rapi: Menu utama hanya bertugas menerima masukan pengguna, memanggil fungsi yang sesuai, dan menampilkan hasilnya.
2. Reusabilitas Kode: Logika perhitungan dapat dipanggil berulang kali dari mana saja tanpa perlu menulis ulang algoritma perulangannya.
3. Kemudahan Debugging: Jika ada kesalahan pada rumus atau logika validasi nonnegatif, perbaikan cukup dilakukan pada fungsi yang bersangkutan tanpa mengganggu tampilan menu atau fungsi lainnya.
