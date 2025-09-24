# EXERCÍCIO 5

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
 
letras_python = set("python")

resultado = [
    p for p in palavras
    if len(p) > 4 and any(letra in letras_python for letra in p)
]

print(resultado)
print(len(resultado))