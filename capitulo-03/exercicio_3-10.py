
salario = int(input("Qual é o valor do seu Salário? "))
porcentagem = int(input("Qual é a porcentagem de aumento? "))

aumento = (salario * porcentagem) / 100
salario_novo = salario + aumento

print("O valor do aumento é R$%5.2f" %aumento, "e o novo salário é R$%5.2f" %salario_novo)
      
