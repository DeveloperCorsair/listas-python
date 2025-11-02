# B. x_antes
# Dada uma lista de strings retorna uma lista onde
# todos os elementos que começam com x ficam sorteados antes 
# Ex.: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] retorna
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Obs.: é necessário que cada lista esteja em ordem antes
# de juntar, a que tem strings que começam com x e a que não
# Dica: monte duas listas separadas e junte-as no final
def x_antes(words):
  a = []
  b = []
  for i in words:
    if i[0] == 'x':
    #if i.startswith('x'):
      b.append(i)
    else:
      a.append(i)
  return sorted(b) + sorted(a)

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ()
  print ('x_antes')
  test(x_antes(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(x_antes(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(x_antes(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
if __name__ == '__main__':
  main()