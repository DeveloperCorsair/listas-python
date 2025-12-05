# Exercício 1 
# Explicação
""" Transforma o resto da divisão da variável por dez em string. Após isso, faz a verificação, se a string está próxima dos mútiplos, com a distância máxima de uma unidade, de dez. """

def near_five (n):
    return str(n % 10) in '014'

# Exercício 2
def sanduiche_de_consoantes (s):
    contador = 0
    s = s.lower()
    for i in range(len(s) -2):
        if s[i] not in 'aeiou' and s[i+2] not in 'aeiou':
            contador += 1
        else:
            continue
    return contador
print(sanduiche_de_consoantes('BANANA'))

# Exercício 3
# Explicação 
""" Verifica se existe algum par de números distintos na lista, que sua soma seja igual a 'n'"""

def diferenca_na_lista (n, lista):
    return n in [x - y for x in lista for y in lista if x != y]
print(diferenca_na_lista(1, [1,0,0,1]))


# Exercício 4
#Explicação
""" Retorna uma string, onde todos os caracteres iguais ao primeiro são trocados por '*', com exceção do primeiro que aparecer na string."""

def fixa_ultimo (s):
    return s[:-1].replace(s[-1], '*') + s[-1]
print(fixa_ultimo('arara'))

# Exercício 5
#Explicação
""" Retorna a quantidade de zeros consecultivos que tem no final do número. Caso o número, do indice atual(c), não seja um '0', ele para a função e retorna no contador a quantidade de zeros. """

def soma_impares_finais(n):
    n = str(n) [::-1]
    cont = 0
    for c in n:
        if int(c) % 2 != 0:
            cont += int(c)
        else:
            break
    return cont

# Exercício 6
#Explicação
""" Dentro da função ordena_diferente abre a função last, onde retorna o valor que está no último índice do parâmetro (x). Após isso, volta para a primeira função e retorna os nomes em ordem crescente, de acordo com a última letra da armazenada na função last """

def ordena_por_tamanho(nomes):
    def last(x):
        return len(x)
    return sorted(nomes, key=last)

# Exercício 7
def remove(p):
    return ''.join(set(p))
print(remove('banana'))

# Exercício 8
def inverte(frase):
    frase = frase.split()
    contrario = []
    for i in frase:
        contrario.append(i[::-1])
    return ' '.join(contrario)
print(inverte('python é divertido')) 

#Exercício 9
a = input()
if a > 10 and a % 6 == 3:
    print('A', end = ' ')
elif a > 10 and a < 20:
    print('B', end = ' ')
else:
    print('C', end = ' ')

""" respostas:
ab = n/a
a = 15
b = 12
c = 9
ab = assim que atender a condição de 'A' não vai ser possível atender a condição de 'B'.
feliz natal = não é imprimido, pois não há condição para ele. """