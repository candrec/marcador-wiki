#! /usr/bin/python3
# bullet_point_adder.py - Acrescenta marcadores da wikipedia no início
# de cada linha de texto do clipboard (área de transferência)
# Separa as linhas que estão na área de transferência e acrescenta asterisco no inicio de cada linha

import pyperclip
text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):    #percorre todos os índices da lista "lines" no loop
    lines[i] = '* ' + lines[i] #acrescenta um asterisco em cada string da lista "lines"
text = '\n'.join(lines)

pyperclip.copy(text)
