#!/usr/bin/env python3
'''
Exemplos de envio de email
'''
import smtplib

SERVER = 'localhost'
PORT = 8025

FROM = 'rogeriodemoraes@gmail.com'
TO = ['r.ufpa@bol.com.br', 'destino2@server.com']
SUBJECT = 'Meu email via python'
TEXT = '''\
Este é o meu e-mail enviado pelo Python
<b>Olá mundo<b>
'''

# mensagem conforme o protocolo SMTP
message = f'''\
From: {FROM} 
To: {', '.join(TO)} 
Subjec: {SUBJECT}

{TEXT}
'''


with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, message.encode("utf-8"))
