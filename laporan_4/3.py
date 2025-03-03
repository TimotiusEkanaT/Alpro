try:
    bulan = int(input("Masukkan bulan: "))
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        print("Jumlah hari :", 31)
    elif bulan in [4, 6, 9, 11]:
        print("Jumlah hari :", 30)
    elif bulan == 2:
        print("Jumlah hari :", 29)
except:
    print(" bulan yang diinputkan oleh pengguna tersebut tidak valid")