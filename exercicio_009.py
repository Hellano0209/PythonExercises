#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 10:08:01 2023

@author: hellano
"""

n = int(input('Digite um número entre 1 e 9: '))

print('A tabuada do número {} é:'.format(n))
for i in range(0, 9):
    print('{}x{} = {}'.format(i+1, n, n*(i+1)))