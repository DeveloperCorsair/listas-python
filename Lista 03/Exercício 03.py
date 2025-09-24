# EXERCÍCIO 3

afeganistao = 80000 # País 1
brasil = 200000 # País 2
ano = 0

while afeganistao <= brasil:
   ano += 1
   afeganistao = afeganistao * 1.03
   brasil = brasil * 1.015
   print(f'Ano: {ano}, População Br: {brasil:.2f}, população Af: {afeganistao:.2f}')
ano += 1
print(f'Ano {ano}. A população do Afeganistão: {afeganistao:.2f} é maior que a do Brasil: {brasil:.2f}')
