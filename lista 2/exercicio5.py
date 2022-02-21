n = int(input("Entre com o valor de n: "))
contador = 0
j = 2
print(f"Primeiros {n} números primos:")
while contador < n:
    i = 2
    ehPrimo = True
    while i < j:
        if j%i == 0:
            ehPrimo = False
        i+=1
    if ehPrimo == True:
        contador += 1
        print(j)
    j+=1
    
