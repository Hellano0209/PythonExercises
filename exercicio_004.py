#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:29:41 2023

@author: hellano
"""

algo = input("Digite algo: ")

if algo.isnumeric():
    print("{} é um número.".format(algo))
if algo.isalnum():
    print("{} é alfanumérico.".format(algo))
if algo.isalpha():
    print("{} é alfabético.".format(algo))
    if algo.istitle():
        print("{} está capitalizado.".format(algo))
    if algo.isupper():
        print("{} tem todas as letras maiúsculas.".format(algo))
    if algo.islower():
        print("{} tem todas as letras minúsculas.".format(algo))