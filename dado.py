"""Programa para simular as jogadas de um dado"""
from random import randint

def dado(max):
	dado = [0, 0, 0, 0, 0, 0]

	for i in range(0,max):
		a = randint(1,6)
		if a == 1:
			dado[0] += 1
		elif a == 2:
			dado[1] += 1
		elif a == 3:
			dado[2] += 1
		elif a == 4:
			dado[3] += 1		
		elif a == 5:
			dado[4] += 1
		else:
			dado[5] += 1

	return dado		


controle = int(input("Quantidade de testes: "))
lista = dado(controle)

print("cada posição da lista representa uma face do dado em ordem")
print(lista)

print("probabilidade de 1 =", lista[0]/controle)
print("probabilidade de 2 =", lista[1]/controle)
print("probabilidade de 3 =", lista[2]/controle)
print("probabilidade de 4 =", lista[3]/controle)
print("probabilidade de 5 =", lista[4]/controle)
print("probabilidade de 6 =", lista[5]/controle)