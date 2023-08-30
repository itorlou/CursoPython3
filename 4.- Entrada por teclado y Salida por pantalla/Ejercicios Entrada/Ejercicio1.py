'''Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”'''

from math import sqrt # importamos sqrt (para raíces cuadradas) de la librería math

A = int(input("Introduce el valor de A:"))
B = int(input("Introduce el valor de B:"))
C = int(input("Introduce el valor de C:"))

x1=0
x2=0

if (((B**2)-(4*A*C)) < 0 ):
    print ("No se puede sacar raíz a un número negativo")
else:
    x1= (-B + sqrt((B**2)-(4*A*C)))/(2*A)
    x2= (-B - sqrt((B**2)-(4*A*C)))/(2*A)
    print ("La solución es : X1= ",x1," ,X2=",x2)



 
