
numero_um = float(input("Digite um número: "))
numero_dois = float(input("Digite outro número: "))
operacao = input("Qual Operação deseja fazer +, -, *, /? ")

if operacao == '+':
    resultado = numero_um + numero_dois

elif operacao == '-':
    resultado = numero_um - numero_dois

elif operacao == '*':
    resultado = numero_um * numero_dois

elif operacao == '/':
    resultado = numero_um / numero_dois

print("O resultado da sua conta é: R$%6.2f" % resultado)



