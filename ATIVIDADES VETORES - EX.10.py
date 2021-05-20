#Calcula a UNIÃO entre dois vetores
import random
vetorA = [0]*3
vetorB = [0]*3
n = len(vetorA)
m = len(vetorB)
lista = []

def preencheVetor():
    for x in range(n):
        vetorA[x] = random.randint(0,10)
    print(vetorA)
    for i in range(m):
        vetorB[i] = random.randint(0,10)
    print(vetorB)

def uniãoVetor():
    lista = []
    for x in range(n):
        for x in range(m):
            if vetorA[x] != vetorB[x]:
                if vetorA[x] not in lista:
                    lista.append(vetorA[x])
                if vetorB[x] not in lista:
                    lista.append(vetorB[x])
    print(lista)


preencheVetor()
uniãoVetor()