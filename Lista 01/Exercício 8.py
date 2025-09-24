km = int(input('''Quantos Km's você percorreu: '''))
dias = int(input('E a quantidade de dias: '))

km_aum = km * 0.15
dia_aum = dias * 60

total = km_aum + dia_aum

print(f'Aluguel por dia: R${dia_aum} e Km rodado: {km_aum}km/h. Então o preço a pagar é: {total}')