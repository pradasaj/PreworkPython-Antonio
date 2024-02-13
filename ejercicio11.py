'''
Ejercicio 11: Calculadora de Edad
 Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad 
actual
'''

año = int(input("Introduzca el año actual en formato XXXX :" )) 
nac = int(input("Introduzca su año de nacimiento en formato XXXX : "))

edad = año - nac

print("Su edad es ", edad," años")
