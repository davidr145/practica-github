import math
a = float(input("introduce el coeficiente a: "))
b = float (input("introduce el coeficiente b: "))
c = float (input("intrduce el coeficiente c: "))
discriminante = b**2 - 4*a*c
if discriminante < 0:
    print("la raiz no  puede ser negativa")
else:
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    print(f"el valor de x1 es {x1}")
    print(f"el valor de x2 es {x2}")
    