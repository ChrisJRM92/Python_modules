def calcularInteresSimple(monto, plazo, tasa):
    return (monto*(tasa/100))*plazo

def calcularInteresCompuesto(monto, plazo, tasa):
    return round((monto*((1+(tasa/100))**plazo))-monto, 4)

def calcularCuota(monto, tasa, plazo):
    r = tasa / 100
    return round(monto*(r*(1+r)**plazo)/((1+r)**plazo-1), 2)