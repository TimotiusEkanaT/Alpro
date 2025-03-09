def cek_angka(a, b, c):
    if a == b or a == c or b == c:
        return False
    elif a + b == c or a + c == b or b + c == a:
        return True
    else:
        return False

print(cek_angka(4, 5, 9))
print(cek_angka(1, 4, 1))
print(cek_angka(3, 5, 1))