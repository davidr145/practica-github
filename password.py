print("el password debe tener entre 6 y 8 caracteres")
print("el password debe cumplir estos requisitos:")
print("el primer valor tiene que estar entre el numero 1 y 5")
print("el segundo valor debe ser una letra mniscula")
print("el tercer valor debe ser una letra mayuscula")
print("el cuarto valor debe ser uno de estos simbolos *, _, @")
print("el quinto valor debe ser una letra miniscula ")
print("el sexto valor tiene que ser un numero mayor o igual a 6 i menor o igual a 9")
print("el septimo valor debe ser uno de los siguienets simbolos &,/ ,#")
print("el  octavo  valor debe ser menor o igual que 5")
#introduce la contraseña
password= input("introduce la contraseña")
#comprobamos
if len(password) < 6 or len(password) > 8:
    print(f"error la contraseña tiene una longitud de {len (password)}")
else:
    if not(password)[0].isdigit():
        print("error en el primer caracter: debe ser un numero entre 1 y 5")
    else:
        if not password[0].isdigit():
            print("Error en el carácter 1: tiene que ser un número.")
        if not password[1].islower():
            print("Error en el carácter 2: tiene que ser una letra minúscula.")
        if not password[2].isupper():
            print("Error en el carácter 3: tiene que ser una letra mayúscula.")
        if password[3] not in '*#/%&':
            print("Error en el carácter 4: tiene que ser uno de estos símbolos: * # / % &.")
        if not password[4].islower():
            print("Error en el carácter 5: tiene que ser una letra minúscula.")
        if not password[5:].isdigit():
            print("Error en los caracteres restantes: tienen que ser números.")
        else:
            print:("el formato es correcto")
    

