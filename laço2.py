print("Pressione enter para determinar valor do produto 1*3*5*7*11")
input()

num_ini = 1

for num in [1, 3, 5, 7, 11] :
    num_ini = num_ini * num

print("O produto é =", num_ini)