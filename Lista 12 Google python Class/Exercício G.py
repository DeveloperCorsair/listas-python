# G. verbing
# Dada uma string, caso seu comprimento seja pelo menos 3,
# adiciona 'ing' no final
# Caso a string já termine em 'ing', acrescentará 'ly'.
# dica use s.endswith('ing')
def verbing(s):
  return s + 'ly' if s.endswith('ing') else s + 'ing' if len(s) > 3 else s 

  if s.endswith('ing') == True:
    return s + 'ly'
  if len(s) >= 3:
    return s + 'ing'
  else:
    return s

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')
if __name__ == '__main__':
  main()