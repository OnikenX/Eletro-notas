def calcRth(resistencias):
    sum_das_resistencias_invertidas = 0
    for resistencia in resistencias:
        sum_das_resistencias_invertidas += 1/resistencia
    return 1/sum_das_resistencias_invertidas
