print("Digite 1 para converter °F para °C, e 2 para °C para °F")
escolha = int(input())
if escolha == 1:
    print("Entre com o valor em °F:")
    valor1 = float(input())
    temp1 = (valor1-32)/1.8
    print(valor1, "°F é = %.2f °C" % temp1)
    if temp1 > 40:
        print("Muito quente")
    else:
        if temp1 >= 30:
            print("Quente")
        else:
            if temp1 >= 15:
                print("Agradavel")
            else:
                if temp1 >= 5:
                    print("friozinho")
                else:
                    if temp1 >= 0:
                        print("Frio")
                    else:
                        if temp1 >= -10:
                            print("Muito frio")
                        else:
                            if temp1 < -10:
                                print("Congelante")
else:
    print("Entre com o valor em °C")
    valor2 = float(input())
    temp2 = valor2*1.8+32
    print(valor2, "°C é = %.2f °F" % temp2)
    if valor2 >= 40:
        print("Muito quente")
    else:
        if valor2 >= 30:
            print("Quente")
        else:
            if valor2 >= 15:
                print("Agradavel")
            else:
                if valor2 >= 5:
                    print("friozinho")
                else:
                    if valor2 >= 0:
                        print("Frio")
                    else:
                        if valor2 >= -10:
                            print("Muito frio")
                        else:
                            if valor2 < -10:
                                print("Congelante")