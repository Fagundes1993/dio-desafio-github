#Função é tudo aquilo que retorna um valor
#Método não retorna um valor, no Python o Método é conhecido como Definição

# def soma(a, b):
#     return a + b
#
# def subtracao(a, b):
#     return a - b
#
# def multiplicacao(a, b):
#     return a * b
#
# def divisao(a, b):
#     return a / b
#
# print(soma(1, 2))
# print(subtracao(3,4))
# print(multiplicacao(5, 6))
# print(divisao(8, 7))

# Por convenção as classes começam com letra maiuscula

class Calculadora:
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.divisao())
    print(calculadora.multiplicacao())