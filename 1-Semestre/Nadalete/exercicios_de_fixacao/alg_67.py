valor = float(input("\nDigite o valor da prestação: "))
taxa = float(input("\nDigite a taxa: "))
tempo = int(input("\nDigite o tempo(número de meses): "))

prest = valor + (valor*(taxa / 100) * tempo)

print(f"\nO valor da prestação em atraso é = R${prest}")
