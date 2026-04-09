
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
#Nas variáveis 'a' e 'b' temos a entrada de dados

resultado_deve_ser_negativo = (a < 0 and b > 0) or (a > 0 and b < 0)
#1 passo: é descobrir se o resultado final deve ser negativo

a_limpo = abs(a)
b_limpo = abs(b)
#2 passo: "limpar" os números (deixar ambos os números positivos)
#Usamos a função abs() que transforma -5 em 5

resultado = 0
for _ in range(a_limpo):
    resultado = resultado + b_limpo
#3 - passo: aplicar a mesma lógica sucessiva que eu já use e aprendi

if resultado_deve_ser_negativo:
    resultado = 0 - resultado
#4 - passo: aplicar o sinal se for necessário
#transforma o positivo em negativo usando subtração

print("O resultado da multiplicação é: %6.2f" % resultado)

