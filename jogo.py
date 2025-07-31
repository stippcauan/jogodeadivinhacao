import random
print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")
print("🟩   JOGO DE AVALIAÇÃO   I")
print("🟩                       I")
print("🟩         CAUAN         I")
print("🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩")

numeroSecreto= random.randrange(0,100)
totalTentativas = 0
pontos = 100

print("Qual o níveis de dificuldade?")
print("")
print("(1)-Fácil (2)- Médio (3)- Difícil ")
print("")
nível = int(input("Escolha um nível"))
print("")
if (nível == 1):
    print(" Você tem 20 tentativas IXE É NOVATO CAGÃO")
    totalTentativas = 20
elif (nível == 2):
    print(" Você tem 10 tentativasOLHA JA TEM UM POUCO DE CORRAGEM ")
    totalTentativas = 10
elif (nível == 3):
    print("Você tem 5 tentativas Ó AI SIM VETERANO CORAJOSO ")
    totalTentativas = 5
else:
    print("número invalido")
    totalTentativas = 0