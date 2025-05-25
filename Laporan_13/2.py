def data_diri():
    data = ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')
    nim = data[1]
    nama = data[0]
    alamat = data[2]

    nim_tuple = tuple(nim)
    nama_depan = nama.split()[0]
    nama_depan_tuple = tuple(nama_depan)
    nama_terbalik = tuple(nama.split()[::-1])
    print(f'NIM: {nim}\nNAMA: {nama}\nALAMAT: {alamat}')
    print(f'NIM: {nim_tuple}')
    print(f'NAMA DEPAN: {nama_depan_tuple}')
    print(f'NAMA TERBALIK: {nama_terbalik}')

data_diri()