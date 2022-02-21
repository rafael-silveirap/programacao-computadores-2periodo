palavra = input("Entre com a string: ")
palavra = palavra.lower()
palavraModificada = ""
for i in range(len(palavra)):
    letra = palavra[i].isalpha()
    if letra == True:
        if palavra[i] in "aeiou":
            palavraModificada += "*"
        else:
            palavraModificada += "+"
    else:
        palavraModificada += "!"
print(palavraModificada)
        
