n1 = 0 
n2 =0
x = 0
numero = int(input("Digite um número inteiro >=50: "))

if numero >= 50:
    for i in range(numero):
        
        x += 1
        
        if (x % 2) == 0 or x == 0 or x == 1:
            n1 += (x*2-1)/x
        else:
            n2 -= (x*2-1)/x

    H = n1 + n2
    print(f"O resultado dessa conta será {H}")


else:
    print("tente novamente digitando um número >=50")

