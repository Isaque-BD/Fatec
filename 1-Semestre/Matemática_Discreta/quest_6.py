print("\n\nProblema: 1² + 2² + 3² +...+ n² = (n/6).(n + 1).(2n + 1), onde qualquer 'n' >= 1\nProve através da indução que isso é verdade")

# Caso base
print("\n1 - Base")
while True:
    try:
        n = int(input("\nDigite o número base (n >= 1): "))
        if n >= 1:
            break
        else:
            print("O número deve ser maior ou igual a 1. Tente novamente.")
    except ValueError:
        print("Tente apenas números inteiros.")

ladoDireito = n**2
ladoEsquerdo = (n/6) * (n + 1) * (2*n + 1)

if ladoDireito == ladoEsquerdo:
    print("\nPortanto, a base é verdadeira.")
else:
    print("\nPortanto, a base é falsa.")
    print("Pelo P.P.I.M, P(n) não é satisfeito.")

# Passo indutivo
print("\n2 - Indução")

# Hipótese
print("Suponha que k² = (k/6).(k + 1).(2k + 1) para algum k.")

# Tese
print("Mostrar que (k+1)² = ((k+1)/6).(k + 2).(2k + 3)")

# Calcular o lado direito da tese
teseDireita = ((n + 1) / 6) * (n + 2) * (2 * n + 3)

# Calcular o lado esquerdo da tese
teseEsquerda = (n / 6) * (n + 1) * (2 * n + 1) + (n + 1)**2

if teseDireita == teseEsquerda:
    print("\nPelo P.P.I.M, P(n) é satisfeita para k+1.")
else:
    print("\nPortanto, a tese é falsa.")
    print("Pelo P.P.I.M, P(n) não é satisfeito para k+1.")
