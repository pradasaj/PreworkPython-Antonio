'''
Ejercicio 20: Suma de Números en una Lista
 Crea un programa que sume todos los números en una lista ingresada por el usuario.
'''

numeros = []
for x in range(5):
  valor = float(input("Insertar cinco números: "))
  numeros.append(valor)

print("La suma de los cinco números introducidos es: ",sum(numeros))

