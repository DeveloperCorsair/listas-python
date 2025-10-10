# C. luck_sum #
# Soma três inteiros a, b, c
# Se aparecer um 13 ele não conta e todos os da
# sua direita também
# lucky_sum(1, 2, 3) -> 6
# lucky_sum(1, 2, 13) -> 3
# lucky_sum(1, 13, 3) -> 1
def lucky_sum(a, b, c):
  y = [a, b, c]
  for i in range(len(y)):
    if a == 13 or b == 13 or c == 13:
      q = y[:13] + y[13+1:]
      return a+b+c - q
    else:
      return 1

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
  print ('Lucky_sum')
  test(lucky_sum(1, 2, 3), 6)
  test(lucky_sum(1, 2, 13), 3)
  test(lucky_sum(1, 13, 3), 1)
  test(lucky_sum(1, 13, 13), 1)
  test(lucky_sum(6, 5, 2), 13)
  test(lucky_sum(13, 2, 3), 0)
  test(lucky_sum(13, 2, 13), 0)
  test(lucky_sum(13, 13, 2), 0)
  test(lucky_sum(9, 4, 13), 13)
  test(lucky_sum(8, 13, 2), 8)
  test(lucky_sum(7, 2, 1), 10)
  test(lucky_sum(3, 3, 13), 6)
if __name__ == '__main__':
  main()