dia = int(input('A quantidade de cigarros por dia: '))
ano = int(input('A quantidade de anos: '))

cig = dia * 365 * ano
vida = cig * 10
perca = vida / 1440

print(f'A quantidade de dias de vida perdidos são: {perca:.2f}')