'''
Ejercicio 14: Calculadora de Descuento
 Crea un programa que calcule el precio final de un artículo después de aplicar un 
descuento del 20%
'''

precio = float(input("Introduzca el precio normal del artículo en euros: "))

precio_final =round(precio * 0.8, 2) 

print("El precio final (20% de descuento) del artículo es: {} eur".format(precio_final))