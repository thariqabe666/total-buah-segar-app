# 🍓 Aplikasi Kasir Ultra Buah Segar

Aplikasi web sederhana yang dibuat menggunakan Streamlit untuk mensimulasikan sistem manajemen inventaris dan kasir untuk toko buah. Pengguna dapat melihat daftar buah yang tersedia, menambahkan buah baru ke inventaris, menghapus buah, dan menambahkan item ke keranjang belanja untuk proses checkout.


## ✨ Fitur Utama

* **Tampilkan Daftar Buah**: Melihat semua buah yang tersedia beserta stok dan harganya dalam format tabel yang rapi.
* **Manajemen Inventaris**:
    * **Tambah Buah**: Menambahkan jenis buah baru ke dalam daftar inventaris.
    * **Hapus Buah**: Menghapus buah dari daftar inventaris.
* **Keranjang Belanja**:
    * Menambahkan buah dari daftar ke keranjang belanja.
    * Stok akan otomatis berkurang saat item ditambahkan.
    * Melihat rincian belanja dan total harga.
* **Checkout**: Menyelesaikan transaksi dan mengosongkan keranjang.
* **Manajemen State**: Menggunakan `st.session_state` untuk menjaga data inventaris dan keranjang tetap konsisten selama sesi penggunaan.

## 🛠️ Teknologi yang Digunakan

* **Python**: Bahasa pemrograman utama.
* **Streamlit**: Framework untuk membangun aplikasi web interaktif.
* **Pandas**: Untuk manipulasi dan tampilan data yang efisien.

## 🚀 Instalasi dan Cara Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan aplikasi ini di komputer lokal Anda.

### 1. **Prasyarat**

Pastikan Anda sudah menginstal Python 3.7 atau versi yang lebih baru di sistem Anda.

### 2. **Clone Repository**

Clone repositori ini ke mesin lokal Anda menggunakan perintah berikut:

```bash
git clone [URL_REPOSITORY_ANDA]
cd [NAMA_FOLDER_REPOSITORY_ANDA]
```

### 3. **Buat Virtual Environment (Opsional tapi Direkomendasikan)**

Sangat disarankan untuk membuat lingkungan virtual agar dependensi proyek tidak tercampur dengan instalasi Python global Anda.

```bash
# Untuk Windows
python -m venv venv
.\venv\Scripts\activate

# Untuk macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. **Instal Dependensi**

Buat file bernama `requirements.txt` dan isi dengan teks di bawah ini:

```txt
streamlit
pandas
```

Kemudian, instal semua pustaka yang diperlukan dengan satu perintah:

```bash
pip install -r requirements.txt
```

### 5. **Jalankan Aplikasi**

Setelah instalasi selesai, jalankan aplikasi Streamlit dengan perintah berikut di terminal Anda:

```bash
streamlit run total_buah_segar_app.py
```

Aplikasi akan otomatis terbuka di browser default Anda.

## 📖 Cara Menggunakan Aplikasi

Setelah aplikasi berjalan, Anda akan melihat sidebar di sebelah kiri dengan beberapa pilihan menu:

1.  **Tampilkan Buah**: Halaman utama di mana Anda bisa melihat daftar buah yang tersedia. Di halaman ini juga Anda dapat memilih buah dan jumlahnya untuk ditambahkan ke keranjang.
2.  **Tambah Buah**: Pindah ke halaman ini untuk menambahkan data buah baru (nama, stok, dan harga) ke dalam sistem.
3.  **Hapus Buah**: Gunakan menu ini untuk memilih dan menghapus buah dari daftar inventaris.
4.  **Keranjang**: Lihat semua item yang telah Anda tambahkan. Di sini Anda bisa melihat total belanja, melakukan **Checkout** untuk menyelesaikan pesanan, atau **Kosongkan Keranjang**.

Semoga berhasil dengan proyek Anda!
