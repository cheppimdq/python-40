# Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor.
# Considerar el caso en que ambos números son iguales.

nro_1= int(input("Ingrese un nro "))
nro_2= int(input("Ingrese otro nro "))
if nro_1 < nro_2:
    print("El primero es menor")
elif nro_2 < nro_1:
    print("El segundo es menor")
else:
    print("Los nros son iguales")