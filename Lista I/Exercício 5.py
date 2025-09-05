merc = float(input('Qual o valor da mercadoria: '))
desc = float(input('Qual o percentual de desconto: '))

total = merc - merc * (desc/100)

print(f'O valor do desconto é: {desc:.0f}% o total a pagar seria de: R${total}')