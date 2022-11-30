#!/usr/bin/env python3

import logging

# nossa instancia
log = logging.Logger('logs.py', logging.DEBUG)
# level
ch = logging.StreamHandler()    # ch - console handler
ch.setLevel(logging.DEBUG)
# formatacao
fmt = logging.Formatter(
    '%(asctime)s %(name)s %(levelname) '
    'l:%$(lineno)d f:%(filename)s: %(message)'
)

logging.critical('Deu problema geral')
logging.error('Erro que afera uma unica execucao')
logging.warning('Aviso que nao causa erro')
logging.info('Mensagem geral para usuarios')
logging.debug('Mensagem pro dev, qe, sysadmin')


try:
    1 / 0
except ZeroDivisionError as e:
    logging.error('[ERRO] Deu erro %s', str(e))

