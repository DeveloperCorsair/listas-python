dia = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
mi = int(input('Digite a quantidade de minutos: '))
seg = int(input('Digite a quantidade de segundos: '))

total = dia*86400 + horas*3600 + mi*60 + seg

print(f'O total de segundos é: {total:.2f}')