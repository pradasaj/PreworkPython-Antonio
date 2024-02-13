'''
Ejercicio 5: Suma de Números Pares
 Escribe un programa que calcule la suma de todos los números pares del 1 al 100
'''

num=0

num_obtenidos=[]

while num < 100:
    num+=2
    num_obtenidos.append(num)

listSum = sum(num_obtenidos)

print(f"Suma de todos los números pares del 1 al 100 -> {listSum}")