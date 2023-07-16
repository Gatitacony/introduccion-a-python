spam = "7"
spam = spam + "0"
eggs = int(spam) + 3
print(float(eggs))
#Salida  73.0

print("---------------------------")

#Si el usuario introduce 42
age = int(input())
print(age + 8)
#Salida  50

print("--------------------------------")

x = 5 
y = x + 3
y = int(str(y) + "2")
print(y)
#Salida  82

print("--------------------------------")

x = 4
x += 5 
print(x)
#Salida  9

print("----------------------------")

x = 3
num = 17 
print(num % x)
#Salida  2

print("-----------------------")

name = input()
print("Welcome, "+ name)
#Salida  Welcome, Franciny

print("-----------------------")

#Calculadora de propinas 
bill = float(input())
print(bill * 20 / 100)
