primeiroNum = 0
segundoNum = 1
lista = [primeiroNum, segundoNum]

valor = int(input("Insira o valor: "))

while segundoNum <= valor:
    lista.append(primeiroNum + segundoNum)
    primeiroNum = segundoNum
    segundoNum = lista[-1] # define o segundo número como o último valor da lista

print(lista)

if lista.count(valor) != 0:
    print(f'O número {valor} faz parte da sequência.')
else:
    print(f'O número {valor} não faz parte da sequência.')
