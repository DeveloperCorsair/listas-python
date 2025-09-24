ano = int(input('Escolha um ano: '))

if ano % 4 == 0 and ano % 100 != 0:
    print('É um ano bissexto')
elif ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0:
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')

# Ou pode fazer de outra forma, deixando o código mais limpo

ano = int(input('Ano: '))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('É um ano bissexto')
else:
    print('Não é um ano bissexto')