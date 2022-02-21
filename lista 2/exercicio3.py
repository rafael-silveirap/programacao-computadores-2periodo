x = float(input("Digite a coordenada x do centro do círculo: "))
y = float(input("Digite a coordenada y do centro do círculo: "))
raio = float(input("Digite o raio do círculo: "))

x_teste = float(input("Digite a coordenada x para o teste: "))
y_teste = float(input("Digite a coordenada y para o teste: "))

distancia = ((x - x_teste)**2 + (y - y_teste)**2)**(0.5)
if(distancia == 0):
    print("O ponto de teste é o centro do círculo")
elif(distancia == raio):
    print("O ponto de teste está na circunferência")
elif(distancia < raio):
    print("O ponto de teste está dentro do círculo")
else:
    print("O ponto de teste está fora do círculo")
