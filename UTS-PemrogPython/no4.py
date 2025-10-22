def jadwal_hari(hari):
    """Fungsi ini mengecek satu per satu isi list untuk menemukan jadwal pada hari tertentu."""
    
    jadwal = [
        {"hari": "Senin", "mata_kuliah": "Algoritma"},
        {"hari": "Selasa", "mata_kuliah": "Basis Data"},
        {"hari": "Rabu", "mata_kuliah": "Pemrograman"},
        {"hari": "Kamis", "mata_kuliah": "Jaringan Komputer"},
        {"hari": "Jumat", "mata_kuliah": "Kecerdasan Buatan"}
    ]
    #print(jadwal["Senin"])

    for item in jadwal:
        if item["hari"] == hari:
            return f"Jadwal hari {hari}: {item['mata_kuliah']}"
    
    return f"Tidak ada jadwal pada hari {hari}."

#print(jadwal_hari("Senin"))
print(jadwal_hari("Selasa"))
print(jadwal_hari("Rabu"))
print(jadwal_hari("Kamis"))
#print(jadwal_hari("Jumat"))
print(jadwal_hari("Sabtu"))
print(jadwal_hari("Minggu"))