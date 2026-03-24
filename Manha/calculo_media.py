n1 = float(input("Digite a primeira nota"))
n2 = float(input("Digite a segunda nota"))
n3 = float(input("Digite a terceira nota"))
media = (n1+n2+n3)/3

if (media >= 7):
    print(f"Parabéns, você foi Aprovado com a média {media}")
elif (media >= 5):
    print(f"Você está de Recuperação com a média {media}")
else:
    print(f"Você está Reprovado, com a média {media}")