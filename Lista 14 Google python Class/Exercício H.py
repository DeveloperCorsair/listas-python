# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é, uma palavra é permutação das letras da outra
# *sem usar while ou for*
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False
def anagrama(s1, s2):
  return True if len(s1) == len(s2) and set(s1) == set(s2) else False

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ()
  print ('anagrama')
  test(anagrama('abacate', 'abacatx'), False)
  test(anagrama('sim', 'xxs'), False)
  test(anagrama('sim', 'siiimmmmm'), False)
  test(anagrama('iracema', 'america'), True)
  test(anagrama('ator', 'rota'), True)
  test(anagrama('aberto', 'rebato'), True)
  test(anagrama('amor', 'roma'), True)
  test(anagrama('ramo', 'amor'), True)
  test(anagrama('baba', 'aba'), False)
  test(anagrama('casa', 'cassa'), False)
  test(anagrama('palmeiras', 'abacate'), False)
  test(anagrama('arco', 'roca'), True)
  test(anagrama('alegria', 'alergia'), True)
  test(anagrama('cantiga', 'catinga'), True)
if __name__ == '__main__':
  main()