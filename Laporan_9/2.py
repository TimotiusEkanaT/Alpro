def soal(nama_file):
    print("Nama file:", nama_file)
    try:
        with open(nama_file, 'r') as file:
            for line in file:
                if '||' in line:
                    bagian = line.split(' || ')
                    soal = bagian[0]
                    jawaban_benar = bagian[1]

                    if jawaban_benar:
                        jawaban_benar = jawaban_benar.replace('\n', '')
                    if '\n' in soal:
                        soal = soal.replace('\n', '')
                    print(soal)

                    jawaban_user = input("Jawab: ")
                    if jawaban_user.lower() == jawaban_benar.lower():
                        print("Jawaban benar!\n")
                    else:
                        print("Jawaban salah!\n")
    except FileNotFoundError:
        print("File tidak ditemukan.")
        
soal('soal.txt')
