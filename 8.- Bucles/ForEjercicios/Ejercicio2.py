'''Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero, solo imprimiendo los números que sean impares'''

n=int(input("Dime el principio: "))
m=int(input("Dime el final: "))

for n in range(n,m+1):
    if n%2==0:
        continue
    print(n)