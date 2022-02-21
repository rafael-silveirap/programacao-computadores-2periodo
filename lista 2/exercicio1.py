n = int(input("Entre com a quantidade de termos do produtório: "))
i = 1
produtorio = 1
if n == 0:
    print("Produto dos termos:", n)
else:
    while i <= n:
        termo = float(input(f"Entre com o termo {i} :"))
        produtorio *= termo
        i += 1
    print("Produto dos termos:", produtorio)
