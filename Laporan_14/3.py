def baca_file(filename):
    try:
        with open(filename, 'r') as file:
            isi = file.read()
            kata_list = isi.lower().split()
            return set(kata_list)
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return None
    except IOError:
        print(f"Error: File '{filename}' tidak bisa dibaca.")
        return None

file1 = input("Masukkan nama file pertama: ")
file2 = input("Masukkan nama file kedua: ")

kata_file1 = baca_file(file1)
kata_file2 = baca_file(file2)

if kata_file1 is not None and kata_file2 is not None:
    kata_sama = kata_file1.intersection(kata_file2)
    if kata_sama:
        print("\nKata-kata yang muncul di kedua file:")
        for kata in sorted(kata_sama):
            print(kata)
    else:
        print("\nTidak ada kata yang sama di kedua file.")
