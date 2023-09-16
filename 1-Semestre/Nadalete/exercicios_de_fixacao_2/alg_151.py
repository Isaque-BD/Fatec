peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / altura ** 2

if imc < 20:
    print("\nAbaixo do peso")

elif imc <= 25:
    print("\nNormal")

elif imc <= 30:
    print("\nExcesso de peso")

elif imc <= 35:
    print("\nObesidade")

else:
    print("\nObesidade mórbida")

