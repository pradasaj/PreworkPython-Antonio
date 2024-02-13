'''
Ejercicio 4: Contador de Vocales
 Crea un programa que cuente el número de vocales en una palabra ingresada por el 
usuario.
'''

palabra = input("Teclea una palabra: ")
vocales = "aeiouAEIOU"
c = 0
for i in palabra:
  if i in vocales:
      c = c + 1
print(f"La palabra tiene {c} vocales")
