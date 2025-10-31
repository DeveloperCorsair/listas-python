# J. zeros finais
# Verifique quantos zeros há no final de um número inteiro positivo
# Exemplo: 10010 tem 1 zero no fim e 908007000 possui três
# dica transforme para texto e inverta
# n = str(n)
# n = n[::-1]
def zf(n):
  n = str(n)
  n = n[::-1]
  contador = 0
  for i in range(len(n)):
      if n[i] == '0':
        contador +=1 
      else: 
        return contador

def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def main():
  print ()
  print ('zeros finais')
  test(zf(10100100010000), 4)
  test(zf(90000000000000000010), 1)
if __name__ == '__main__':
  main()