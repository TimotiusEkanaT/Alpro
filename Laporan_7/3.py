tinggi = int(input("Tinggi = "))
lebar = int(input("Lebar = "))

a = 1
for i in range(tinggi):
    for j in range(lebar):
        print(a, end=" ")
        a += 1
    print()