opcao = int(input("Digite o número do programa que deseja utilizar: \n" \
"1. Menor número\n" \
"2. Par ou Impar\n" \
"3. Estado Civil\n" \
"-------->"))
# 1. Menor número
if (opcao == 1):
    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite outro número: "))
    if (numero1 > numero2):
        print(f"O numero {numero2}, é menor que o número {numero1}!")
    elif (numero2 > numero1):
        print(f"O numero {numero1}, é menor que o número {numero2}!")
    else:
        print("Ambos os números são iguais.")

# 2. Par ou Impar
elif (opcao == 2):
    numero = int(input("Digite um número para ser verificado:"))
    resto = numero % 2
    if (numero <= 0):
        print("Valor inválido!")
    elif (resto == 0):
        print(f"O número {numero} é PAR!")
    else:
        print(f"O número {numero} é IMPAR!")

# 3. Estado Civil
elif (opcao == 3):
    estado_civil = input("Digite a opção do seu estado civil:\n" \
    "C. Casado\n" \
    "S. Solteiro\n" \
    "D. Divorciado\n" \
    "V. Viúvo\n" \
    "O. Outros\n" \
    "-------->").lower()

    if (estado_civil == "c"):
        print("Casado!")
    elif (estado_civil == "d"):
        print("Divorciado!")
    elif (estado_civil == "s"):
        print("Solteiro!")
    elif (estado_civil == "o"):
        print("Viúvo!")
    elif (estado_civil == "o"):
        print("Outros!")
    else:
        print("Você digitou uma opção inválida!")