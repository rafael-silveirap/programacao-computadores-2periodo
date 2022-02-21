renda = float(input("Digite a renda anual: "))
if(renda <= 0):
    print("Renda inválida")
elif(0 < renda <= 21450):
    imposto = renda*0.15
    print("Imposto:", imposto)
elif(21450 < renda <= 51900):
    imposto = 3117.50 + 0.28*(renda - 21450)
    print("Imposto:", imposto)
else:
    imposto = 11743 + 0.31*(renda - 51900)
    print("Imposto:", imposto)
