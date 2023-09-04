# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def total():
    factura = float(input("Introduce el total de la factura: "))
    IVA = int(input("Ingresa el valor del IVA: "))
    return factura, IVA

factura,IVA = total()

def calcularIVA (factura,IVA):
    if IVA ==0:
        totalFactura= factura*1.21
        print("El total de la factura es: {} y con IVA: {}".format(factura, totalFactura))
    elif IVA < 0:
        print("El monto del iva es negativo, no podemos avanzar")
    else:
        totalFactura= ((factura*IVA)/100) + factura
        print ("El total de la factura es: {} y con IVA: {}".format(factura,totalFactura)) 

calcularIVA(factura,IVA)

        

