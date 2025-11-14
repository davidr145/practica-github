num_numeros=int(input("introduce la cantidad de numeros deseados"))
postivos=0
negativos=0
ceros=0
for i in range(num_numeros):
    numero=float(input("introduce tu numero"))
    if numero>0:
        postivos += 1
    elif numero<0:
        negativos += 1
    else:
        ceros += 1
print(f"la cantidad de positivos es {postivos}")
print(f"la cantidad de negativos es {negativos}")
print(f"la cantidad de ceros es {ceros}")