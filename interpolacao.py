#!/usr/bin/env python3
"""
Imprime a mensagem de um e-mail
NAO MANDE SPAM!!!
"""
__version__ = '0.1.1'

import sys 
import os
import smtplib
from email.mime.text import MIMEText


arguments = sys.argv[1:]
if not arguments:
    print('Informe o nome do arquivo de emails e de template')
    sys.exit()

filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
templatepath = os.path.join(path, templatename)


with smtplib.SMTP(host='localhost', port=8025) as server:

    for line in open(filepath):
        nome, email =  line.split(',')

        text = (
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

        from_ = 'rogeriodemoraes@gmail.com'
        to = ', '.join(['r.ufpa@bol.com.br', 'email'])
        message = MIMEText(text)
        message['Subjec'] = 'Compre mais'
        message['From'] = from_
        message['To'] = to

        server.sendmail(from_, to, message.as_string())
