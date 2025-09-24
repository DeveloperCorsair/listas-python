# EXERCÍCIO 5

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while num2 != 0:
    resto = num1 % num2
    num1 = num2
    num2 = resto
print(f'O MDC é: {num1}')