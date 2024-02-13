'''
 Ejercicio 13: Verificación de Número Primo
 Escribe un programa que determine si un número ingresado por el usuario es primo 
o no'''

n = int(input("Introduzca un número entero: "))

x = 1
c = 0

while x <= n:
  if n % x == 0:
    c = c + 1
  x = x + 1

if c == 2:
  print("El número ",n," ES primo")
else:
  print("El número ",n," NO es primo")
