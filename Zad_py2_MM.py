# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:39:45 2022

@author: Martyna
"""

#Zad 1


    
def czesc(name:str, surname:str)->str:
    
    return 'Cześć '+ name +' '+ surname+'!'

x=czesc('Martyna','Michalik')
print(x)

#Zad 2
def mnozenie(x: int, y:int):
    return x*y

print(mnozenie(2,3))

#Zad 3
def parzyste(liczba)-> bool:
    if liczba%2==0:
        return True
    else:
        return False
    
wynik=parzyste(3)
if wynik==True:
    print ("Liczba parzysta")
else:
    print ("Liczba nieparzysta")
    
    
#Zad 4

def czy_wieksze( x: int, y:int, z:int)->bool:
    return(x+y>=z)

print(czy_wieksze(1, 5, 2))

#Zad 5

def czy_zawiera( lista:list, x : int)->bool:
    
    if x in lista:
        return True
    else: False
 
liczby=[1,2,3,4]
print(czy_zawiera(liczby,2))

#Zad 6

def listy(l1:list,l2:list)->list:
    wynik=list(set(l1+l2))
    return wynik


l1=[1,2,3,4,5,6]
l2=[3,4,5,6,7,8,9]

print(listy(l1,l2))










