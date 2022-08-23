#!/usr/bin/env python3
'''
Exibe relatorio de criancas por atividade.

Imprimir a lista de criancas agrupadas por sala
que frequenta cada uma das atividades.
'''
__version__ = '0.1.0'

# Dados
sala1 = ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana']
sala2 = ['Joao', 'Antonio', 'Carlos', 'Maria', 'Isolda']

aula_ingles = ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio']
aula_musica = ['Erik', 'Carlos','Maria']
aula_danca = ['Gustavo', 'Sofia', 'Joana', 'Antonio']

atividades = [
    ('ingles', aula_ingles), 
    ('musica', aula_musica), 
    ('danca', aula_danca)
]

# Listar alunos em cada  atividade por sala.
for nome_atividade, atividade in atividades:
    print()
    print(f'Alunos da atividade {nome_atividade}')
    print('-' * 40)

    # sala que tem intersecao com a atividade
    atividade_sala1 = set(sala1) & set(atividade)
    atividade_sala2 = set(sala2).intersection(set(atividade))

    print(f'{nome_atividade} sala 1 {atividade_sala1}')
    print(f'{nome_atividade} sala 2 {atividade_sala2}')
    print('#' * 40)