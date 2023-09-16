conta = int(input("Digite conta de três dígitos: "))

d1 = conta // 100
d2 = conta % 100 // 10
d3 = conta % 100 % 10
inv = (d3 * 100) + (d2 * 10) + d1
soma = conta + inv

d1 = (soma // 100) 
d2 = (soma % 100 // 10) 
d3 = (soma % 100 % 10) 
digito = (d1*1 + d2*2 + d3*3) 

print(f"\nDígito verificador: {digito:.0f}")
print(soma)
