'''
 Ejercicio 16: Contador de Números Pares e Impares
 Crea un programa que cuente y muestre la cantidad de números pares e impares en 
una lista ingresada por el usuario
'''

numeros = []
for x in range(5):
  valor = int(input("Insertar cinco valores enteros: "))
  numeros.append(valor)

par = 0
impar = 0
for x in numeros:
  if x % 2 == 0:
    par = par + 1
  else:
    impar = impar + 1

print("Tenemos {} números pares".format(par))
print("Tenemos {} números impares".format(impar))

