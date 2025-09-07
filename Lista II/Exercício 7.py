metro = int(input('Tamanho em M²: '))

tinta = int(metro / 3)

lata = int(tinta / 18)
if tinta % 18 != 0:
    lata += 1
preco = lata * 80

print(f'A quantidade de latas a serem compradas são: {lata} Preco: R${preco:.2f}')