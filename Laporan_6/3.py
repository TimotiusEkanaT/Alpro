jumlah = int(input("Berapa jumlah mata kuliah? "))
nilaiAkhir = 0
for i in range(1, jumlah+1):
    nilai = input(f"Nilai MK {i}: ")
    nilai = nilai.upper()
    if nilai == "A":
        nilai = 4
    elif nilai == "B":
        nilai = 3
    elif nilai == "C":
        nilai = 2
    elif nilai == "D":
        nilai = 1
    nilaiAkhir += nilai

print(f"Nilai IPS anda semester ini adalah {round((nilaiAkhir/jumlah),2)}")
    