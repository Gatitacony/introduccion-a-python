num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("Something else")
#Salida  Three

#Y como se puede ver en el ejemplo anterior, una serie de declaraciones if elif pueden tener un bloque final else, que se llama si ninguna de las expresiones if o elif es True.
num = 8
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("Something else")
#Salida  Somethin else

num = 42 
if num < 0:
    print("Negative")
elif num > 0:
    print("Positive")
else:
    print("Zero")
#Salida  Positive

#Tu programa toma la edad de la persona que intenta entra, y genera "Allowed" si se les permite entrar en el club, y "Sorry" si son menores de la edad permitida.
age = int(input())
if age >=18:
    print("Allowed")
else:
    print("Sorry")
#Entrada 11
#Salida Sorry
#Entrada 42
#Salida Allowed

x = 10

y = 20 

if x > y :

    print(x + y)

else:

    print(y - x)
#Salida  10