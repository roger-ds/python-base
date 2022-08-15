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

msg = 'Hello, World !'

if current_language == 'pt_BR':
    msg = 'Olá Mundo !'
elif current_language == 'it_IT':
    msg = 'Ciao, Mondo!'

print(msg)
print(current_language)

