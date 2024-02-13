'''
 Ejercicio 9: Conversor de Divisas
 Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que 
1 dólar es igual a 0.85 euros
'''

def conversion(dolares, tipo_cambio):
    return dolares * tipo_cambio

dolares = float(input("Ingresa la cantidad de US Dollar a convertir en Euros: "))
tipo_cambio = 0.85

print(dolares, "US Dollar *", "tipo de cambio", tipo_cambio, "=", round(conversion(dolares, tipo_cambio),2), "Euros")
