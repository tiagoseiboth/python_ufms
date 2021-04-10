import os

print("Quantas horas foram trabalhadas?")
x = int(input())
print("Qual o salario/h do funcionario em reais?")
y = float(input())
os.system('cls' if os.name == 'nt' else 'clear')

if x > 40:
    z = y*40
    horas_extras = x-40 
    s_horas = y*0.50+y
    print("##############################################")
    print("Horas extras trabalhadas:", horas_extras, "horas")
    print("Salario/h para horas extras:", s_horas , "Reais")
    print("Total pago em horas extras:", s_horas*horas_extras , "Reais")
    print("Salario final:", z+(s_horas*horas_extras) , "Reais")
    print("##############################################")

if x <= 40:
    print("##############################################")
    print("Salario total por horas trabalhas:", x*y , "Reais")
    print("##############################################")

os.system('pause' if os.name == 'nt' else 'sleep(5)')