def semua_sama(t):
    for x in t:
        if x != t[0]:
            return False
    return True

data = (90, 90, 90, 90)
if semua_sama(data):
    print("Semua anggota tuple sama")
else:
    print("Ada anggota tuple yang berbeda")