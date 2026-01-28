LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE" # Cadena de letras para calcular el DNI
def calcular_letra(numero_dni):
    """Calcula la letra del DNI a partir del número."""
    try:
        numero = int(numero_dni)
        if len(numero_dni) != 8:
            return 0 # Código 0: longitud incorrecta
        resto = numero % 23 # El resto de la división entre 23 determina la letra
        return LETRAS_DNI[resto]
    except ValueError:
        return 1 # Código 1: no es numérico
    except IndexError:
        return 2 # Código 2: resto no aparece en la tabla (situación de error teórica)

LISTA_INTENTOS = [] # Lista para almacenar códigos de intento (0, 1, 2, 3)
DNI_CORRECTOS = [] # Lista para DNI completos correctos
DNI_INCORRECTOS = [] # Lista para DNI completos incorrectos

while True:
    dni_input = input("Introduce un número de DNI (o 'n' para salir): ")
    if dni_input.lower() == 'n':
        break # Salir del bucle si se introduce 'n'

    # Calcular la letra y validar el DNI
    resultado_letra = calcular_letra(dni_input)
   
    if isinstance(resultado_letra, str):
        # Es una letra válida, el DNI es correcto (código 3)
        dni_completo = f"{dni_input}-{resultado_letra}" # Formato: 11111111-R
        print(f"El NIF completo es: {dni_completo}")
        LISTA_INTENTOS.append(3)
        DNI_CORRECTOS.append(dni_completo)
    else:
        # Es un código de error (0, 1, 2)
        if resultado_letra == 0:
            print("Error: El DNI no cumple con la longitud correcta (8 dígitos).")
        elif resultado_letra == 1:
            print("Error: El valor introducido no es numérico.")
        elif resultado_letra == 2:
            print("Error: El resto obtenido no aparece en la tabla.")
        LISTA_INTENTOS.append(resultado_letra)
        DNI_INCORRECTOS.append(dni_input)

print("\n--- MENÚ DE RESULTADOS ---")

# Ordenar listas
DNI_CORRECTOS.sort()
DNI_INCORRECTOS.sort()

# Calcular estadísticas
total_intentos = len(LISTA_INTENTOS)
total_correctos = len(DNI_CORRECTOS)
total_errores = total_intentos - total_correctos
perc_correctos = (total_correctos / total_intentos) * 100 if total_intentos > 0 else 0
perc_incorrectos = (len(DNI_INCORRECTOS) / total_intentos) * 100 if total_intentos > 0 else 0
perc_error_longitud = (LISTA_INTENTOS.count(0) / total_intentos) * 100 if total_intentos > 0 else 0
perc_error_numerico = (LISTA_INTENTOS.count(1) / total_intentos) * 100 if total_intentos > 0 else 0
perc_error_inexistente = (LISTA_INTENTOS.count(2) / total_intentos) * 100 if total_intentos > 0 else 0

# Visualizar la información
print(f"1. Listar DNI correctos ordenados: {DNI_CORRECTOS}")
print(f"2. Listar DNI incorrectos ordenados: {DNI_INCORRECTOS}")
print(f"3. Número total de errores: {total_errores}")
print(f"4. Número total de DNIs correctos: {total_correctos}")
print(f"5. Porcentajes:")
print(f"   Correctos: {perc_correctos:.2f}%")
print(f"   Incorrectos totales: {perc_incorrectos:.2f}%")
print(f"   Errores de longitud: {perc_error_longitud:.2f}%")
print(f"   Errores de número: {perc_error_numerico:.2f}%")
print(f"   Errores de inexistencia (teórico): {perc_error_inexistente:.2f}%")
print("programa finalizado")

