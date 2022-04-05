a = int(input('Primeiro semestre: '))
while a > 10:
    a = int(input('Nota inválida. Primeiro bimestre: '))
b = int(input('Segundo semestre: '))
while b > 10:
    b = int(input('Nota inválida. Segundo bimestre: '))
c = int(input('Terceiro semestre: '))
while c > 10:
    c = int(input('Nota inválida. Terceiro bimestre: '))
d = int(input('Quarto semestre: '))
while d > 10:
    d = int(input('Nota inválida. Quarto bimestre: '))

media = (a + b + c + d) / 4
print('Media: {}'.format(media))

# nota = int(input('Entre com a nota: '))
# while nota > 10:
#     nota = int(input('Nota inválida. Entre com a nota correta: '))
# print(nota)

# a = 0
# while a <= 10:
#     print(a)
#     a +=1

# for num in range(101):
#     div = 0
#     for x in range (1, num+1):
#         resto = num % x
#         if resto == 0:
#             div += 1
#     if div == 2:
#         print(num)

# a = int(input('Informe o número: '))
# div = 0
#
# for x in range(1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div += 1
#
# if div ==2:
#     print('O número {} é primo'.format(a))
# else:
#     print('O número {} não é primo'.format(a))