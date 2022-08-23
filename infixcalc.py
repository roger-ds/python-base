#!/usr/bin/env python3
"""Calculadira infix.

Funcionamento:

[operacao] [n1] [n2]

Operacoes:
sum -> +
sub -> -
mul -> *
div -> / 

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py
operacao: mul
n1: 3
n2: 5
15

Os resultados serao gravados em infixcalc.log
"""

__version__ = '0.1.0'

import os
import sys
from datetime import datetime


path = os.curdir
filepath = os.path.join(path, 'infixcalc.log')

#print(f'{sys.argv=}')

arguments = sys.argv[1:]

if not arguments:
   op = input('operacao:').strip()
   n1 = input('n1:').strip()
   n2 = input('n2:').strip()
   arguments = [op, n1, n2]
elif len(arguments) != 3:
    print('Numero de argumentos invalido')
    print('ex: `sum 5 3`')
    sys.exit(1)

op, *nums = arguments

valid_operations = 'sum', 'sub', 'mul', 'div'
if op not in valid_operations:
    print('Operacao invalida')
    print(valid_operations)
    sys.exit(1)

validated_nums = []
for num in nums:
    # TODO: Repeticao while + exeptions
    if not num.replace('.', '').isdigit():
        print(f'Numero invalido {num}')
        sys.exit()
    if '.' in num:
        num = float(num)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums
# TODO: Usar dict de funcoes
if op == 'sum':
    result = n1 + n2
elif op == 'sub':
    result = n1 - n2
elif op == 'mul':
    result = n1 * n2
elif op == 'div':
    result = n1 / n2

timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')

with open(filepath, 'a') as file:
    file.write(f'{timestamp} - {user} - {op} {n1} {n2} = {result}\n')

print(result)
