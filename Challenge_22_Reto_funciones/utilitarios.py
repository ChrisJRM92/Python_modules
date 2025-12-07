def calcularPromedio(nota1, nota2, nota3):
    return (nota1+nota2+nota3)/3

def consultarMulta(tipoMulta):
    if(tipoMulta == 1):
        return 10
    elif(tipoMulta == 2):
        return 15
    elif(tipoMulta == 3):
        return  20
    elif(tipoMulta == 4):
        return  30
    else:
        return -1
def calcularValorHora(salario):
    return (salario/160)

def calcularSubtotal(precioProducto, cantidad, porcentajeDescuento):
    subtotalSinDescuento = precioProducto*cantidad
    return (subtotalSinDescuento-(subtotalSinDescuento*porcentajeDescuento)/100)

def calcularValorDescuento(precio, porcentajeDescuento):
    return precio*porcentajeDescuento/100