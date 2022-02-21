palavra1 = input("Entre com a primeira string: ")
palavra1 = palavra1.lower()
palavra2 = input("Entre com a segunda string: ")
palavra2 = palavra2.lower()
caracteres = len(palavra1)
caracteresContados = 0
for i in palavra1:
    if i in palavra2:
        caracteresContados += 1
if caracteresContados == caracteres:
    print("Todos os caracteres da primeira string aparecem na segunda")
else:
    print("Nem todos os caracteres da primeira string aparecem na segunda")
        

