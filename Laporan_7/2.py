n = int(input("n = "))
bantu = 1
for i in range(n, 0 , -1):
    for j in range(i, 0, -1):
        bantu *= j
    print(bantu, end=" ")
    for j in range(i, 0, -1):
        print(j, end=" ")

    bantu = 1
    print()

