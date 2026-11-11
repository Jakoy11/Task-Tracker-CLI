# Task Tracker CLI

Task Tracker CLI adalah aplikasi berbasis Command Line Interface (CLI) yang dibuat menggunakan bahasa pemrograman Python.

Aplikasi ini digunakan untuk mencatat, mengelola, dan melacak perkembangan tugas melalui terminal.

## Tujuan Proyek

Proyek ini dibuat untuk mempelajari dasar-dasar pemrograman Python, khususnya:

- Penggunaan function
- Penggunaan conditional statement
- Penggunaan perulangan
- Pengelolaan file JSON
- Penggunaan command line arguments
- Penanganan error

## Teknologi yang Digunakan

- Python
- JSON
- Built-in Python Libraries

## Fitur Aplikasi

1. Menambahkan tugas baru.
2. Menampilkan seluruh tugas.
3. Memperbarui deskripsi tugas.
4. Menghapus tugas.
5. Menandai tugas sedang dikerjakan.
6. Menandai tugas selesai.
7. Menampilkan tugas berdasarkan status.

## Struktur Proyek

task-tracker/
│
├── .gitignore
├── task_cli.py
├── README.md
└── tasks.json (dibuat otomatis saat aplikasi dijalankan)

## Cara Menjalankan

Pastikan Python sudah terinstal.

Buka terminal pada folder proyek, kemudian jalankan:

py task_cli.py help

## Daftar Perintah

Menambahkan tugas:
py task_cli.py add "Belajar Python"

Melihat semua tugas:
py task_cli.py list

Memperbarui tugas:
py task_cli.py update 1 "Belajar Python Lanjutan"

Menghapus tugas:
py task_cli.py delete 1

Menandai sedang dikerjakan:
py task_cli.py mark-in-progress 1

Menandai selesai:
py task_cli.py mark-done 1

Melihat tugas belum dikerjakan:
py task_cli.py list todo

Melihat tugas sedang dikerjakan:
py task_cli.py list in-progress

Melihat tugas selesai:
py task_cli.py list done

## Penyimpanan Data

Seluruh data tugas disimpan dalam file tasks.json menggunakan format JSON.

Setiap tugas memiliki properti:

- id
- description
- status
- createdAt
- updatedAt

## Status Proyek

Proyek Task Tracker CLI telah selesai dibuat dan seluruh fitur utama telah diuji.

## Project URL

GitHub Repository: https://github.com/Jakoy11/Task-Tracker-CLI
URL: https://roadmap.sh/projects/task-tracker
