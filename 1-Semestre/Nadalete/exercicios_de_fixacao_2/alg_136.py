nome = str(input("Entre com nome: "))
idade = int(input("Entre com a idade: "))

if idade <= 10:
    print(f"\n{nome} pagará R$60,00")

elif idade <= 29:
    print(f"\n{nome} pagará R$120,00")

elif idade <= 59:
    print(f"\n{nome} pagará R$150,00")

elif idade <= 65:
    print(f"\n{nome} pagará R$250,00")

else:
    print(f"\n{nome} pagará R$400,00")
    
