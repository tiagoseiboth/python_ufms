print("Informe a temperatura em que se encontra o objeto em °C:")
t = float(input())
print("Informe a temperatura final com que o objeto deve ficar em °C:")
t_f = float(input())
print("Informe a massa em g do objeto:")
m = float(input())
print("Informe o calor especifico do objeto em cal/g°C:")
c = float(input())
energia = m*c
var_temp = t_f-t
energia_f = energia*var_temp
print("Calorias nescessarias para aquecer até a temperatura alvo: %.3f" % energia_f)