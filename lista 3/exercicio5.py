vestibulandos = int(input("Entre com o numero de vestibulandos: "))
gabarito = input("Entre com a string do gabarito: ")
i = 1
notas = []
while i <= vestibulandos:
    resposta = input(f"Entre com a resposta do vestibulando {i}: ")
    notaAtual = 0
    for c in range(len(resposta)):
        if resposta[c] == gabarito[c]:
            notaAtual += 1
    notas.append(notaAtual)
    i+=1
menorNota = float("inf")
posicao = 0
for n in notas:
    if n < menorNota:
        menorNota = n
for k in range(len(notas)):
    if notas[k] == menorNota:
        posicao = k+1
print(f"O último colocado foi o vestibulando {posicao} tendo marcado {menorNota} pontos")

