# E. hello_name
# seja uma string name
# hello_name('Bob') -> 'Hello Bob!'
# hello_name('Alice') -> 'Hello Alice!'
# hello_name('X') -> 'Hello X!'
def hello_name(name):
  return 'Hello ' + name + '!'

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
  print ('Hello Name')
  test(hello_name('Bob'), 'Hello Bob!')
  test(hello_name('Alice'), 'Hello Alice!')
  test(hello_name('X'), 'Hello X!')
  test(hello_name('Hello'), 'Hello Hello!')
if __name__ == '__main__':
  main()
