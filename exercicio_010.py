#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 12:43:16 2023

@author: hellano
"""

valor = float(input("Quantos reais você deseja converter para dolar: "))
dolar = 5.12

nvalor = valor/dolar

print('Com R${:.2f} você consegue comprar ${:.2f}'.format(valor, nvalor))