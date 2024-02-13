'''
Ejercicio 12: Calculadora de Área de un Rectángulo
 Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la 
longitud y el ancho del rectángulo
'''

lon = float(input("Introduzca la longitud del rectágulo en cm: "))
ancho = float(input("Introduzca el ancho del rectágulo en cm: "))

area = lon * ancho

print("El area de un rectágulo de {} por {} es {} cm2".format(lon, ancho, area))