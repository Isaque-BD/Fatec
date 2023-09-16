x = float(input("Dite o valor de x: "))
fx = (5 * x + 3) / (x**2 - 16) ** (1/2)

if x > 4 or x < -4:
    print(f"\nf(x) = {fx}")

else:
    print("\nNão pode ser feita")

    