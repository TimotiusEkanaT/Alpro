n = int(input('Masukkan jumlah kategori: '))
data_aplikasi = {}

for i in range(n):
    nama_kategori = input('Masukkan nama kategori:')
    print('Masukkan 5 nama aplikasi di kategori', nama_kategori)
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input('Nama aplikasi: ')
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori] = aplikasi

print('\nData Aplikasi per Kategori:')
print(data_aplikasi)

daftar_aplikasi_list = []
for aplikasi in data_aplikasi.values():
    daftar_aplikasi_list.append(set(aplikasi))

print('\nSet Aplikasi per Kategori:')
print(daftar_aplikasi_list)

hasil = daftar_aplikasi_list[0]
for i in range(1, len(daftar_aplikasi_list)):
    hasil = hasil.intersection(daftar_aplikasi_list[i])

print('\nAplikasi yang muncul di SEMUA kategori:')
print(hasil)

gabungan_semua = set()

from collections import Counter

semua_aplikasi_flat = []

for s in daftar_aplikasi_list:
    gabungan_semua |= s
    semua_aplikasi_flat += list(s)

frekuensi_aplikasi = Counter(semua_aplikasi_flat)

unik_satu_kategori = {app for app, freq in frekuensi_aplikasi.items() if freq == 1}
print('\nAplikasi yang hanya muncul di SATU kategori:')
print(unik_satu_kategori)

if n > 2:
    tepat_dua_kategori = {app for app, freq in frekuensi_aplikasi.items() if freq == 2}
    print('\nAplikasi yang muncul TEPAT di DUA kategori:')
    print(tepat_dua_kategori)
