gaji_diinginkan = float(input("Masukkan gaji per jam yang diinginkan: "))
jam_kerja = float(input("Masukkan jam kerja per minggu: "))
minggu = 5 

pendapatan = gaji_diinginkan * jam_kerja * minggu
print("Pendapatan selama libur sebelum bayar pajak:", pendapatan)

pajak = 14 / 100
pendapatansetelahpajak = pendapatan * (1 - pajak)
print("Pendapatan selama libur setelah bayar pajak:", pendapatansetelahpajak)

baju_aksesoris = 10 / 100
jumlah_baju_aksesoris = pendapatansetelahpajak * baju_aksesoris
pendapatansetelahbajuaksesoris = pendapatansetelahpajak - jumlah_baju_aksesoris
print("Jumlah uang yang dihabiskan untuk beli baju dan aksesoris:", jumlah_baju_aksesoris)

alat_tulis = 1 / 100
jumlah_alat_tulis = pendapatansetelahbajuaksesoris * alat_tulis
pendapatansetelahalattulis = pendapatansetelahbajuaksesoris - jumlah_alat_tulis
print("Jumlah uang yang dihabiskan untuk beli alat tulis:", jumlah_alat_tulis)

sedekah = 25 / 100
jumlah_sedekah = pendapatansetelahalattulis * sedekah  
pendapatansetelahsedekah = pendapatansetelahalattulis - jumlah_sedekah
print("Jumlah uang yang disedekahkan:", jumlah_sedekah)

jumlah_anak_yatim = (jumlah_sedekah // 1000) * 1000 * (30 / 100)  
print("Jumlah uang yang diberikan kepada anak yatim:", jumlah_anak_yatim)

jumlah_kaum_dhuafa = (jumlah_sedekah // 1000) * 1000 * (70 / 100) 
print("Jumlah uang yang diberikan kepada kaum dhuafa:", jumlah_kaum_dhuafa)
