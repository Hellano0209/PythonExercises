#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 13:50:06 2023

@author: hellano
"""

altura = float(input('Qual a altura da parede: '))
largura = float(input('Qual a largura da parede: '))

area = altura*largura
tinta = area/2 # 1 litro de tinta para 2 m² de parede

print('Essa parede tem uma área de {:.2f}m².'.format(area))
print('Você irá precisar de {:.2f}l de tinta'.format(tinta))
