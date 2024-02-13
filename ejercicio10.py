'''
Ejercicio 10: Determinar el Día de la Semana
 Escribe un programa que determine el día de la semana correspondiente a un 
número ingresado por el usuario (1 para lunes, 2 para martes, etc.)
'''

dia = int(input("Que día es hoy (numérico de 1 a 7) = "))

if dia == 1:
    print("Hoy es lunes")
elif dia == 2:
    print("Hoy es martes")
elif dia == 3:
    print("Hoy es miércoles")
elif dia == 4:
    print("Hoy es jueves")
elif dia == 5:
    print("Hoy es viernes")
elif dia == 6:
    print("Hoy es sabado")
else:
    print("Hoy es domingo")