op = int(input("Digite \n1 - Região Norte \n2 - Região Nordeste \n3 - Região Centro-Oeste \n4 - Região Sul: \n"))

iv = int(input("\nDigite 1 - Ida \n2 - Ida e Volta: "))

if op == 1:
    if iv == 1:
        print("\nO valor da passagem de ida para R.Norte R$500,00")
    else:
        print("\nO valor da passagem de ida-volta para R.Norte: R$950,00")

elif op == 2:
    if iv == 1:
        print("\nO valor da passagem de ida para R.Nordeste: R$350,00")
    else:
        print("\nO valor da passagem de ida-volta para R.Nordeste: R$650,00")

elif op == 3:
    if iv == 1:
        print("\nO valor da passagem de ida para R.C.Oeste: R$350,00")
    else:
        print("\nO valor da passagem de dia-volta para R.C.Oeste: R$600,00")

elif op == 4:
    if iv == 1:
        print("\nO valor da passagem de ida para R.Sul: R$300,00")
    else:
        print("\nO valor de ida-volta para R.Sul: R$550,00")

else:
    print("\nOpção Inexistente")


