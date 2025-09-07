# Exercício 3

primo = int(input('Digite: '))

if primo <= 1:
    print('Não é um número primo. O número preciso ser positivo!')
else:
    for i in range(2, primo):
        if primo % i == 0:
            print('Não é um número primo')
            break
    else:
        print('É um número primo')