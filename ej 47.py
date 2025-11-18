a = int(input("Introduce el primer intervalo: "))
b = int(input("Introduce el segundo intervalo: "))

if a < b:
    numeros = list(range(a, b + 1))
else:
    numeros = list(range(a, b - 1, -1))

print("-".join(map(str, numeros)))