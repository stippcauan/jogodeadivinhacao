import random
print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")
print("🟩   JOGO DE AVALIAÇÃO   I")
print("🟩                       I")
print("🟩         CAUAN         I")
print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")

numeroSecreto= random.randrange(0,100)
totalTentativas = 0
pontos = 100

print("Qual os níveis de dificuldade?")
print("")
print("(1)-Fácil (2)- Médio (3)- Difícil ")
print("")
nível = int(input("Escolha um nível"))
print("")
if (nível == 1):
    print(" Você tem 20 tentativas. IXE É NOVATO CAGÃO")
    totalTentativas = 20
elif (nível == 2):
    print(" Você tem 10 tentativas. OLHA JA TEM UM POUCO DE CORRAGEM ")
    totalTentativas = 10
elif (nível == 3):
    print("Você tem 5 tentativas. Ó AI SIM VETERANO CORAJOSO ")
    totalTentativas = 5
else:
    print("número invalido")

for rodada in range (1, totalTentativas +1 ): 
    print("Tentativa {} de {}". format(rodada, totalTentativas ))
    chute_str = input("Digite um número entre 1 e 100: ")
    chute =(chute_str)

    if(chute < 1 or chute > 100):
        print("Número invalido")
        continue 

    acertou = chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto

    if(acertou):
        print(f"Você acertou e fez {pontos}! ")
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto")

            pontosPerdidos = abs(numeroSecreto - chute)
            pontos = pontos - pontosPerdidos
            
print("Fim de jogo ! O número era ", numeroSecreto)