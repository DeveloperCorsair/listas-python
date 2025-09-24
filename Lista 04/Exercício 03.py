# Exercício 3
 
import random
 
primeiro = [random.randint(0, 101) for i in range(10)]
segundo = [random.randint(0, 101) for i in range(10)]
numbers = []

for i in zip(primeiro, segundo):
    numbers.append(i)

print(f'Os números pares são: {primeiro}')
print(f'Os números ímpares são: {segundo}')
print(f"Os números da lista são: {numbers}") 