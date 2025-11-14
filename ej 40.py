pares = 0
impares = 0

for num in range(50):
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"El total de pares es: {pares}")
print(f"El total de impares es: {impares}")