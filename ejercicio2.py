entero_positivo = int(input("Introduce un entero positivo: "))
suma = 0
for i in range(1, entero_positivo + 1):
    suma += i
print("La suma de los enteros desde 1 hasta", entero_positivo, "es:", suma)