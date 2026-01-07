def calcularProbabilidadGanar(lista, cartaMenor, cartaMayor):
    cartaMayorSplit = int(cartaMayor.split("-")[3])
    cartaMenorSplit = int(cartaMenor.split("-")[3])
    aciertos = 0
    numeroCartas = 0

    for carta in lista:
        numeroCartas+=1
        # print(cartaMayorSplit)
        # print(cartaMenorSplit)
        # print(int(carta.split("-")[3]))
        if cartaMenorSplit < int(carta.split("-")[3]) and int(carta.split("-")[3]) < cartaMayorSplit:
            aciertos+=1
    probabilidad = (aciertos/numeroCartas)*100
    return round(probabilidad, 2)