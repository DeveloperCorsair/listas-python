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
        if int(n) % 2 != 0:
            cont += int(n)
        else:
            break
    return cont