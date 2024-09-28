import numpy as np

# constantes e parametros
x = 0
quantidade_intervalos = 11
k = 8.99e9
q1 = float(input("valor de q1:"))
q2 = float(input("valor de q2:"))
r = float(input("distancia entre cargas:"))
r1 = x

#listas para armazenar os valores de x e E
valores_x = np.linspace(0, r, quantidade_intervalos)
valores_E = np.zeros(quantidade_intervalos)

#funcao para calcular campo eletrico resultante das cargas
def campo_E(x):
    if x == 0 or x == r:
        return np.inf
    campo_q1 = k*q1/(x**2)
    campo_q2 = k*q2/((r-x)**2)
    campo_total = campo_q1 - campo_q2
    return campo_total

#laco para calcular a distancia
for i in range (1, quantidade_intervalos-1):
    x = valores_x[i]
    resultado = campo_E(x)
    valores_E[i] = resultado
    teste = valores_E[i-1] * valores_E[i]
#    print(valores_x[i], valores_E[i])
    if teste < 0:
        print("A distancia em que o campo é nulo está entre %.4f" % valores_x[i-1], "e %.4f" % valores_x[i])
        a = valores_x[i-1]
        b = valores_x[i]
        break

#Aproximação das raizes
precisao = float(input("Digite a precisao para a aproximação da raiz:"))
contagem = 0
raiz = (a + b) / 2
fx_a = campo_E(a)
fx_b = campo_E(b)

# falsa posição

#raiz = b - (fx_b*(b-a))/(fx_b - fx_a)

# loop para calculo do refinamento das raizes

while (b - a) > precisao:

    x = raiz
    valor_x = campo_E(x)
    passos = contagem
    contagem = passos + 1
    print(contagem, "%.6f" % a, "%.6f" % b, (b-a))

    if (valor_x*fx_a) < 0:
        b = x

    if (valor_x*fx_a) > 0:
        a = x

#    raiz = b - (fx_b*(b-a))/(fx_b - fx_a)   # posicao falsa
    raiz = (a + b) / 2  #bissecção

print("A raiz esta entre %.7f" % a, "e %.7f" % b)