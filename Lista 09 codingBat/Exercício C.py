# C. common_end #
# Dada duas listas a e b verifica se os dois primeiros são
# iguais ou os dois últimos são iguais, isto significa
# o primeiro da lista a igual ao primeiro da lista b
# ou o último da lista a igual ao último da lista b
# suponha que as listas tenham pelo menos um elemento
# common_end([1, 2, 3], [7, 3]) -> True
# common_end([1, 2, 3], [7, 3, 2]) -> False
# common_end([1, 2, 3], [1, 3]) -> True
def common_end(a, b):
    # Inline, direto no return
    return False if a and b == [] else True if a[0] == b[0] or a[-1] == b[-1] else False

    # Em bloco
    '''for i in (a, b):
        if a[0] == b[0] or a[-1] == b[-1]:
                return True
        else:
            if a or b == []:
                return False
            else:
                return False'''

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
  print ('Common_end')
  test(common_end([1, 2, 3], [7, 3]), True)
  test(common_end([1, 2, 3], [7, 3, 2]), False)
  test(common_end([1, 2, 3], [1, 3]), True)
  test(common_end([1, 2, 3], [1]), True)
  test(common_end([1, 2, 3], [2]), False)
if __name__ == '__main__':
  main()
