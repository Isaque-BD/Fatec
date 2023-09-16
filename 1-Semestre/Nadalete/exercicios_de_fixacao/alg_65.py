import math

altura = float(input("\nDigite a altura da alta: "))
raio = float(input("\nDigite o raio da lata: "))

volume = math.pi * raio ** 2 * altura

print(f"\nO volume da lata é = {volume:.2f}")

