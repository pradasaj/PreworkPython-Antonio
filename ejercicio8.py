'''
Ejercicio 8: Cálculo del Índice de Masa Corporal (IMC)
 Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona
 '''

def imc(altura, peso):
  return peso / altura ** 2

peso = float(input("Indique su peso en kg. = "))
altura  = float(input("Indique su altura  en m. =  "))

indice = round(imc(altura, peso),2)

print("Su IMC es: {}".format(indice))