quant = float(input("Digite a quantidade de fitas: "))
vaAluguel = float(input("\nDigite o valor do aluguel: "))
fatAnual = quant/3 * vaAluguel * 12

print(f"\nFaturamento anual: {fatAnual}")

multas = vaAluguel * 0.1 * (quant/3)/10

print(f"\nMultas mensais: {multas}")

quantFinal = quant - quant * 0.02 + quant / 10

print(f"\nQuantidade de fitas no final do ano: {quantFinal}")




