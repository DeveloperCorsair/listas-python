# EXERCÍCIO 2

nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')

while senha == nome:
   print('Sua senha não pode ser ter o mesmo nome de seu usuário! Tente novamente')
   nome = str(input('Digite seu nome: '))
   senha = str(input('Digite sua senha: '))
print('Tudo certo!')
