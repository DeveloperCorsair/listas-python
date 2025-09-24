#Exercício 2

conta = int(input('Valor: '))
pag = int(input('Quanto: '))

troco = pag - conta

if conta <= 0:
    print('Não pode ser zero ou negativo!')
elif troco == 0:
    print('Não há troco.')
elif conta > pag:
    print('Valor insuficiente para pagar a conta!')
else:
    notas = [50, 20, 10, 5, 2, 1]

    for i in notas:
        pagar_troco = troco // i 
        
        if pagar_troco > 0:
            print(f'{pagar_troco} nota(s) de {i}')
            troco -= pagar_troco * i