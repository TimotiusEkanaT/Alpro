def tiga_terbaik(data):
    data.sort()
    data.reverse()
    print("Tiga nilai terbaik adalah:", data[:3])

data = [10, 5, 20, 8, 15]
tiga_terbaik(data)