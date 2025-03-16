def perkalian (a,b):
    print(f"{a} x {b} = ", end="")
    for i in range (1, a+1):
        if i == a:
            print(b, end = "")
        else:
            print(b, end = " + ")
    print(f" = {a*b}")

perkalian(6,5)