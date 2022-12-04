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

import logging

# TODO: Mover para módulo

def is_completely_filled(dict_of_inputs):
    """Returns a boolean telling if a dict is completely filled."""
    info_size = len(dict_of_inputs)
    filled_size = len(
        [value for value in dict_of_inputs.values() if value is not None]
    )
    return info_size == filled_size


def read_inputs_for_dict(dict_of_info):
    """Reads information for a dict from user input."""
    for key in dict_of_info.keys():
        if dict_of_info[key] is not None:
            continue
        try:
            dict_of_info[key] = float(input(f'Qual a {key} atual ? ').strip())
        except ValueError: 
            log.error(f'{key.capitalize()} invalida')
            break


log = logging.Logger('alerta')

info = {'temperatura': None, 'umidade': None}

while not is_completely_filled(info):
    read_inputs_for_dict(info)

temp, umidade = info.values()

if temp <= 0: print('Frio extremo') 
elif temp > 0 and temp <= 10: print('Frio')
elif temp > 10 and temp <= 30: print('Normal')
elif temp > 45: print('Calor extremo')
elif temp * 3 >= umidade: print('ALERTA!!! Perigo de calor úmido')
