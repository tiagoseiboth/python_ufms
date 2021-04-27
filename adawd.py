print("Qual foi o valor da nota obtida:")
nota = float(input())
if nota > 10 or nota < 0:
    print("Score incorreto")
if nota >= 9.0 and nota <=10:
    print("Parabens, voce tirou A")
if nota < 9.0 and nota >= 8.0:
    print("Muito bom, voce tirou B")
if nota < 8.0 and nota >= 7.0:
    print("Bom, voce tirou C")
if nota < 7.0 and nota >= 6.0:
    print("Na risca, voce tirou D")
if nota < 6.0 and nota >= 0:
    print("Hmm, estude mais, voce tirou F")