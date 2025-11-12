# Split Running Text

Program Python untuk membaca file teks dari shared folder, memisahkan konten berdasarkan delimiter, dan mengekspor setiap bagian ke file terpisah secara otomatis.

## 🎯 Fitur Utama

- **Koneksi Otomatis ke Shared Folder** - Menghubungkan ke network drive dengan authentikasi username dan password
- **Deteksi Encoding Otomatis** - Mendukung berbagai encoding (UTF-8, Latin-1, ISO-8859-1, CP1252, Windows-1252)
- **Split File Dinamis** - Memisahkan konten berdasarkan delimiter custom (default: `@_@`)
- **Pembersihan Folder Otomatis** - Menghapus file lama sebelum membuat file baru
- **Pelaporan Proses** - Menampilkan status setiap tahap dengan indikator visual ✓ ❌ 🎉

## 🛠️ Teknologi yang Digunakan

- **Python 3.7+**
- **Library Built-in:**
  - `os` - Manajemen file dan folder
  - `sys` - Kontrol sistem
  - `subprocess` - Eksekusi command Windows
  - `datetime` - Manipulasi tanggal dan waktu

## 📋 Prasyarat Instalasi

### Sistem Operasi
- Windows 7 atau lebih baru

### Requirements
- Python 3.7 atau lebih tinggi
- Akses ke shared folder dengan username dan password
- Koneksi jaringan ke server (contoh: `\\192.168.0.113`)

### Instalasi
```bash
# Clone atau download project ini
git clone <repository-url>
cd Split-Running-Text-

# Tidak ada dependency eksternal yang perlu diinstal
# Semua menggunakan library built-in Python
```

## 📁 Struktur Project

```
Split-Running-Text-/
│
├── RunningText.py          # File utama program
├── README.md               # Dokumentasi ini
└── .gitignore              # File yang diabaikan git
```

## ⚙️ Konfigurasi

Edit bagian `if __name__ == "__main__":` di `RunningText.py`:

```python
# Username dan Password untuk shared folder
username = "your_username"          # Ganti dengan username Anda
password = "your_password"          # Ganti dengan password Anda

# Path shared folder
shared_folder = f"\\\\192.168.0.113\\bahan berita\\2025\\RUNNING TEXT\\..."

# Folder untuk hasil output
result_folder = r"C:\CPNS\RUNNING TEXT TERBARU NOVEMBER 2025"

# Delimiter pemisah konten
split_char = '@_@'
```

## 🚀 Contoh Penggunaan

### Cara Dasar

1. **Konfigurasi File**
   - Buka `RunningText.py`
   - Ubah `username` dan `password` dengan kredensial shared folder Anda
   - Sesuaikan `shared_folder` dan `result_folder` path

2. **Jalankan Program**
   ```bash
   python RunningText.py
   ```

3. **Hasil Output**
   - Program akan membuat file-file terpisah bernama `01.txt`, `02.txt`, `03.txt`, dll
   - Setiap file berisi satu bagian dari konten yang dipisahkan

### Contoh File Input

**File: 11.txt** (dari shared folder)
```
Berita Pertama@_@Berita Kedua@_@Berita Ketiga
```

**Output Files** (di result folder):
- `01.txt` → `Berita Pertama`
- `02.txt` → `Berita Kedua`
- `03.txt` → `Berita Ketiga`

## 📝 Penjelasan Fungsi Utama

### `connect_to_shared_folder(shared_folder_path, username, password)`
Menghubungkan PC ke shared folder menggunakan kredensial yang diberikan.

```python
connect_to_shared_folder("\\\\192.168.0.113\\bahan berita", "user", "pass")
```

### `disconnect_shared_folder(shared_folder_path)`
Memutuskan koneksi dari shared folder.

### `detect_encoding(file_path)`
Mendeteksi encoding file secara otomatis dari berbagai format.

### `read_split_and_export(shared_folder_path, result_folder_path, filename, split_char)`
Fungsi utama yang membaca, memisah, dan mengekspor file.

## 🔐 Keamanan

**Penting:** Jangan commit credentials ke repository!

### Rekomendasi:
- Simpan username dan password di environment variable
- Gunakan file konfigurasi terpisah yang tidak ter-track git
- Hanya bagikan file dengan orang yang terpercaya

Contoh dengan environment variable:
```python
import os
username = os.getenv('SHARED_FOLDER_USER')
password = os.getenv('SHARED_FOLDER_PASS')
```

## 🐛 Troubleshooting

### Error: "Access Denied"
- Pastikan username dan password benar
- Cek koneksi jaringan ke server
- Verifikasi permissions shared folder

### Error: "File not found"
- Pastikan file input tersedia di path yang benar
- Cek format path shared folder

### Error: "UnicodeDecodeError"
- Program akan otomatis mendeteksi encoding
- Jika tetap gagal, periksa format file input

## 🤝 Kontribusi

Kontribusi sangat diterima! Untuk berkontribusi:

1. Fork repository ini
2. Buat branch fitur Anda (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add some AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buka Pull Request

## 📄 Lisensi

Project ini dilisensikan di bawah **MIT License** - lihat file [LICENSE](LICENSE) untuk detail.

---

**Dibuat dengan ❤️ untuk automasi proses Running Text**
