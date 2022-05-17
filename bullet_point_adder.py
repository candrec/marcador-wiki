#! /usr/bin/python3
# bullet_point_adder.py - Acrescenta marcadores da wikipedia no início
# de cada linha de texto do clipboard (área de transferência)
# Separa as linhas que estão na área de transferência e acrescenta asterisco no inicio de cada linha

import pyperclip
text = pyperclip.paste()

# TODO: separa as linhas e acrescenta asteriscos

pyperclip.copy(text)
