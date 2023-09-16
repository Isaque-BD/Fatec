saldomedio = float(input("Digite o saldo medio: "))

if saldomedio < 501:
    credito = 0

elif saldomedio < 1001:
    credito = saldomedio * 0.3

elif saldomedio < 3001:
    credito = saldomedio * 0.4

else:
    credito = saldomedio * 0.5

if credito != 0:
    print(f"\nComo seu saldo era de: {saldomedio}, seu crédito será de: {credito}")

else:
    print(f"\nComo seu saldo era de: {saldomedio}, seu crédito será de: {credito}")
