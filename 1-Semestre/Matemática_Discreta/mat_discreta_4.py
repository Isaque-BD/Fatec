certificado = ["administração", "engenharia", "programação"]

formacao1= input("\nPara passar na você tem que ter pelo menos 2 formações, sendo {} Digite sua primeira formação: ".format(certificado)).lower()
formacao2 = input("\nDigite sua segunda formação: ").lower()

#Verificação dos dados, se eles pertencem no comjunto, utilizando o fator de duas condições para a verificação.

if (formacao1 and formacao2) in certificado:
    print("\nParabéns você conseguiu a vaga")
else:
    print("\nInfelizmente você não conseguiu a vaga")
