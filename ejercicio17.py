'''
 Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo 
que 1 milla equivale a 1.60934 kilómetros.
'''


km = round(float(input("Introduzca los kilómetros que quiera convertir en millas: ")),2)

milla = round(1.60934 * km,2)

print(km,"kilometros son",milla,"millas")

