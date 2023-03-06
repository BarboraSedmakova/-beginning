#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 17:41:17 2023

@author: barbora
"""
# Štvrtá úloha
a = int(input("Ahoj, vlož prvé číslo! "))

while a <= 1000:
   
    cislo = int(input("Ahoj, vlož opäť číslo! "))
    operacia = input("vlož znak operácie ")
    if operacia == "+":
       a = a + cislo
       print(a)
    elif operacia == "-":
         a = a - cislo
         print(a)
    elif operacia == "*":
         a = a * cislo
         print(a)
    else :
         print("NEPLATNÁ OPERÁCIA!")
           
     
     

