# Problema: A soma dos n primeiros termos de uma PG é dada por S = a * (1 - r^n) / (1 - r), onde a é o primeiro termo e r é a razão.
# Provar por indução matemática.

# Caso base
n_base = int(input("Digite o número base (n >= 1): "))
a = int(input("Digite o primeiro termo da PG: "))
r = int(input("Digite a razão da PG (r != 1): "))

# Verificar se a razão é diferente de 1 para evitar divisão por zero
if r == 1:
    print("A razão não pode ser 1. Escolha outra razão.")
    exit()

base_right = a * (1 - r**n_base) / (1 - r)  # Fórmula da soma dos n primeiros termos de uma PG
base_left = sum(a * r**i for i in range(n_base))  # Soma dos n primeiros termos da PG

if base_right == base_left:
    print("Base verdadeira.")
else:
    print("Base falsa. Pelo P.P.I.M, P(n) não é satisfeito.")

# Passo indutivo
print("\nPasso Indutivo:")

# Hipótese
print("Suponha que a soma dos k primeiros termos de uma PG é dada por S = a * (1 - r^k) / (1 - r) para algum k.")

# Tese
print("Mostrar que a soma dos (k + 1) primeiros termos de uma PG é dada por S = a * (1 - r^(k+1)) / (1 - r)")

# Calcular o lado direito da tese
tese_direita = a * (1 - r**(n_base + 1)) / (1 - r)

# Calcular o lado esquerdo da tese
tese_esquerda = base_left + a * r**n_base

if tese_direita == tese_esquerda:
    print("Tese verdadeira. Pelo P.P.I.M, P(n) é satisfeito para k + 1.")
else:
    print("Tese falsa. Pelo P.P.I.M, P(n) não é satisfeito para k + 1.")
