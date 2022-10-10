# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 13:50:56 2022

@author: Martyna
"""
#Zad 2
#a
'''
def imiona(lista):
    for i in lista:
        print(i)

names = ['Martin', 'Tom', 'Eva','Julia','Julianna']
imiona (names)
'''
#b

def liczby(lista):
    for i in range(len(lista)):
        lista[i]=lista[i]*2
    return lista

numerki=[1,2,3,4,5]
print(liczby(numerki))

numerki=[1,2,3,4,5]
numerki_2=[number*2 for number in numerki]
print(numerki_2)

#c

def parzyste(liczby):
    for i in range(len(liczby)):
        if liczby[i]%2==0:
            print(liczby[i])
            
numerki10=[1,2,3,4,5,6,7,8,9,10]

parzyste(numerki10)

#d
def co_drugie(liczby):
    print(numerki10[::2]) 
        
  
        
co_drugie(numerki10)









