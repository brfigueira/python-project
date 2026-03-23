n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

print("===Avaliando qual o menor número:===")

if (n1>n2):
    print(f"O número {n1} é menor que o número {n2}.")
elif (n1<n2):
    print(f"O número {n2} é menor que o número {n1}.")
else:
    print("Ambos os números são iguais!")