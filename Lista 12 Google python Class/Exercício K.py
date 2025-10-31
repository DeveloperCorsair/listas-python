# K. conta 2
# Verifique quantas vezes o dígito 2 aparece entre 0 e n-1
# Exemplo: para n = 20 o dígito 2 aparece duas vezes entre 0 e 19
def conta2(n):
  contador = 0
  for i in range(0, n-1):
    i = str(i)
    if '2' in i:      
      a = i.count('2')
      contador = contador + a
  return contador

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ()
  print ('conta 2')
  test(conta2(20), 2)
  test(conta2(999), 300)
  test(conta2(555), 216)
if __name__ == '__main__':
  main()