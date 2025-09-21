# D. array_front9
# verifica se pelo menos um dos quatro primeiros é nove
# array_front9([1, 2, 9, 3, 4]) -> True
# array_front9([1, 2, 3, 4, 9]) -> False
# array_front9([1, 2, 3, 4, 5]) -> False
def array_front9(nums):
  return True if nums[0:3].count(9) else False

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
  print ('Array front 9')
  test(array_front9([1, 2, 9, 3, 4]), True)
  test(array_front9([1, 2, 3, 4, 9]), False)
  test(array_front9([1, 2, 3, 4, 5]), False)
  test(array_front9([9, 2, 3]), True)
  test(array_front9([1, 9, 9]), True)
  test(array_front9([1, 2, 3]), False)
  test(array_front9([1, 9]), True)
  test(array_front9([5, 5]), False)
  test(array_front9([2]), False)
  test(array_front9([9]), True)
  test(array_front9([]), False)
  test(array_front9([3, 9, 2, 3, 3]), True)
if __name__ == '__main__':
  main()
