# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 11:32:26 2023

@author: Daniela Chinarro
"""

import numpy as np
A = np.matrix([[2.0, 3.0, 4.0, 5.0], [6.0, 15.0, 19.0, 23.0],[8.0, 42.0, 60.0, 70.0],[12.0, 60.0, 1.0, 17.0]])
b = np.array([5.0, 30.0, 98.0, 144.0])
x = np.zeros(len(A))

def Gauss(A, b):
    #Dimensión del sistema
    n=len(A)
    
    #Matriz ampliada
    Ab = np.c_[A,b] #usamos la función stack colum que permite añadir una columna extra
    
    #Triangulación
    for k in range(0,n-1):#cada elemento en la diagonal menos el último
        if Ab[k,k]==0: #si un elemento de la diagonal es 0
            for i in range(k+1,n):#filas por debajo de la diagonal
               if abs(A[i,k])>b<abs(Ab[k,k]):
                   Ab[k,i]=Ab[i,k]
                   break
        else:     
            for i in range(k+1,n):      
                for j in range(1,n+1): #cada elemento de la fila
                        m=-Ab[i,k]/Ab[k,k]
                        Ab[i,j]=Ab[i,j]+m*Ab[k,j]
                    
    #sustitucion
        for k in range(n-1,-1,-1):
            m=0.0
            for i in range(k+1,n):
                m=m+Ab[k,i]*x[i]
            x[k]= (Ab[k,n]-m)/Ab[k,k]
    return x


x = Gauss(A, b)
print('\n El vector solución del sistema, x=', x)