# EXERCÍCIO 1

nota = int(input('Digite um valor entre 01 e 10: '))

while nota < 1 or nota > 10:
    print('Número inválido. Digite um número entre 01 e 10')   
    nota = int(input('Tente novamente: '))
print('Excelente opção!')