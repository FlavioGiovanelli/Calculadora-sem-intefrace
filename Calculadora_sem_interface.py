import math 

def soma(a, b):
    soma = a + b
    return soma 

def sub(a, b):
    sub = a - b
    return sub

def mult(a, b):
    mult = a * b 
    return mult

def div(a, b):
    if b != 0:
        div = a / b
    return div

def pot(a, b):
    return math.pow(a, b)

def raiz(a):
    return math.sqrt(a)


print("----------------------Bem Vindo a calcudora.----------------------")
print()
print("1-Adição")
print("2-Subtração")
print("3-Multiplicação")
print("4-Divisão")
print("5-Potência")
print("6-Raiz")
print("Cancelar")
print()

opcao = input("Digite o número da operação desejada (1/2/3/4/5/6): ")


if opcao not in ['1', '2', '3', '4', '5', '6']:
    print("Opção inválida. Por favor, escolha uma opção válida.")
else:
    
    if opcao in ['1', '2', '3', '4', '5']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    elif opcao == '6':
        num1 = float(input("Digite o número: "))


if opcao == "1":
    resultado = int(soma(num1, num2))

elif opcao == "2":
    resultado = int(sub(num1, num2))

elif opcao == "3":
    resultado = int(mult(num1, num2))

elif opcao == "4":
    resultado = div(num1, num2)

elif opcao == "5":
    resultado = int(pot(num1, num2))

elif opcao == "6":
    resultado = raiz(num1)

else:
    print("Opção inválida")


print("O resultado da operação é:", resultado)



    










