#Exercício 3 

quant = 1

for i in range(1067, 3627):
    if i % 2 == 0:
        # print(i) para mostrar quais são os números pares e divsiveis por 7
        while i % 7 == 0:            
            print(f'{quant}')
            quant += 1
            break