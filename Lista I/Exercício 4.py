sal = float(input('Seu salário: '))
aum = float(input('Porcentagem de aumento: '))

novo = sal + sal * (aum/100)

print(f'O valor do aumento do salário é: {aum} e o novo salário fica: {novo}')