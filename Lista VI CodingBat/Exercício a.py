# A. dormir
# dia_semana é True para dias na semana
# feriado é True nos feriados
# você pode ficar dormindo quando é feriado ou não é dia semana
# retorne True ou False conforme você vá dormir ou não
def dormir(dia_semana, feriado):
    return not dia_semana or feriado
    
    """ if dia_semana True:
        print('Não é hora de dormir, é dia de semana!')
    else:
        print('Você pode dormir. Pois é feriado!') """
    
print(dormir(False, False))