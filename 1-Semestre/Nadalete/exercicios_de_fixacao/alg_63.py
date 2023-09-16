na = int(input("\nHoras trabalhadas: "))
vha = int(input("\nValor da hora-aula: "))
pd = int(input("\nPercentual de desconto: "))

sb = na * vha
td = (pd / 100) * sb
sl = sb - td

print(f"\nSalário líquido: R${sl:.2f}")
