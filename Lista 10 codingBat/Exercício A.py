# A. near_ten 
# Seja um n não negativo,
# retorna True se o número está a distância de
# pelo menos dois de um múltiplo de dez.
# near_ten(12) -> True
# near_ten(17) -> False
# near_ten(19) -> True
def near_ten(n):
    r = n % 10
    return r <= 2 or r >= 8

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
  print ('Near_ten')
  test(near_ten(12), True)
  test(near_ten(17), False)
  test(near_ten(19), True)
  test(near_ten(31), True)
  test(near_ten(6), False)
  test(near_ten(10), True)
  test(near_ten(11), True)
  test(near_ten(21), True)
  test(near_ten(22), True)
  test(near_ten(23), False)
  test(near_ten(54), False)
  test(near_ten(155), False)
  test(near_ten(158), True)
  test(near_ten(3), False)
  test(near_ten(1), True)
if __name__ == '__main__':
  main()