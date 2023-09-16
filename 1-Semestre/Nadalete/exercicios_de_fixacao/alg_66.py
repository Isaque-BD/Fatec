tempo = float(input("\nDigite o tempo gasto: "))
vel = float(input("\nDigite a velocidade média: "))

dist = tempo * vel
litros = dist / 12

print(f"\nVelocidade = {vel},\nTempo = {tempo},\nDistânca = {dist},\nLitros = {litros:.2f}")


