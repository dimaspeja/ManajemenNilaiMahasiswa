# Program Manajemen Nilai Mahasiswa
## Dekripsi
Program Manajemen Nilai Mahasiswa adalah aplikasi berbasis **Python** yang dibuat untuk mengelola data nilai mahasiswa.  
Program ini menerapkan konsep **Object Oriented Programming (OOP)** dan **modular programming**, di mana kode dipisahkan ke dalam beberapa file sesuai fungsinya.

Pengguna dapat memasukkan data mahasiswa berupa **NIM, nama, dan nilai**, kemudian program akan melakukan **validasi input** serta menampilkan hasil dalam bentuk **tabel**.

## Tujuan Program
- Menerapkan konsep OOP dalam bahasa Python
- Menerapkan modular programming
- Melakukan validasi input pengguna
- Menentukan grade mahasiswa secara otomatis
- Menampilkan data mahasiswa dalam bentuk tabel

## Konsep yang Digunakan
- Object Oriented Programming (OOP)
- Modular Programming
- Class dan Object
- Constructor (`__init__`)
- Method
- Percabangan (`if - elif - else`)
- Exception Handling
- Input & Output Console

## Struktur Folder
uas-manajemen-nilai/
1. main.py # Program utama
2. data.py # Class Mahasiswa
3. process.py # Proses dan logika program
4. view.py # Tampilan output (tabel)
5. README.md # Dokumentasi program

## Penjelasan File
### 1. `data.py`
Berisi class `Mahasiswa` yang digunakan untuk menyimpan data mahasiswa dan menentukan grade berdasarkan nilai.

**Atribut:**
- `nim` : Nomor Induk Mahasiswa
- `nama` : Nama Mahasiswa
- `nilai` : Nilai Mahasiswa

**Method:**
- `grade()` : Menentukan nilai huruf (A–E)

### 2. `process.py`
Berisi class `ManajemenNilai` yang berfungsi untuk:
- Menyimpan data mahasiswa
- Menambahkan data mahasiswa
- Melakukan validasi nilai (0–100)

### 3. `view.py`
Digunakan untuk menampilkan data mahasiswa dalam bentuk **tabel** pada console.

### 4. `main.py`
Merupakan program utama yang:
- Menerima input dari pengguna
- Melakukan validasi NIM dan nilai
- Menghubungkan class `data`, `process`, dan `view`
- Menampilkan hasil akhir

## Aturan Penilaian Grade
| Nilai | Grade |
|------|-------|
| ≥ 85 | A |
| 70 – 84 | B |
| 60 – 69 | C |
| 50 – 59 | D |
| < 50 | E |

## Contoh Penggunaan
```python
Masukkan NIM (atau 'exit' untuk selesai): 12345
Masukkan Nama: Andi
Masukkan Nilai: 80
Data berhasil ditambahkan!

Masukkan NIM (atau 'exit' untuk selesai): exit
Output:
=== DAFTAR NILAI MAHASISWA ===
NIM       Nama                 Nilai     Grade
12345     Andi                 80        B
```
Validasi Program
- NIM hanya boleh berisi angka
- Nilai hanya boleh berupa angka
- Nilai harus berada pada rentang 0 – 100
- Jika input salah, program akan menampilkan pesan error tanpa berhenti

Demo program:
<img width="1421" height="439" alt="image" src="https://github.com/user-attachments/assets/06407a48-9e43-4a1a-81b2-b709ba7ed910" />

Dokumentasi dan Proses pembuatan Program:
https://www.youtube.com/watch?v=t8CWRVyozmU
