A = 15000
B = 45000
C = 65000 
anos = 0

while True:
    A = A * 1.10
    B = B * 1.05
    anos = anos + 1
    
    if A >= B:
        print(f"A cidade A {anos} anos para passar da cidade B")
        print(A)
        print(anos)
        break

A = 15000
anos = 0

while True:
    
    A = A * 1.10
    
    anos = anos + 1
    
    if  A > C * 1.23:
        print(f"A cidade A demorará {anos} anos para passar da cidade C")
        print(A)
        print(anos)
        break
 
    

        



