#!/usr/bin/env/ python3
import os
import logging  # root logger

log_level = os.getenv('LOG_LEVEL', 'WARNING').upper()

# nossa instancia
log = logging.Logger('logs', log_level) # mostra bruno against root logger ex: __name__
#level
ch = logging.StreamHandler()
ch.setLevel(log_level)
# formataçao
fmt = logging.Formatter(
  '%(asctime)s %(name)s  %(levelname)s l:%(lineno)d f:%(filename)s %(message)s'
)
ch.setFormatter(fmt)
# destino
log.addHandler(ch)

log.critical('Erro geral ex: banco de dados sumiu')
log.error('Erro que afeta uma unica execucao')
log.warning('Aviso que nao causa erro')
log.info('Mensagem geral para usuarios')
log.debug('Mensagem pro dev, qe, sysadmin')

print('-' * 50)

try:
  1 / 0
except ZeroDivisionError as e:
  log.error('Deu erro %s', str(e))