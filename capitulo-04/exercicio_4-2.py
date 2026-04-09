
velocidade_carro = int(input("Digite a velocidade do carro: "))

if velocidade_carro > 80:
    multa = (velocidade_carro - 80) * 5

    print("Você foi multado. O valor da multa é de R$%2.2f" % multa)

if velocidade_carro <= 80:

    print("Não ultrapasse a velocidade permitida 80km/h sujeito a multa!")
 
