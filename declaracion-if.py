#Ejemplo de una declaración if en acción:
x = 42
if x > 5:
    print("x es mayor que 5")
#Salida  x es mayor que 5

spam = 7
if spam > 5:
    print("cinco")
if spam > 8:
    print("ocho")
#Salida  cinco

age = 24
if age > 18:
    print("Cool")
#Salida  Cool

x = 8
y = 42 
if x > y:
    print("x es mayor que y")
#Salida  no aparece nada porque no es mayor que y

#Las declaraciones if pueden estar anidados, uno dentro de otro. 
#Por ejemplo:
num = 12 
if num > 5:
    print("Más grande que 5")
    if num <= 47:
        print("Entre 5 y 47")
#Salida  Más grande que 5
#        Entre 5 y 47

num = 7
if num > 3: 
    print("3")
    if num < 5: 
        print("5")
        if num == 7:
            print("7")
#Salida  3

#Programa que compruebe si el agua está hirviendo. Toma la temperatura entera en Celsius como entrada y genera "boiling" si la temperatura es superior o igual a 100.
temp = int(input())
if temp >= 100:
    print("Boiling")
#Entrada 132
#Salida
#  Boiling
#Entrada 76 
#Sin salida

x = 'a'
if x < 'c':
    x += 'b'
if x > 'z':
    x += 'c'

print(x)
#Salida  ab

#Programa para tomar la edad(age) de los pasajeros como entrada y generar 'Take your kindle!' si la edad es menor o igual a 19 años.
age = int(input())
if age <= 19:
    print("Take your kindle!")
#Entrada 19
#Salida
# Take your kindle!
#Entrada 24 
#Sin salida.

