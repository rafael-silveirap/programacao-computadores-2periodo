peso = float(input("Entre com o peso: "))
altura = float(input("Entre com a altura: "))
imc = peso/(altura**2)
print(imc)
if(imc < 18.5):
    print("Condição: abaixo do peso")
elif(18.5 <= imc < 25):
    print("Condição: peso normal")
elif(25 <= imc < 30):
    print("Condição: sobrepeso")
else:
    print("Condição: obeso")
