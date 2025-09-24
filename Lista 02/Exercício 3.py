quilo = int(input('Quilo: '))

if quilo > 50:
    excesso = quilo - 50
    multa = excesso * 4
    
    print(f'Peso excedido, MULTADO em R${multa:.2f}')
else:
    print(f'Multa: {0:.2f}')