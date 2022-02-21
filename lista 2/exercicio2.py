n = int(input("Entre com o número de coordenadas: "))
i = 1
quantidade_positivos = 0 #identificar a quantidade de numeros positivos no vetor
while i <= n:
    coordenada = float(input(f"Entre com a coordenada {i}: "))
    if coordenada > 0:
        quantidade_positivos += 1
    i += 1
if quantidade_positivos == n:
    print("Este vetor se encontra no primeiro ortante")
else:
    print("Este vetor não se encontra no primeiro ortante")
    
