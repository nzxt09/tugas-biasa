while True:
    x = input("Masukkan nama barang yang akan dibeli: ")
    jumlah = int(input("Masukkan jumlah barang yang akan dibeli: "))

    
    barang_yang_tersedia = {
        "ram": 50000,
        "keyboard": 10000,
        "psu": 20000,
        "1 set pc jadi": 100000,
        "mouse": 30000,
        "1 set pc jadi (premium)": 200000
    }


    if x in barang_yang_tersedia:
        harga_awal = barang_yang_tersedia[x]
        total_harga = harga_awal * jumlah

        
        if jumlah >= 10:
            diskon = 0.10  
        elif jumlah >= 5:
            diskon = 0.05 
        else:
            diskon = 0.0 

        
        harga_setelah_diskon = total_harga * (1 - diskon)

        
        print(f"Harga awal untuk {jumlah} {x}: {total_harga}")
        print(f"Diskon yang diterapkan: {diskon * 100}%")
        print(f"Harga setelah diskon: {harga_setelah_diskon}")
    else:
        print("Barang tidak tersedia.")

    
    lanjut = input("Apakah Anda ingin melanjutkan? (ketik 'ya' untuk melanjutkan, atau 'tidak' untuk berhenti): ").strip().lower()
    if lanjut != 'ya':
        print("Terima kasih telah menggunakan program ini!")
        break
