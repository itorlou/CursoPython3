'''Se desea tener un algoritmo que permita determinar y mostrar el promedio que ha obtenido un alumno en un determinado curso, conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:

PP = ( P1 + P2 +P3 ) / 3 PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas

PP: promedio de práctica

PROM: promedio

EP: examen parcial

EF: examen final'''

P1 = float(input("Introduce el valor de Práctica1: "))
P2 = float(input("Introduce el valor de Práctica2: "))
P3 = float(input("Introduce el valor de Práctica3: "))

EP = float(input("Introduce el valor de Examen Parcial: "))
EF = float(input("Introduce el valor de Examen Final: "))

PP = ( P1 + P2 +P3 ) / 3

PROM = ( PP + 2*EP + 3*EF ) / 6

print ("El promedio del alumno es: ",PROM)
