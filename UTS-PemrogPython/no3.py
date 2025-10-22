def hitung_ongkir(berat_kg, kota, asuransi=False):
    """
    Menghitung total ongkir berdasarkan kota, berat, dan pilihan asuransi.
    Tambahkan 3000 jika asuransi = True.
    """
    tarif_dasar = {
        "Solo": 10000,
        "Jakarta": 15000,
        "Bandung": 12000,
        "Surabaya": 13000
    }

    if kota not in tarif_dasar:
        return "Kota tidak tersedia!"

    total = tarif_dasar[kota] + (2000 * berat_kg)
    #print(berat_kg)

    if asuransi:
        total += 3000
        #print("total dengan asuransi:", total)

    return total

print("Ongkir 1:", hitung_ongkir(3, "Solo"))
print("Ongkir 2:", hitung_ongkir(2, "Jakarta", asuransi=True))
