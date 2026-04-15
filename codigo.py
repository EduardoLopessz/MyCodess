peso = float(input("Digite o seu peso = "))
if peso < 40:
    print("Peso palha")
elif peso >= 40 and peso < 60:
    print("Peso pluma")
elif peso >= 60 and peso < 76:
    print("Peso Leve")
elif peso >= 76 and peso < 88:
    print("Peso Pesado")
else:
    print("Peso Super Pesado")
    