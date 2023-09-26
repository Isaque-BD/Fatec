A = [1, 2, 5, 9]
B = [3, 5, 9, 11]

#Fazendo a diferença de dados, ou seja A - B, e sua saída 
C = [item for item in A if item not in B]

#Fazendo B - A
D = [item for item in B if item not in A]

print(C)
print(D) 