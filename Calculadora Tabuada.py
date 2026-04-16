numero = int(input("Digite o numero para Tabuada"))
while numero <0:
    print("Numero Invalido")
    numero = int(input("Digite um numero positivo para realizar a tabuada: "))
else:
    print("Numero Valido")
for contador in range(1,11):
    resultado = contador * numero
    print("Resultado = ", resultado)
