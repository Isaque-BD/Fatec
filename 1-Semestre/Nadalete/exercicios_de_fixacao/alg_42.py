import math

angulo = float(input("\nDigite um ângulo em graus: "))
rang = math.pi*angulo / 180

print(f"\nSeno: {math.sin(rang)}")
print(f"\nCosseno: {math.cos(rang)}")
print(f"\nTangente: {math.tan(rang)}")
print(f"\nCossecante: {1/math.sin(rang)}")
print(f"\nSecante: {1/math.cos(rang)}")
print(f"\nCotangente: {1/math.tan(rang)}")

