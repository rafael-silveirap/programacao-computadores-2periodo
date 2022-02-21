def pontuacao(resposta, gabarito):
    letrasIguais = 0
    for i in range(len(resposta)):
        if resposta[i] == gabarito[i]:
            letrasIguais += 1
    return letrasIguais
