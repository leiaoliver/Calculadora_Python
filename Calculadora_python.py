def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def divisao(a, b):
    return a / b


def multiplicacao(a, b):
    return a * b


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("Operações: ")
print("1 - soma")
print("2 - subtração")
print("3 - Divisão")
print("4 - multiplicação)")

operacao = int(input("Digite o número da operação que irá realizar: "))


resultado = 0

if operacao == 1:
    resultado = soma(num1, num2)
elif operacao == 2:
    resultado = subtracao(num1, num2)
elif operacao == 3:
    resultado = divisao(num1, num2)
elif operacao == 4:
    resultado = multiplicacao(num1, num2)
else:
    print("Operação inválida!")


print("Resultado: ", resultado)
