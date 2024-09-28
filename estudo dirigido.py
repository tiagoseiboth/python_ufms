import numpy as np
import math as m

# constantes e parametros

x = 0
quantidade_intervalos = 100
k = 8.99e9
q1 = float(input())
q2 = float(input())
r = float(input())
r2 = r**2 - 2*r*x + x**2
r1 = x

valores_x = np.linspace(r, quantidade_intervalos)
valores_dist = np.zeros(quantidade_intervalos)

def dist(x):
    q1*(r2) - (q2*r1)
    
for i in range (1, quantidade_intervalos-1):
    x = valores_x[i]
    resultado = dist(x)
    valores_dist[i] = dist(x)
    if resultado == 0:
        print(x)
        
    