# informatica2023
import numpy as np
A = np.matrix([[2.0, 3.0, 4.0, 5.0], [6.0, 15.0,19.0, 23.0],[8.0, 42.0, 60.0, 70.0],[12.0, 60.0,1.0, 17.0]])
b = np.array([5.0, 30.0, 98.0, 144.0])
x = np.zeros(len(A))
def Gauss(A, b):
#Dimensión del sistema
     n = len(A)
#Matriz ampliada
     Ab = np.c_[A,b]
#Triangulación
     for k in range(0,n-1):
         for i in range(k+1,n):
             m= +Ab[i,k]/Ab[k,k]
             for j in range(0,n+1):
                 Ab[i,j] = Ab[i,j] - m*Ab[k,j]
                 
         
     
#Sustitución
     for k in range(n-1,-1,-1):
         m= 0.0
         for i in range(k+1,n):
             m=+ Ab[k,i]*x[i]
         x[k]= (Ab[k,n] -m)/ Ab[k,k]
     
     return x
x = Gauss(A, b)
print('\n El vector solución del sistema, x=', x)
