#! /usr/bin/env python3
"""
Calcula a tabuada de 1 a 10.
"""
__version__ = '0.0.1'
__author__ = 'Rogerio Rodrigues'
__license__ = 'Unlicense'

numeros = list(range(1, 11))

for n1 in numeros:
    print()
    print('{:-^20}'.format(f'Tabuada do {n1}'))
    for n2 in numeros:
        resultado = n1 * n2
        print('{:^20}'.format(f'{n1} x {n2} = { resultado}'))
    print('#' * 20)
