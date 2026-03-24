idade = int(input("Digite a sua idade: "))

if (idade >= 18):
    print(f"Você tem {idade} anos, e é um adulto!")
elif (idade >= 12):
    print(f"Você tem {idade} anos, e é um adolescente!")
else:
    print(f"Você tem {idade} anos, e é uma criança!")