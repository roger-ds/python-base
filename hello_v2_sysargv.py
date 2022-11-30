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
# commst concluido

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
<<<<<<< HEAD
        # TODO: Logging
        print(f'[ERROR] {str(e)}')
        print('You need to use `=`')
        print(f'You passed {arg}')
        print('try with --key=value')
        sys.exit()
        
=======
        log.error(
            "You need to use `=`, you passed %s, try --key=value: %s",
            arg,
            str(e)
        )
        sys.exit(1)
>>>>>>> 80104d5a0c9af86044074a353cae7f5b3fd6b767
    key = key.lstrip('-').strip()
    value = value.strip()

    # validaçao
    if key not in arguments:
<<<<<<< HEAD
        print(f'Invalid Option {key}')
=======
        print(f'Invalid Option `{key}`')
>>>>>>> 80104d5a0c9af86044074a353cae7f5b3fd6b767
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

"""
# try com valor defout
message = msg.get(current_language, msg['en_US'])
"""
# EAFP
try:
    message = msg[current_language]
except KeyError as e:
    print(f'[ERROR] {str(e)}')
    print(f'Language is invalid, choose from: {list(msg.keys())}')
    sys.exit(1)

print(message * int(arguments['count']))

