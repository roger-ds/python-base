"""
Alarme de temperatura

Faça um script que pergunte ao usuário qual a temperatura arual e o indice de
umidade do ar, sendo que será exibida uma mensagem de alerta dependendo das co_
ndições:

temp maior 45: ALERTA!!! Perigo calor extremo
temp vezes 3 for maior ou igual a umidade: ALERTA!!! Perigo de calor úmido
temp entre 10 e 30 : Normal
temp < 0: ALERTA: Frio extremo
"""

import sys
import logging

log = logging.Logger('alerta')

info = {
    'temperatura': None,
    'umidade': None
}
keys = info.keys()

for key in keys:
    
    try:
        info[key] = float(input(f'Qual a {key} atual ? ').strip())
    except ValueError: 
        log.error(f'{key.capitalize()} invalida')
        sys.exit(1)

temp = info['temperatura']
umidade = info['umidade']

if temp <= 0: print('Frio extremo') 
elif temp > 0 and temp <= 10: print('Frio')
elif temp > 10 and temp <= 30: print('Normal')
elif temp > 45: print('Calor extremo')
elif temp * 3 >= umidade: print('ALERTA!!! Perigo de calor úmido')
