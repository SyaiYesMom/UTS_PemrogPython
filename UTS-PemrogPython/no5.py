import os
import csv
import json
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)

folder = "data"
if not os.path.exists(folder):
    os.mkdir(folder)
    logging.info("Folder 'data' berhasil dibuat.")
else:
    logging.info("Folder 'data' sudah ada, lanjut...")

csv_file = os.path.join(folder, "presensi.csv")

try:
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["nim", "nama", "hadir_uts"])
        writer.writerow(["2301", "Syailendra", 1])
        writer.writerow(["2302", "Suryaa", 0])
        writer.writerow(["2303", "Lendraa", 1])
    logging.info("File CSV berhasil dibuat dan ditulis.")
except Exception as e:
    logging.error(f"Gagal menulis file CSV: {e}")

try:
    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        data = list(reader)

        total = len(data)
        hadir = sum(int(row["hadir_uts"]) for row in data)
        persen = (hadir / total) * 100

        ringkasan = {
            "total_mahasiswa": total,
            "jumlah_hadir": hadir,
            "persentase_hadir": f"{persen:.2f}%"
        }
        print(f"Total Mahasiswa: {ringkasan['total_mahasiswa']}\nJumlah Hadir: {ringkasan['jumlah_hadir']}\nPersentase Hadir: {ringkasan['persentase_hadir']}")
        #print(f"Jumlah Hadir: {ringkasan['jumlah_hadir']}")
        #print(f"Persentase Hadir: {ringkasan['persentase_hadir']}")

    json_file = os.path.join(folder, "ringkasan.json")
    with open(json_file, mode="w") as jf:
        json.dump(ringkasan, jf, indent=4)

    logging.info("Data berhasil dibaca & disimpan ke JSON.")

except Exception as e:
    logging.error(f"Terjadi kesalahan saat membaca/menulis file: {e}")