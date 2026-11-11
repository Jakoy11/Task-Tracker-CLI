
import json
import os
import sys
from datetime import datetime


# =====================================
# KONFIGURASI
# =====================================

FILE_NAME = "tasks.json"


# =====================================
# FUNGSI UNTUK MENGAMBIL WAKTU
# =====================================

def get_current_time():

    return datetime.now().astimezone().isoformat(timespec="seconds")


# =====================================
# FUNGSI UNTUK MEMBACA DATA TUGAS
# =====================================

def load_tasks():

    # Memeriksa apakah file tersedia
    if not os.path.exists(FILE_NAME):

        save_tasks([])
        return []

    # Membuka file JSON
    try:

        with open(FILE_NAME, "r", encoding="utf-8") as file:

            tasks = json.load(file)

        # Memeriksa apakah data berbentuk list
        if not isinstance(tasks, list):
            raise ValueError("Data JSON harus berbentuk daftar tugas.")

        # Menyesuaikan nama properti lama
        for task in tasks:

            if not isinstance(task, dict):
                raise ValueError("Data tugas tidak valid.")

            if "updatedAt" not in task and "updateAt" in task:
                task["updatedAt"] = task.pop("updateAt")

        return tasks

    except json.JSONDecodeError:

        print("ERROR: File JSON tidak valid.")
        sys.exit(1)

    except ValueError as error:

        print("ERROR:", error)
        sys.exit(1)


# =====================================
# FUNGSI UNTUK MENYIMPAN DATA TUGAS
# =====================================

def save_tasks(tasks):

    with open(FILE_NAME, "w", encoding="utf-8") as file:

        json.dump(
            tasks,
            file,
            indent=4,
            ensure_ascii=False
        )


# =====================================
# FUNGSI UNTUK MEMBUAT ID BARU
# =====================================

def generate_id(tasks):

    if len(tasks) == 0:

        return 1

    else:

        return max(task["id"] for task in tasks) + 1


# =====================================
# FITUR 1: MENAMBAHKAN TUGAS
# =====================================

def add_task(description):

    # Memeriksa deskripsi kosong
    if description.strip() == "":

        print("ERROR: Deskripsi tugas tidak boleh kosong.")
        return

    # Membaca data tugas
    tasks = load_tasks()

    # Membuat ID baru
    new_id = generate_id(tasks)

    # Mengambil waktu saat ini
    waktu_sekarang = get_current_time()

    # Membuat tugas baru
    new_task = {

        "id": new_id,
        "description": description,
        "status": "todo",
        "createdAt": waktu_sekarang,
        "updatedAt": waktu_sekarang

    }

    # Menambahkan tugas
    tasks.append(new_task)

    # Menyimpan data
    save_tasks(tasks)

    print(f"Task added successfully (ID: {new_id})")


# =====================================
# FITUR 2: MENAMPILKAN DAFTAR TUGAS
# =====================================

def list_tasks(status=None):

    # Membaca data tugas
    tasks = load_tasks()

    # Memeriksa apakah ada filter status
    if status is not None:

        if status not in ["todo", "in-progress", "done"]:

            print("ERROR: Status tidak valid.")
            return

        # Memfilter tugas berdasarkan status
        tasks = [
            task for task in tasks
            if task["status"] == status
        ]

    # Memeriksa apakah tugas kosong
    if len(tasks) == 0:

        print("Belum ada tugas yang tersedia.")
        return

    # Menampilkan judul
    print("\n========== DAFTAR TUGAS ==========")

    # Menampilkan setiap tugas
    for task in tasks:

        print("\nID          :", task["id"])
        print("Deskripsi   :", task["description"])
        print("Status      :", task["status"])
        print("Dibuat      :", task["createdAt"])
        print("Diperbarui  :", task["updatedAt"])

        print("----------------------------------")

    # Menampilkan jumlah tugas
    print("\nTotal Tugas:", len(tasks))


# =====================================
# FITUR 3: MEMPERBARUI TUGAS
# =====================================

def update_task(task_id, new_description):

    # Memeriksa deskripsi kosong
    if new_description.strip() == "":

        print("ERROR: Deskripsi tidak boleh kosong.")
        return

    # Membaca data tugas
    tasks = load_tasks()

    # Mencari tugas berdasarkan ID
    for task in tasks:

        if task["id"] == task_id:

            # Mengubah deskripsi
            task["description"] = new_description

            # Memperbarui waktu
            task["updatedAt"] = get_current_time()

            # Menyimpan perubahan
            save_tasks(tasks)

            print("Task updated successfully!")
            return

    # Jika ID tidak ditemukan
    print(f"ERROR: Tugas dengan ID {task_id} tidak ditemukan.")


# =====================================
# FITUR 4: MENGHAPUS TUGAS
# =====================================

def delete_task(task_id):

    # Membaca data tugas
    tasks = load_tasks()

    # Mencari tugas
    for task in tasks:

        if task["id"] == task_id:

            # Menghapus tugas
            tasks.remove(task)

            # Menyimpan perubahan
            save_tasks(tasks)

            print(f"Task deleted successfully (ID: {task_id})")
            return

    print(f"ERROR: Tugas dengan ID {task_id} tidak ditemukan.")


# =====================================
# FITUR 5 DAN 6: MENGUBAH STATUS TUGAS
# =====================================

def mark_task(task_id, new_status):

    # Membaca data tugas
    tasks = load_tasks()

    # Mencari tugas berdasarkan ID
    for task in tasks:

        if task["id"] == task_id:

            # Mengubah status
            task["status"] = new_status

            # Memperbarui waktu
            task["updatedAt"] = get_current_time()

            # Menyimpan perubahan
            save_tasks(tasks)

            print(f"Task status updated to: {new_status}")
            return

    print(f"ERROR: Tugas dengan ID {task_id} tidak ditemukan.")


# =====================================
# FUNGSI UNTUK MENAMPILKAN BANTUAN
# =====================================

def show_help():

    print("""
========== TASK TRACKER CLI ==========

DAFTAR PERINTAH:

1. Menambahkan tugas:
   py task_cli.py add "Nama Tugas"

2. Menampilkan semua tugas:
   py task_cli.py list

3. Memperbarui tugas:
   py task_cli.py update ID "Deskripsi Baru"

4. Menghapus tugas:
   py task_cli.py delete ID

5. Menandai sedang dikerjakan:
   py task_cli.py mark-in-progress ID

6. Menandai selesai:
   py task_cli.py mark-done ID

7. Menampilkan tugas belum dikerjakan:
   py task_cli.py list todo

8. Menampilkan tugas sedang dikerjakan:
   py task_cli.py list in-progress

9. Menampilkan tugas selesai:
   py task_cli.py list done

10. Menampilkan bantuan:
    py task_cli.py help

======================================
""")


# =====================================
# PROGRAM UTAMA
# =====================================

def main():

    # Mengambil argumen terminal
    args = sys.argv[1:]

    # Memeriksa apakah perintah kosong
    if len(args) == 0:

        show_help()
        return

    # Mengambil perintah
    command = args[0]

    # ---------------------------------
    # PERINTAH ADD
    # ---------------------------------

    if command == "add":

        if len(args) < 2:

            print("ERROR: Masukkan deskripsi tugas.")

        else:

            description = " ".join(args[1:]).strip()

            add_task(description)

    # ---------------------------------
    # PERINTAH LIST
    # ---------------------------------

    elif command == "list":

        if len(args) == 1:

            list_tasks()

        elif len(args) == 2:

            list_tasks(args[1])

        else:

            print("ERROR: Format perintah list tidak valid.")

    # ---------------------------------
    # PERINTAH UPDATE
    # ---------------------------------

    elif command == "update":

        if len(args) < 3:

            print("Gunakan: py task_cli.py update ID 'Deskripsi Baru'")

        else:

            try:

                task_id = int(args[1])

                new_description = " ".join(args[2:]).strip()

                update_task(task_id, new_description)

            except ValueError:

                print("ERROR: ID harus berupa angka.")

    # ---------------------------------
    # PERINTAH DELETE
    # ---------------------------------

    elif command == "delete":

        if len(args) != 2:

            print("Gunakan: py task_cli.py delete ID")

        else:

            try:

                task_id = int(args[1])

                delete_task(task_id)

            except ValueError:

                print("ERROR: ID harus berupa angka.")

    # ---------------------------------
    # PERINTAH MARK-IN-PROGRESS
    # ---------------------------------

    elif command == "mark-in-progress":

        if len(args) != 2:

            print("Gunakan: py task_cli.py mark-in-progress ID")

        else:

            try:

                task_id = int(args[1])

                mark_task(task_id, "in-progress")

            except ValueError:

                print("ERROR: ID harus berupa angka.")

    # ---------------------------------
    # PERINTAH MARK-DONE
    # ---------------------------------

    elif command == "mark-done":

        if len(args) != 2:

            print("Gunakan: py task_cli.py mark-done ID")

        else:

            try:

                task_id = int(args[1])

                mark_task(task_id, "done")

            except ValueError:

                print("ERROR: ID harus berupa angka.")

    # ---------------------------------
    # PERINTAH HELP
    # ---------------------------------

    elif command == "help":

        show_help()

    # ---------------------------------
    # PERINTAH TIDAK DIKENAL
    # ---------------------------------

    else:

        print("ERROR: Perintah tidak dikenal:", command)
        print("Gunakan: py task_cli.py help")


# =====================================
# MENJALANKAN PROGRAM
# =====================================

if __name__ == "__main__":

    main()
