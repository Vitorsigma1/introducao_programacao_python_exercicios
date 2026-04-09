
num1 = int(input("Digite o primeiro número: "))#dividendo
num2 = int(input("Digite o segundo número: "))#divisor

quociente = 0

while num1 >= num2:
    num1 = num1 - num2
    quociente = quociente + 1

print("O resultado da divisão é:%6.2f" % quociente)

