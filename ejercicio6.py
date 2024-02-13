'''
Ejercicio 6: Verificación de Palíndromo
 Crea un programa que verifique si una palabra ingresada por el usuario es un 
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda)
'''

palabra = input("Inserta la palabra: ")

if str(palabra) == str(palabra)[::-1]:
  print("Es un palindromo")
else:
  print("No es un palindromo")