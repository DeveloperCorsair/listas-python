# B. same_first_last #
# retorna True se a lista nums
# possui pelo menos um elemento
# e o primeiro elemento é igual
# ao último
# same_first_last([1, 2, 3]) -> False
# same_first_last([1, 2, 3, 1]) -> True
# same_first_last([1, 2, 1]) -> True
def same_first_last(nums):
  return ''.join([nums and nums[0] == nums[-1] if nums == True else False for i in  range(len(nums))])

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
  print ('Same_first_last')
  test(same_first_last([1, 2, 3]), False)
  test(same_first_last([1, 2, 3, 1]), True)
  test(same_first_last([1, 2, 1]), True)
  test(same_first_last([7]), True)
  test(same_first_last([]), False)
  test(same_first_last([7, 7]), True)
if __name__ == '__main__':
  main()