import math
print("Para calcular o tempo de queda de um objeto forneça os dados abaixo")
print("Altura em metros:")
h = float(input())
print("Informe o valor da gravidade em m/s²:")
g = float(input())
t = math.sqrt((h*2/g))
print("Tempo até o objeto partindo do repouso cair, em segundos: %2.2f"  % t)