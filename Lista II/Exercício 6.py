ganho = float(input('Quanto você ganha por hora: '))
hora = int(input('Quantas horas você trabalhou: '))

sal = ganho * hora

liq = sal * (0.11 + 0.08 + 0.05)

print(f'Salário bruto: {sal}')