# Exercício 2
 
import random
 
quant = 20

numbers = [random.randint(0, 101) for i in range(quant)]
par = []
impar = []

for i in numbers:
    if i % 2 == 0:
        par.append(i)
    if i % 2 == 1:
        impar.append(i)

print(f"Os números da lista são: {numbers}") 
print(f'Os números pares são: {par}')
print(f'Os números ímpares são: {impar}')