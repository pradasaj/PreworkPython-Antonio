'''
 Ejercicio 19: Verificación de Año Bisiesto
 Escribe un programa que determine si un año ingresado por el usuario es bisiesto o no
'''

año = int(input("Introzuca el año que desea comprobar (formato XXXX): "))

if año % 4 == 0:
  print("El año", año,"SI es bisiesto")

else:
  print("EL año", año,"NO es bisiesto")

