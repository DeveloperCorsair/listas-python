# Exercícios by Nick Parlante (CodingBat)
# A. multstring
# seja uma string s e um inteiro positivo n
# retorna uma string com n cópias da string original
# multstring('Hi', 2) -> 'HiHi'
def multstring(s, n):
  return s*n

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('Multstring')
  test(multstring('Hi', 2), 'HiHi')
  test(multstring('Hi', 3), 'HiHiHi')
  test(multstring('Hi', 1), 'Hi')
  test(multstring('Hi', 0), '')
  test(multstring('Hi', 5), 'HiHiHiHiHi')
  test(multstring('Oh Boy!', 2), 'Oh Boy!Oh Boy!')
  test(multstring('x', 4), 'xxxx')
  test(multstring('', 4), '')
  test(multstring('code', 2), 'codecode')
  test(multstring('code', 3), 'codecodecode')
if __name__ == '__main__':
  main()
