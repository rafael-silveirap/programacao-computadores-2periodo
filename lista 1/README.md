# Lista 1
## Exercício 1
Escreva um programa que leia um número inteiro positivo do teclado e informe se ele é múltiplo de 3. <br>
Exemplos:
```
Digite um numero: 9
Esse número é multiplo de três!
```
```
Digite um numero: 17
Esse número não é multiplo de três!
```

## Exercício 2
O Índice de Massa Corporal (IMC) de uma pessoa é calculado segundo a fórmula: <br> <br>
<p align="center"><img src="https://media.discordapp.net/attachments/780042178424471583/945395749733142608/751211349627109416.png" width="200"></p> <br>

Em outras palavras, o IMC é uma razão entre o peso de um indivíduo eo quadrado de sua altura. A partir do cálculo do IMC, a Organização Mundial de Saúde define a condição referente ao peso de um adulto de acordo com a seguinte tabela: <br> <br>

<p align="center"><img src="https://media.discordapp.net/attachments/859912057163874315/945397258709508166/unknown.png" width="400"></p> <br>

Escreva um programa em Python que leia o peso de uma pessoa e a sua respectiva altura e informe seu IMC juntamente com a sua devida condição de acordo com a tabela acima.<br>
Exemplos:
```
Entre com o peso: 54
Entre com a altura: 1.71
IMC: 18.467220683287167
Condição: abaixo do peso
```
```
Entre com o peso: 65
Entre com a altura: 1.75
IMC: 21.224489795918366
Condição: peso normal
```

## Exercício 3
Escreva um programa que leia as coordenadas do centro de um círculo (em um plano cartesiano) juntamente com o seu raio, e então informe se um determinado ponto de teste lido está dentro do círculo, no centro do círculo, na circunferência (fronteira) ou fora do círculo. Assuma que não ocorrem erros de arredondamento nos cálculos e que o usuário sempre fornece valores válidos. Apenas para lembrar, a equação da circunferência é dada por: <br>

<p align="center"><img src="https://media.discordapp.net/attachments/780042178424471583/945643298159226890/751211349627109416.png?width=1440&height=232" width="250"></p>

Onde *(xc, yc)* são as coordenadas do centro da circunferência e *r* é o raio. Lembre-se de que seu programa deve informar em qual das *quatro* categorias está o ponto de teste. <br>

Exemplos:

```
Digite a coordenada x do centro do circulo: 10
Digite a coordenada y do centro do circulo: 5
Digite o raio do circulo: 4

Digite a coordenada x do ponto de teste: 9
Digite a coordenada y do ponto de teste: 6

O ponto de teste está dentro do circulo
```
```
Digite a coordenada x do centro do circulo: 1
Digite a coordenada y do centro do circulo: 2
Digite o raio do circulo: 5

Digite a coordenada x do ponto de teste: 1
Digite a coordenada y do ponto de teste: 2

Ponto de teste está no centro do circulo
```

## Exercício 4

A *Bachatóvia* adota a Tabela abaixo para o cálculo do seu imposto de renda. Faça um programa que peça a renda anual de um contribuinte e calcule o seu devido imposto, de acordo com a tabela.

<p align="center"><img src="https://media.discordapp.net/attachments/859912057163874315/946018813311332392/unknown.png" width="550"></p>

Exemplos:

```
Digite a sua renda anual: -20
Renda invalida!
```
```
Digite a sua renda anual: 21451
Imposto: 3117.78
```

Obs: note que, no exemplo acima os 28% foram calculados sobre o valor da renda que ultrapassou 21450. Assim, o imposto foi de 3117,50 + 28%(21451 - 21450) = 3117,78 . O mesmo vale para o exemplo abaixo, em sua respectiva categoria.

```
Digite a sua renda anual: 52000
Imposto: 11774.0
```

## Exercício 5

Faça um programa para calcular a média final de um aluno da matéria de Abstração I da Universidade da Bachatóvia. As provas dessa universidade são pontuadas de 0 a 10, podendo haver casas decimais nas notas. A média final deve ser calculada segundo as regras abaixo:

- O programa deve receber inicialmente dois números representando as notas da Prova 1 (P1) e da Prova 2 (P2) do aluno. Se a média M1 for maior ou igual que 7,0, o aluno estará aprovado direto. Se essa mesma média for menor que 4,0, o aluno estará reprovado direto. Nesses dois casos, esta média M1 será a média final do aluno.
- Caso a média M1 do aluno fique entre 4,0 e 7,0, o aluno deve realizar uma Prova Final (PF). Apenas nesse caso, o programa deverá pedir também a nota da PF. A média final MF será então calculada. Para este último caso, se MF for maior ou igual que 6,0, o aluno estará aprovado. Caso contrário, estará reprovado.

Considere:


<p><img src="https://media.discordapp.net/attachments/780042178424471583/945648150742458388/751211349627109416.png" width="250"></p>
<p><img src="https://media.discordapp.net/attachments/780042178424471583/945648336222978048/751211349627109416.png" width="250"></p>








