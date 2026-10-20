# Pertemuan 09 - List dan Pengolahan Data Numerik

- **Nama:** Lina Mulyana Ismail
- **NIM:** 2225250145
- **Mata Kuliah:** Algoritma dan Pemrograman (S1 Pendidikan Matematika FKIP Untirta)[cite: 1, 12]

## Tujuan
Mempelajari cara menyimpan, mengakses, memanipulasi, dan mengolah kumpulan data numerik menggunakan list/array di Python, serta mendokumentasikannya melalui Git dan GitHub[cite: 1, 12].

## Struktur Program
- `latihan/01_buat_list.py`: Pembuatan list dan pengecekan panjang data[cite: 3].
- `latihan/02_indeks_slicing.py`: Penerapan indeks positif, negatif, dan slicing[cite: 3].
- `latihan/03_manipulasi_list.py`: Operasi ubah, tambah, sisip, dan hapus elemen[cite: 3, 6].
- `latihan/04_agregasi_nilai.py`: Perhitungan total, rata-rata, nilai min dan max[cite: 3, 7].
- `latihan/05_filter_kelulusan.py`: Penyaringan data berdasarkan batas kelulusan[cite: 3, 7, 8].
- `latihan/06_fungsi_statistik.py`: Penerapan fungsi modular untuk menghitung rata-rata[cite: 3, 8].
- `praktik/analisis_nilai_mahasiswa.py`: Program utama analisis data nilai ujian mahasiswa[cite: 3, 11].

## Cara Menjalankan Program Praktik
Buka terminal di VS Code, lalu jalankan perintah berikut[cite: 12]:
```bash
python3 praktik/analisis_nilai_mahasiswa.py

## Test Case
| Data Masukan | Yang Diperiksa | Hasil yang Diharapkan | Status |
| :--- | :--- | :--- | :--- |
| `[60, 70, 80]` | Rata-rata | `70.00` | Lulus[cite: 11] |
| `[60, 70, 80]` | Minimum / Maksimum | `60 / 80` | Lulus[cite: 11] |
| `[60, 70, 80]` | Jumlah lulus | `3` | Lulus[cite: 11] |
| `[59, 60, 61]` | Batas kelulusan (60) | `2` orang lulus | Lulus[cite: 11] |
| `[]` (Kosong) | Penanganan list kosong pada fungsi rata-rata | Tidak error (`0`) | Lulus[cite: 8, 11] |

## Refleksi
Pemahaman: Saya memahami bahwa indeks list di Python dimulai dari angka 0, serta pemanfaatan fungsi len() dan sum() sangat memudahkan proses agregasi data numerik tanpa harus melakukan iterasi manual yang panjang.   
Kendala/Perbaikan: Sempat mengalami kesalahan logika saat menyaring kelulusan akibat salah menentukan batas kondisi if x >= 60, namun berhasil diperbaiki dengan menyesuaikan kembali parameter operator perbandingannya.