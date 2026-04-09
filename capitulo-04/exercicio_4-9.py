
#Qual o valor da casa?#

#Qual é o seu salário?#

#Em quantos anos você vai pagar?#

#Calcular o valor da prestação = valor da casa/numero prestações.#

#A prestação não pode ser maior que 30% do salário!#


valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o valor do seu Salário: "))
prestacao = float(input("Digite em quantas prestações você vai pagar a casa: "))

valor_prestacao = valor_casa / prestacao

if valor_prestacao < (salario * 0.30):
    print("Empréstimo aprovado!")
    
else:
    print("Empréstimo não foi aprovado!")


        
