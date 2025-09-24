lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if (lado1 >= lado2 + lado3) or (lado2 >= lado1 + lado3) or (lado3 >= lado1 + lado2):
    print('Não pode ser um triângulo')
if lado1 == lado2 and lado1 == lado3 and lado2 == lado3:
    print('Triângulo equilátero')
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print('Triângulo escaleno')
else:
    print('Triângulo isósceles')