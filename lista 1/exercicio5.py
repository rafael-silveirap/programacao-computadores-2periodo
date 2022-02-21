p1 = float(input("Digite a nota da P1: "))
p2 = float(input("Digite a nota da P2: "))

media1 = (p1 + p2)/2

if(p1 > 10 or p1 < 0):
    print("Nota inválida")
elif(p2 > 10 or p2 < 0):
    print("Nota inválida")
elif(media1 >= 7.0):
    print("Aprovado direto.")
    print("Média final:", media1)
elif(media1 < 4.0):
    print("Reprovado direto.")
    print("Média final:", media1)
else:
    pf = float(input("Digite a nota da PF: "))
    mediaF = (media1 + pf)/2
    if(mediaF >= 6.0):
        print("Aprovado.")
        print("Média final:", mediaF)
    else:
        print("Reprovado.")
        print("Média final:", mediaF)
