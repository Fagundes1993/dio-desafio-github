conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {5, 6, 7, 8}
conjunto_uniao = conjunto_a.union(conjunto_b) #união de conjuntos
conjunto_interseccao = conjunto_a.intersection(conjunto_b) #intersecção de conjuntos
conjunto_diferenca = conjunto_a.difference(conjunto_b) #diferença entre conjuntos
conjunto_dif_simetrica = conjunto_a.symmetric_difference(conjunto_b) #diferença simétrica entre conjuntos

# print('União: {}'.format(conjunto_uniao))
# print('Intersecção: {}'.format(conjunto_interseccao))
# print('Diferença: {}'.format(conjunto_diferenca))
# print('Diferença simétrica: {}'.format(conjunto_dif_simetrica))

#Conceitos de pertinência
#Subset = Subconjunto

conjunto_c = {1, 2, 3}
conjunto_d = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_c.issubset(conjunto_d) #True
print(conjunto_subset)

conjunto_superset = conjunto_d.issuperset(conjunto_c) #true
print(conjunto_superset)

#Remover dplicidade da lista convertendo-a em um conjunto

lista = ['dog', 'dog', 'cat', 'cat', 'elephant']
conjunto_animais = set(lista)
print(conjunto_animais)
# conjunto = {1, 2, 3, 4} #declaração de conjunto
# conjunto.add(5) #Adição de elemento ao conjunto
# conjunto.discard(2) #remoção de elemento no conjunto