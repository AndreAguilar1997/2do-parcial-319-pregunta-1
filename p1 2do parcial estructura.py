# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 02:17:40 2022

@author: USER
"""
print("forma estructurada")
n=int(input("ingresar un numero "))
a=0
b=1
cont=0
if n<= 0:
    print("ingresar un numero entero")
elif n==1:
    print(a)
else:
    print("la serie fibonaci es: ")
    while cont < n:
        print(a)
        f= a+b
        a=b
        b=f
        cont+=1



print("finonaci en forma recursuva:")
def recursivafibonaci(nn):
    if nn<= 1:
        return nn
    else:
        return(recursivafibonaci(nn-1) + recursivafibonaci(nn-2))
    
nr=int(input("ingresar un numero "))
if nr<=0:
    print("ingrese otro numero")
else:
    print("la serie fibonaci es: ")
    for i in range(nr):
        print(recursivafibonaci(i))