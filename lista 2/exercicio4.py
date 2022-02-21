numero = 1
impar = 0
posicao = 1
while numero >= 0:
    numero = int(input(f"Entre com o número {posicao} do conjunto: "))
    if numero > 0 and numero%2 != 0:
        impar += 1
    posicao += 1

if impar > 0:
    print("Existe número ímpar nesse conjunto")
else:
    print("Não existe número ímpar nesse conjunto")
