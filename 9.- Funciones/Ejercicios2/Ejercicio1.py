# Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1; si ambos son iguales, debe retornar 0


def pidenumeros():
    num1= int(input("Dime un número:"))
    num2= int(input("Dime el segundo número:"))
    return num1, num2
num1,num2=pidenumeros()
def checkNumeros(num1,num2):
    if num1>num2:
        return 1
    elif num1<num2:
        return -1
    else:
        return 0 
    
print (checkNumeros(num1,num2))
        