# Tugas Kecil III IF2211 Strategi Algoritma
> Sebuah program untuk menyelesaikan permainan *15-Puzzle* menggunakan algoritma *branch and bound*.

## Daftar Isi
* [Informasi Umum](#informasi-umum)
* [Setup](#setup)
* [Struktur File](#struktur-file)
* [Penggunaan](#penggunaan)

## Informasi Umum
Program ini dibuat untuk memenuhi tugas Mata Kuliah IF2211 Strategi Algoritma

*Program Studi Teknik Informatika* <br />
*Sekolah Teknik Elektro dan Informatika* <br />
*Institut Teknologi Bandung* <br />

*Semester II Tahun 2021/2022*

Secara umum program ini dapat meminta input nama file berisi puzzle dalam bentuk matriks persegi berukuran 4x4 atau membuat puzzlenya sendiri secara acak. Kemudian program akan mencari langkah-langkah penyelesaiannya pada puzzle dengan menggunakan algoritma *branch and bound*.

## Setup
- Persyaratan dasar
    - Install [Python 3](https://www.python.org/downloads/).
    - Unduh repository ini dalam bentuk zip, kemudian ekstrak.
- Cara Eksekusi Program
    - Buka command prompt, kemudian arahkan ke folder src pada folder yang sudah diekstrak.
    - Jalankan program dengan command di bawah ini.
```
$ python main.py
```

## Struktur File
- **doc**
Laporan pengerjaan tugas.
- **src**
Seluruh file program serta program utama yakni *main.py*.
- **test**
Berisi file berekstensi *.txt* sebagai penyimpan puzzle.

## Penggunaan
1. Jalankan program main.py.
2. Pilih metode input puzzle.
3. Jika memilih untuk dibuat secara acak oleh program, pilih tingkat kesulitan puzzle.
    - Easy (mudah) untuk menggeser kotak kosong sebanyak 10 langkah. Pencarian relatif cepat.
    - Medium (menengah) untuk menggeser kotak kosong sebanyak 15 langkah. Pencarian membutuhkan waktu lebih banyak namun tetap lebih rendah daripada tingkat kesulitan Hard.
    - Hard (sulit) untuk menggeser kotak kosong sebanyak 20 langkah. Pencarian membutuhkan waktu paling banyak.
4. Jika memilih untuk menggunakan file, masukkan nama file.
5. Tunggu program menyelesaikan puzzle.
6. Jika sudah selesai, dapat memilih untuk keluar atau melakukan pencarian puzzle lain.

Jika ingin memasukkan puzzle baru, buatlah file dengan esktensi .txt pada folder test. Kemudian tulis puzzle sebagai matriks 4x4 berisi bilangan bulat berbeda dari 1 sampai 16 dengan 16 berperan sebagai kotak kosong. Berikut adalah format penulisannya.
```
<angka-1> <angka-2> <angka-3> <angka-4>
<angka-5> <angka-6> <angka-7> <angka-8>
<angka-9> <angka-10> <angka-11> <angka-12>
<angka-13> <angka-14> <angka-15> <angka-16>
```
Contoh
```
1 2 16 4
5 6 3 7
9 10 15 8
13 14 12 11
```

## Author
Dibuat oleh [Muhammad Helmi Hibatullah](https://github.com/mhelmih) - 13520014
