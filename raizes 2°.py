import math
print("Para esquações sem o termo C, digite 1; sem o termo B, digite 2; para equações com os 3 termos digite 3.")
escolha = int(input())
print("Entre apenas os valores que acompanham os termos. Ex: 2x² -3x -4, 2 -3 -4; Em casos em que um dos termos é omitido, ou seja, = 0 siga o exemplo: ex2: 2x² - 27, 2 0 -27")
a, b, c = input().split()
a1 = float(a)
b1 = float(b)
c1 = float(c)
if escolha == 3:
    delta = b1**2-(4*a1*c1)
    if delta <= 0:
        print("Solução impossivel ou apenas com numeros imaginarios.")
    else:
        r1 = ((-1*b1)+math.sqrt(delta))/2*a1
        r2 = ((-1*b1)-math.sqrt(delta))/2*a1
        print("As raizes são:")
        print("%.2f" % r1)
        print("%.2f" % r2)
if escolha == 2:
    razaoC1_A1 = (c1*-1)/a1
    if razaoC1_A1 <= 0:
        print("Solução impossivel ou apenas com numeros imaginarios.")
    else:
        r = math.sqrt(razaoC1_A1)
        print("As raizes são:")
        print("%.2f" % r)
        print("%.2f" % -r)
if escolha == 1:
    r2 = (b1*-1)/a1
    r1 = 0
    print("As raizes são:")
    print("%.2f" % r2)
    print("%.2f" % r1)