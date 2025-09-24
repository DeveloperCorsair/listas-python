# A. dormir
# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo quando é feriado ou não é dia semana
# retorne True ou False conforme você vá dormir ou não
def dormir(dia_semana, feriado):
  return not dia_semana or feriado

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
  print ('Oba! Hoje vou ficar dormindo!')
  test(dormir(False, False), True)
  test(dormir(True, False), False)
  test(dormir(False, True), True)
  test(dormir(True, True), True)
if __name__ == '__main__':
  main()