#! /usr/bin/env python3
"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Ou informe atraves do CLI argument `--lang`

Ou o usuario tera que digitar.

Execucao:

    python3 hello.python3
    ou
    ./hello.py
"""
__version__ = '0.1.3'
__author__ = 'Rogerio Rodrigues'
__license__ = 'Unlicense'

import os
import sys

print(f'{sys.argv=}') # atente para o =
arguments = {'lang': None, 'count': 1}

for arg in sys.argv[1:]:
    # TODO: Tratar Value Error
    key, value = arg.split('=')
    key = key.lstrip('-').strip()
    value = value.strip()
    if key not in arguments:
        print(f'Invalid Option {key}')
        sys.exit()
    arguments[key] = value

current_language = arguments['lang']
if current_language is None:
    # TODO: Usar repeticao
    if 'LANG' in os.environ:
        current_language = os.getenv('LANG')
    else:
        current_language = input('Choose a language:')

current_language = current_language[:5]    

msg = {
    'en_US': 'Hello, World !',
    'pt_BR': 'Olá Mundo !',
    'it_IT': 'Ciao, Mondo!',
    'es_ES': 'Holla, Mundo!',
    'fr_FR': 'Bon ju Mounde!',
}

print(msg[current_language] * int(arguments['count']))

# commit concluido
