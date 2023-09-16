import math

num = float(input("\nEntre com o logaritmando: "))
base = float(input("\nEntre com a base> "))
logaritmo = math.log(num) / math.log(base)

print(f"\nO logaritmo de {num} na base {base} é {logaritmo}")