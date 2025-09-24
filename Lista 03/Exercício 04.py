# EXERCÍCIO 4

num = int(input('Digite um número: '))

a, b = 1, 1
rep = 1

while rep <= num-1:
   a, b = b, a + b

   rep += 1
print(a)