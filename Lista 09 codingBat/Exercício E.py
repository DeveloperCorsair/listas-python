# E. sum2 #
# Dada uma lista de inteiros de qualquer tamanho
# retorna a soma dos dois primeiros elementos
# se a lista tiver menos de dois elementos, soma o que for possível
def sum2(nums):
  return [nums[0] if len(nums) < 2 else nums[0] + nums[1] for i in range(len(nums))]

  for i in range(len(nums)):
    if len(nums) < 2:
      return nums[0] + i
    else:
      return nums[0] + nums[1]

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
  print ('sum2')
  test(sum2([1, 2, 3]), 3)
  test(sum2([1, 1]), 2)
  test(sum2([1, 1, 1, 1]), 2)
  test(sum2([1, 2]), 3)
  test(sum2([1]), 1)
  test(sum2([]), 0)
  test(sum2([4, 5, 6]), 9)
  test(sum2([4]), 4)
if __name__ == '__main__':
  main()