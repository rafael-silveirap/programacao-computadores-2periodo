# Lista 1
## Exercício 1
Escreva um programa que leia um conjunto de números (termos) do teclado e imprima o produto de todos esses números. Antes de começar a ler os números, o programa deve solicitar o total de termos que o usuário pretende entrar. Não se esqueça de que um produtório de 0 termos deve resultar em **zero**.

Exemplos:

```
Entre com a quantidade de termos do produtorio: 2
Entre com o termo 1: 3
Entre com o termo 2: -6
Produto dos termos: -18.0
```
```
Entre com a quantidade de termos do produtorio: 3
Entre com o termo 1: 7
Entre com o termo 2: 0.2
Entre com o termo 3: 10
Produto dos termos: 14.0
```
```
Entre com a quantidade de termos do produtorio: 0
Produto dos termos: 0.0
```

## Exercício 2
Escreva um programa que leia um vetor de n coordenadas e informe se o vetor se encontra no primeiro ortante (ortante positivo). Nota: um vetor se encontra no ortante positivo se **todas** as suas coordenadas são números positivos.

Exemplos:

```
Entre com o numero de coordenadas: 4

Entre com a coordenada 1: 6
Entre com a coordenada 2: 5.3
Entre com a coordenada 3: -7
Entre com a coordenada 4: 12.34

Este vetor não se encontra no primeiro ortante.
```
```
Entre com o numero de coordenadas: 5

Entre com a coordenada 1: 8
Entre com a coordenada 2: 99.99
Entre com a coordenada 3: 2.008
Entre com a coordenada 4: 1
Entre com a coordenada 5: 37.8

Este vetor se encontra no primeiro ortante.
```

## Exercício 3
Um número de Armstrong N de três dígitos é um número que tem a seguinte propriedade:

<p align="center"><img src="https://media.discordapp.net/attachments/780042178424471583/946193523579944980/751211349627109416.png" width = "250"></p>

onde C, D e U são, respectivamente, as centenas, as dezenas e as unidades do número N. Por exemplo, o número 720 não é de Armstrong, pois 7³ + 2³ + 0³ = 351 e 351 é diferente de 720. Já o número 153 é de Armstrong, pois 1³ + 5³ + 3³ = 153. Faça um programa que leia um númerodo teclado e diga se esse número é ou não de Armstrong. Assuma que o usuário sempre fornecerá números inteiros de três algarismos decimais como entrada. Ao final da execução, seu programa deve perguntar ao usuário se ele deseja executar o programa novamente. Se o usuário entrar com o número zero, ele estará dizendo que não, e se entrar com qualquer outro número, estará dizendo que sim. Neste último caso, seu programa deve solicitar novamente a entrada e executar até o usuário não querer mais. 

Veja o exemplo:

```
Entre com um número: 829
829 não é numero de Armstrong.

Deseja executar o programa novamente? (0 - Não) (1 - Sim): 1

Entre com um numero: 153
153 é numero de Armstrong.

Deseja executar o programa novamente? (0 - Não) (1 - Sim): 1

Entre com um numero: 720
720 não é numero de Armstrong.

Deseja executar o programa novamente? (0 - Não) (1 - Sim): 1

Entre com um numero: 407
407 é numero de Armstrong.

Deseja executar o programa novamente? (0 - Não) (1 - Sim): 0

Tenha um bom dia!

```
