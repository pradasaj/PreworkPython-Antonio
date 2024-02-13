'''
Ejercicio 15: Conversor de Tiempo
 Escribe un programa que convierta un número de minutos en horas y minutos. Por 
ejemplo, 145 minutos serían 2 horas y 25 minutos
'''

minutos = float(input("Introduzca el número de minutos a conventir: "))

horas  = (minutos / 60)//1

minutos_resto = minutos - (horas * 60)

print( "{} minutos son {} horas y {} minutos".format(minutos, horas, minutos_resto))



