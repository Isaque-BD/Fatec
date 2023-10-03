salario_fixo = float(input("Digite o valor do salário fixo: "))
valor_vendas = float(input("Digite o valor das vendas efetuadas: "))


salario_porcentagem_1 = (valor_vendas + salario_fixo) * 1.05
salario_porcentagem_2 = (valor_vendas + salario_fixo) * 1.12

if salario_fixo <= 1500:
    print(f"Seu salário final será de {salario_porcentagem_1}")

else:
    print(f"Seu salário total será de {salario_porcentagem_2}")
    
