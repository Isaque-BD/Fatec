num = float(input("\nEntre com um número com a parte fracionaria: "))
numi = int(num)
numfrac = num - numi
numa = int(num + 0.00001)
 
print(f"\nParte inteira: {numi}")
print(f"\nParte fracionaria: {numfrac + 0.00001:.3f}")
print(f"\nNúmero arredondado: {numa}")
