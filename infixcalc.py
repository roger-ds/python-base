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

__version__ = '0.2.0'

import os
import sys
from datetime import datetime


#print(f'{sys.argv=}')
path = os.curdir
filepath = os.path.join(path, 'infixcalc.log')
arguments = sys.argv[1:]
timestamp = datetime.now().isoformat()
user = os.getenv('USER', 'anonymous')


valid_operations = {
    'sum': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}

while True:

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

    try:
        n1, n2 = validated_nums
    except ValueError as e:
        print(str(e))
        sys.exit(1)

    result = valid_operations[op](n1,n2)
    
    print(result)

    try:
        with open(filepath, 'a') as file:
            file.write(f'{timestamp} - {user} - {op} {n1} {n2} = {result}\n')
    except PermissionError as e:
        # TODO: logging
        print(str(e))
        sys.exit(1)

    arguments = None

    if input('Pressione enter para continuar ou qualquer tecla para sair'):
        break
