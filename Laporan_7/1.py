import math
n = int(input("n = "))

i = n- 1
while i > 1:
    prima = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            prima = False
            break
    if prima:
        print(f"Maka prima terdekat < {n} adalah {i}")
        break
    i -= 1
