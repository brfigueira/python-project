estado_civil = input("Digite a letra que representa \n" \
"seu estado civil \n" \
"C. Casado\n" \
"S. Solteiro\n" \
"D. Divorciado\n" \
"V. Viúvo\n" \
"O. Outros\n"
"------>")

if (estado_civil=="C" or estado_civil=="c"):
    print("Casado")
elif (estado_civil=="D" or estado_civil=="d"):
    print("Divorciado")
elif (estado_civil=="S" or estado_civil=="s"):
    print("Solteiro")
elif (estado_civil=="V" or estado_civil=="v"):
    print("Viúvo")
elif (estado_civil=="O" or estado_civil=="o"):
    print("Outros")
else:
    print("Você digitou uma opção inválida!")
    