# Exercício 1
 
import random
 
quant = 10
number = [random.randint(1, 101) for i in range(quant)]
 
menor = 101
maior = 0
 
for valor in number:
    if valor < menor:
        menor  = valor
    if valor > maior:
        maior = valor

print(f"Os números da lista são: {number}") 
print(f'O menor valor da sequência é: {menor}')
print(f'O maior valor da sequência é: {maior}')