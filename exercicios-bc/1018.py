'''Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.'''

num = int(input())
n100 = n50 = n20 = n10 = n5 = n2 = n1 = 0
while num >0:
    if num >= 100:
        n100 = num // 100
        num %= 100
    elif num >= 50:
        n50 = num // 50
        num %= 50
    elif num >= 20:
        n20 = num // 20
        num %= 20
    elif num >= 10:
        n10 = num // 10
        num %= 10
    elif num >= 5:
        n5 = num // 5
        num %= 5
    elif num >= 2:
        n2 = num // 2
        num %= 2
    elif num == 1:
        n1 = 1
        num = 0
print('{} nota(s) de R$ 100,00'.format(n100))
print('{} nota(s) de R$ 50,00'.format(n50))
print('{} nota(s) de R$ 20,00'.format(n20))
print('{} nota(s) de R$ 10,00'.format(n10))
print('{} nota(s) de R$ 5,00'.format(n5))
print('{} nota(s) de R$ 2,00'.format(n2))
print('{} nota(s) de R$ 1,00'.format(n1))
