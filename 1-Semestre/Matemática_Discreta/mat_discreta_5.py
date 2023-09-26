#Utilizando a bicondicional, caso o usuário fazer o login utilizando o mesmo nome como senha ele não poderá entrar.
while True:
    nome = input("Digite seu nome: ") #Primeira entrada do elemento 
    senha = input("Digite sua senha: ") #Segunda entrada do elemento 

    if nome == senha: #Verificação se a senha se iguala com o nome
        print("\nSenha inválida, tente novamente")
    else:
        break

print("Cadastro feito com sucesso!!!!")
