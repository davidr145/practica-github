num_notas=int(input("introduce el numero de notas deseadas:"))
for i in range(num_notas):
    nota=float(input("introduce tu nota"))
    if nota >=5:
        print("estas aprobado")
    else:
        print("no estas aprobado")