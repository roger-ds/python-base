#!/usr/bin/env python3
"""
Imprime a mensagem de um e-mail
NAO MANDE SPAM!!!
"""
__version__ = '0.1.1'

import sys 
import os

arguments = sys.argv[1:]
if not arguments:
    print('Informe o nome do arquivo de emails e de template')
    sys.exit()

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)

clientes = []
for line in open(filepath):
    nome, email =  line.split(',')

    # TODO: Substituir por envio de email
    print(f'Enviando email para: {email}')
    print(
        open(templatepath).read()
        % {
            'nome': nome,
            'produto': 'caneta',
            'texto': 'Escrever muito bem',
            'link': 'https:\\canetaslegais.com',
            'quantidade': 1,
            'preco': 50.5,
        }
    )
    print('-' * 40)
