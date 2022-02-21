mensagem = input("Entre com a mensagem: ")
mensagemNova = ""
for i in mensagem:
    if i.isalpha():
        x = ord(i)
        if x == 65:
            mensagemNova += chr(90)
        elif x == 97:
            mensagemNova += chr(122)
        else:
            mensagemNova += chr(x - 1)
    else:
        mensagemNova += i
print(mensagemNova)
