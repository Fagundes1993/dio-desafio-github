a = int(input('Primeiro semestre: '))
if a > 10:
    a = int(input('Nota inválida. Primeiro bimestre: '))
b = int(input('Segundo semestre: '))
if b > 10:
    b = int(input('Nota inválida. Segundo bimestre: '))
c = int(input('Terceiro semestre: '))
if c > 10:
    c = int(input('Nota inválida. Terceiro bimestre: '))
d = int(input('Quarto semestre: '))
if d > 10:
    d = int(input('Nota inválida. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('Media: {}'.format(media))

# a = int(input('Entre com primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um número par')
# else:
#     print('Não foi digitado número par')

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))
# print('Final do programa')