soma = 0
escolha = 1
while escolha == 1:
    numero = int(input("Entre com o número: "))
    n = numero
    while n > 0:
        digito = n%10
        n = n//10
        soma += digito**3
    if soma == numero:
        print(f"{numero} é um número de Armstrong")
    else:
        print(f"{numero} não é um número de Armstrong")

    escolha = int(input("Deseja executar o programa novamente? (0 - Não) (1 - Sim): "))
print("Tenha um bom dia!")
