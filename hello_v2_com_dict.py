#! /usr/bin/env python3
"""
Hello World Multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem 
correspondente.

Como usar:

Tenha a variavel LANG devidamente configurada ex:

    export LANG=pt_BR

Execucao:

    python3 hello.python3
    ou
    ./hello.py
"""
__version__ = '0.0.1'
__author__ = 'Rogerio Rodrigues'
__license__ = 'Unlicense'

import os

current_language = os.getenv('LANG', 'en_US')[:5]

msg = {
    'en_US': 'Hello, World !',
    'pt_BR': 'Olá Mundo !',
    'it_IT': 'Ciao, Mondo!',
    'es_ES': 'Holla, Mundo!',
    'fr_FR': 'Bon ju Mounde!',
}

print(msg[current_language])

# commit concluido
