# Escribir un programa que pida al usuario dos números y devuelva su división.
# Si el usuario no introduce números debe devolver un aviso de error y si el divisor es cero también.

nro1 = int(input("ingrese dividendo"))
nro2 = int(input("ingrese divisor"))
if nro2 == 0:
    print("no se puede dividir por 0")
else:
    print(nro1/nro2)