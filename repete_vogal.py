"""
Repete vogais

Faça um programa que pede ao usuário para digitar uma ou  mais words e 
imprime cada uma das words com suas vogais duplicadas.

ex:
python3 repete_vogal.py
'Digite uma word (ou enter para sair):' Python
'Digite uma word (ou enter para sair):' Bruno

Pythoon
Bruunoo
"""

vogais = 'aeiou'
words = []
while True:
   
    word = input('Digite uma word (ou enter ara sair):').strip()
    if not word:
        break
    final_word = ''
    for letter in word:
        # TODO: Remover acentuaçao com funçoes
        if letter.lower() in vogais:
           final_word += letter * 2
        else:
            final_word += letter
    words.append(final_word)

print(*words, sep='\n')

