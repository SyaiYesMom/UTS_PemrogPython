setoran1 = int(input("Masukkan setoran 1: "))
setoran2 = int(input("Masukkan setoran 2: "))
setoran3 = int(input("Masukkan setoran 3: "))

if setoran1 <= 0 or setoran2 <= 0 or setoran3 <= 0:
    print("Input tidak valid (harus lebih dari 0)")
else:
    total = setoran1 + setoran2 + setoran3

    if total < 300000:
        print("Total:", total, "- Kategori: Rendah")
    elif total <= 600000:
        print("Total:", total, "- Kategori: Sedang")
    else:
        print("Total:", total, "- Kategori: Sangat Tinggi")