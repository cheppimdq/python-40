# El empleado cobró 300 desde enero a junio, 500 de julio a octubre, y 700 en noviembre y en diciembre. En base al escenario propuesto, creen un pequeño programa que calcule el sueldo promedio del empleado. indicar sí se encuentra cobrando un sueldo bajo, normal o mejor de lo normal: Sueldo bajo: debajo de 300 dólares. Sueldo normal: entre 300 a 900. Sueldo mejor de lo normal: más de 900 dólares.

mensualidades = [300, 300, 300, 300, 300, 300, 500, 500, 500, 500, 700, 700] # SUELDOS
sueldo_promedio = sum(mensualidades) / len(mensualidades) # PROMEDIO

# ESCALA
if sueldo_promedio < 300:
    clasificacion = "Sueldo bajo"
elif sueldo_promedio <= 900:
    clasificacion = "Sueldo normal"
else:
    clasificacion = "Sueldo mejor de lo normal"

print(f"Sueldo promedio: {sueldo_promedio:.2f} dólares")
print(f"Escala salarial: {clasificacion}")