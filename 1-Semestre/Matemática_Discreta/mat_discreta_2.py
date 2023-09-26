#Declarando os elementos do conjunto
a = ["honda", "fiat", "uno", "ferrari"]

#Entrada do elemento
carro = input("Escolha um carro que deseja: ").lower()

#Utilizando uma condição para verificar se o elemento pertence
#ao conjunto A
if carro in a:
    print("Esse carro contém no nosso estoque")
else:
    print("Esse carro não contém no nosso estoque")
 
