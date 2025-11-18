palabra_secreta = input("Introduce la palabra secreta: ")
longitud = len(palabra_secreta)

for _ in range(longitud):
    letra = input("Introduce una letra: ")
if letra in palabra_secreta:
    print("La letra existe")
else:
    print("La letra no existe")