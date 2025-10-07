# E. count_hi #
# conta o número de vezes que aparece a string 'hi'
# count_hi('abc hi ho') -> 1
# count_hi('ABChi hi') -> 2
# count_hi('hihi') -> 2
def count_hi(s):
  return s.count('hi')

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
  print ()
  print ('Count_hi')
  test(count_hi('abc hi ho'), 1)
  test(count_hi('ABChi hi'), 2)
  test(count_hi('hihi'), 2)
  test(count_hi('hiHIhi'), 2)
  test(count_hi(''), 0)
  test(count_hi('h'), 0)
  test(count_hi('hi'), 1)
  test(count_hi('Hi is no HI on ahI'), 0)
  test(count_hi('hiho not HOHIhi'), 2)
if __name__ == '__main__':
  main()