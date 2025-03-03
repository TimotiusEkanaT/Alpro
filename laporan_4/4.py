try:
    sisi1 = int(input("Masukkan sisi 1: "))
    sisi2 = int(input("Masukkan sisi 2: "))
    sisi3 = int(input("Masukkan sisi 3: "))

    if sisi1 == sisi2 == sisi3:
        print("3 sama sisi")
    elif sisi1 == sisi2 or sisi2 == sisi3 or sisi1 == sisi3:
        print("2 sama sisi")
    else:
        print("Tidak ada yang sama")
except:
    print("input tidak valid")