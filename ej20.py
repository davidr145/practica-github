num1 = float (input("introduce un valor (0-10): "))
num2 = float (input("introduce un segundo valor (0-10): "))
if 0 <= num1 <= 10 and 0 <= num2 <= 10:
    if num1 > num2:
        print(f"el {num1} es mayor quee el {num2}")
    elif num2 > num1:
       print(f"el {num2} es mayor quee el {num1}") 
    else:
        print(f"ambos numeros son iguales")
else:
    print(f"uno o los dos numeros son mayores de diez")
    



