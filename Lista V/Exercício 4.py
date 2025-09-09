#Exercício 4

# Para retornar apenas 2, tirar o segundo for e, vice-versa
for i in range(18644, 33087):
    if '2' in str(i) and '7' not in str(i):
        print('número com 2 e sem 7:',i)