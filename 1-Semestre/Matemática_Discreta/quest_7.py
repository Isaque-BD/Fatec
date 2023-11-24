# Problema: 1 + 2 + 3 + ... + n = n * (n + 1) / 2, para qualquer n >= 1
# Provar por indução matemática.

# Caso base
n_base = int(input("Digite o número base (n >= 1): "))
base_right = sum(range(1, n_base + 1))
base_left = n_base * (n_base + 1) / 2

if base_right == base_left:
    print("Base verdadeira.")
else:
    print("Base falsa. Pelo P.P.I.M, P(n) não é satisfeito.")

# Passo indutivo
print("\nPasso Indutivo:")

# Hipótese
print("Suponha que 1 + 2 + 3 + ... + k = k * (k + 1) / 2 para algum k.")

# Tese
print("Mostrar que 1 + 2 + 3 + ... + (k + 1) = (k + 1) * ((k + 1) + 1) / 2")

# Calcular o lado direito da tese
tese_direita = (n_base + 1) * (n_base + 2) / 2

# Calcular o lado esquerdo da tese
tese_esquerda = base_left + (n_base + 1)

if tese_direita == tese_esquerda:
    print("Tese verdadeira. Pelo P.P.I.M, P(n) é satisfeito para k + 1.")
else:
    print("Tese falsa. Pelo P.P.I.M, P(n) não é satisfeito para k + 1.")
