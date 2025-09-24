# EXERCÍCIO 4

import re
 
texto = '''“ The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you. ”'''
 
res = re.sub(r"[.,:;]", " ", texto)
 
palavras = res.split()
 
words = "python"
 
resultado = []
 
for palavra in palavras:
    palavra = palavra.lower()
    if palavra[0] in words or palavra[-1] in words:
        resultado.append(palavra)
 
print(resultado)