'''
Ejercicio 18: Contador de Palabras
Crea un programa que cuente la cantidad de palabras en una oración ingresada por 
el usuario
'''

oracion = str(input("Escriba una frase: "))

palabras = oracion.split()
num_palabras = len(palabras)

print("La oración introducida tiene {} palabras".format(num_palabras))

