import os

print("Quantas horas foram trabalhadas?")
x1 = input()
try:
    x = int(x1)
    print("Qual o salario/h do funcionario em reais?")
    y = float(input())
    os.system('cls' if os.name == 'nt' else 'clear')
    if x > 40.00:
        z = y*40
        horas_extras = x-40 
        s_horas = y*0.50+y
        h_extras = s_horas*horas_extras
        s_final = z+(s_horas*horas_extras)
        print("###############################################")
        print("Horas extras trabalhadas:", horas_extras, "horas")
        print("Salario/h para horas extras:", s_horas , "Reais")
        print("Total pago em reais para as horas extras: %.2f" % h_extras)
        print("Salario final em reais: %.2f" % s_final)
        print("###############################################")
    else:
        s_total = x*y
        print("##############################################")
        print("Salario total por horas trabalhas: %.2f" % s_total)
        print("##############################################")
except:
    x = -1
    print("Valor incorreto para o numero de horas, por favor utilize somente numeros")
os.system('pause' if os.name == 'nt' else 'sleep(5)')