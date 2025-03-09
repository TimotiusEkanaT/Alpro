fahrenheit = lambda f: "F = " + str(int((9/5)*f + 32))
reamur = lambda r: "R = " + str(int(0.8*r))


print(fahrenheit(100)) 
print(reamur(80))
print(fahrenheit(0))