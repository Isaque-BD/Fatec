def prova_inducao(k):
    # Caso base: para k = 0
    if k == 0:
        return (2**(3*k) - 1) % 7 == 0

    # Hipótese de indução: supondo que a fórmula é verdadeira para k, mostramos para k + 1
    hipotese_inducao = prova_inducao(k - 1)

    # Passo de indução: mostramos que a fórmula é verdadeira para k + 1
    resultado_k_mais_um = (2**(3*(k + 1)) - 1) % 7 == 0

    # A fórmula é verdadeira para k se e somente se a hipótese de indução for verdadeira e o passo de indução for verdadeiro
    return hipotese_inducao and resultado_k_mais_um

# Testar para alguns valores de k
for k in range(10):
    resultado = prova_inducao(k)
    print(f"Para k = {k}, a fórmula é {resultado}")
