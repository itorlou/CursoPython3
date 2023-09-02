'''Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero'''

num = int(input("Dime un número y te daré la tabla de multiplicar: "))
i = 0

while i < 10:
    i+=1
    print ("{} * {} =".format(num,i),num*i)
    