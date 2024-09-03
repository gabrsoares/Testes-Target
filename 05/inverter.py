texto = input("Insira o texto a ser revertido: ")
lista_texto = list(texto) # precisa converter pra lista para realizar mudanças

for x in range(len(lista_texto) // 2): # lista percorrida até a metade pois se for até o fim, ele reverte a ordem pro estado original
    lista_texto[x], lista_texto[-(x+1)] = lista_texto[-(x+1)], lista_texto[x] # inverte a posição do elemento com o seu oposto (0 com -1, 1 com -2...)
texto_convertido = ''.join(lista_texto) # converte a lista de volta para texto
print(texto_convertido)