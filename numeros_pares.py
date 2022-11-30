"""
Imprime os numeros pares de 1 a 200
ex
python3 numros_pares.py
2
4
6
8
...
"""


for i in range(201):
    if i % 2 != 0:
        continue
    print(i)
