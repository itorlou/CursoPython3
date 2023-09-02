'''Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras'''

for i in range(1,11):
    print(i)

n=int(input("Dime el principio: "))
m=int(input("Dime el final: "))

for n in range (n,m+1):
    print(n)