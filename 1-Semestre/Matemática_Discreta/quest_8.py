# Problema: A soma dos n primeiros termos de uma PA é dada por S = n/2 * (2a + (n-1)d), onde a é o primeiro termo e d é a razão.
# Provar por indução matemática.

# Caso base
n_base = int(input("Digite o número base (n >= 1): "))
a = int(input("Digite o primeiro termo da PA: "))
d = int(input("Digite a razão da PA: "))

base_right = sum(range(a, a + n_base * d, d))  # Soma dos n primeiros termos da PA
base_left = n_base / 2 * (2 * a + (n_base - 1) * d)  # Fórmula da soma dos n primeiros termos de uma PA

if base_right == base_left:
    print("Base verdadeira.")
else:
    print("Base falsa. Pelo P.P.I.M, P(n) não é satisfeito.")

# Passo indutivo
print("\nPasso Indutivo:")

# Hipótese
print("Suponha que a soma dos k primeiros termos de uma PA é dada por S = k/2 * (2a + (k-1)d) para algum k.")

# Tese
print("Mostrar que a soma dos (k + 1) primeiros termos de uma PA é dada por S = (k + 1)/2 * (2a + kd)")

# Calcular o lado direito da tese
tese_direita = (n_base + 1) / 2 * (2 * a + n_base * d)

# Calcular o lado esquerdo da tese
tese_esquerda = base_left + (a + n_base * d)

if tese_direita == tese_esquerda:
    print("Tese verdadeira. Pelo P.P.I.M, P(n) é satisfeito para k + 1.")
else:
    print("Tese falsa. Pelo P.P.I.M, P(n) não é satisfeito para k + 1.")
