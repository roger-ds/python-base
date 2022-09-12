#!/usr/bin/env/ python3

<<<<<<< HEAD
import logging  # root logger

# nossa instancia
log = logging.Logger('logs.py', logging.DEBUG) # mostra bruno against root logger ex: __name__
=======
import logging

# nossa instancia
log = logging.Logger('logs.py', logging.DEBUG)
>>>>>>> feature
#level
ch = logging.StreamHandler()


logging.critical('Erro geral ex: banco de dados sumiu')
logging.error('Erro que afeta uma unica execucao')
logging.warning('Aviso que nao causa erro')
<<<<<<< HEAD
logging.info('Mensagem geral para usuarios')
logging.debug('Mensagem pro dev, qe, sysadmin')

print('-' * 50)
=======
logging.debug('Mensagem pro dev, qe, sysadmin')
logging.info('Mensagem geral para usuarios')

print('-' * 50) 
>>>>>>> feature

try:
  1 / 0
except ZeroDivisionError as e:
  logging.error('Deu erro %s', str(e))