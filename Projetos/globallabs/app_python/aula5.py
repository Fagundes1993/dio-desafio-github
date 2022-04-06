lista = [12, 10, 7, 5] #declaração de lista numérica
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara'] #declaração de lista de caracteres

tupla = (1, 10, 12, 14) #declaração de tupla (não permite alteração)

# print(len(tupla)) #imprime o numero de elemento da tupla/lista

tupla_animal = tuple(lista_animal) # conversão de uma lista em uma tupla
lista_numerica = list(tupla) #conversão de tupla em lista)
# lista.sort() #ordena a lista em ordem crescente
# lista_animal.sort() #ordena a lista em ordem crescente
#
# print(lista)
# print(lista_animal)
#
# lista.reverse() #ordena a lista em ordem decrescente
# lista_animal.reverse() #ordena a lista em ordem decrescente
#
# print(lista)
# print(lista_animal)

# #Imprime o elemento da lista através da posisção
# print(lista_animal[1])
#
# #imprime os elementos da lista
# for x in lista_animal:
#     print(x)
#
# #imprime o somatório dos elementos da lista
# print(sum(lista))
#
# #imprime o maior elemento da lista
# print(max(lista))
#
# #imprime o menor elemento da lista
# print(min(lista))

#Verifica se o elemento está na lisra
# if 'lobo' in lista_animal:
#     print('Existe um lobo na lita')
# else:
#     print('Não existe um lobo na lista')
#     lista_animal.append('lobo') #adição do elemento lobo na lista
#     print(lista_animal)
#
#
# lista_animal.pop() #remove o ultimo elemento da lista
# lista_animal.remove('elefante') #remove o elemento da lista informado
# print(lista_animal)
# #Nova lista criada com a multiplicação dos elementos por 3
# nova_lista = lista_animal * 3
# print(nova_lista)