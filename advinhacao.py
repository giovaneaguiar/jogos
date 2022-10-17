print("********************************")
print("Bem vindo ao jogo de Advinhação!")
print("********************************")

numero_secreto = 13

chute_str = input("Digite o seu número: ")
print("Você digitou ", chute_str)
chute = int(chute_str)

if numero_secreto == chute:
    print("Você acertou o número secreto!")
else:
    print("Você errou o número secreto!")