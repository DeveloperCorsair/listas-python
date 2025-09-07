# Exercício 1
 
numero = int(input('Digite um número: '))
 
for i in range(1, numero + 1):
    p = i * (i + 1) // 2 
    if p == numero:
        print('É um número triangular!')
        break
    elif p > numero:
        print('NÃO é um número triangular.')
        break
else:
    print('NÃO é um número triangular.')