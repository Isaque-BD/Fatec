sm = float(input("\nEntre com o salário mínimo: "))
qtadade = float(input("\nEntre com a quantidade em quilowatt: "))
preco = sm/700
vp = preco * qtadade
vd = vp * 0.9

print(f"\nPreço do quilowatt: {preco:.2f}, \nvalor a ser pago {vp:.2f}, \nvalor do desconto {vd:.2f}")