# Exercício 4
 
number = int(input('Digite um número: '))
fator = []

for i in range(2, number):
    while number % i == 0:
        fator.append(i)
        number = number // i
print(f"Fatores primos: {fator}")