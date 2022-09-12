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
import logging

# BOILERPLATE
# TODO: Usar funcao
# TODO: Usar lib externa (loguru)
log_level = os.getenv('LOG_LEVEL', 'WARNING').upper()
log = logging.Logger('logs', log_level) # mostra logs against root logger ex: __name__
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
  '%(asctime)s %(name)s  %(levelname)s l:%(lineno)d f:%(filename)s %(message)s'
)
ch.setFormatter(fmt)
log.addHandler(ch)

print(f'{sys.argv=}') # atente para o =
arguments = {'lang': None, 'count': 10}

for arg in sys.argv[1:]:
    try:
        key, value = arg.split('=')
    except ValueError as e:
        log.error(
            "You need to use `=`, you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)
    key = key.lstrip('-').strip()
    value = value.strip()

    # validaçao
    if key not in arguments:
        print(f'Invalid Option `{key}`')
        sys.exit(1)
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
