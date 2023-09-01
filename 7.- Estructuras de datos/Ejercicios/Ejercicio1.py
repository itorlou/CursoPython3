'''Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla'''

meses = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

numMes=int(input("Dime el número del mes del año y te diré su nombre: "))-1


print("El mes es: "+meses[numMes])
