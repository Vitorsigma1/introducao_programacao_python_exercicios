
distancia = int(input("Quantos quilômetros que você vai percorrer em sua viagem? "))

if distancia <= 200:
    viagem_menor = (distancia * 0.50)
    
    print("O preço da passagem será de R$%6.2f" % viagem_menor)

else:
    viagem_maior = (distancia * 0.45)
    print("O preço da viagem será de R$%6.2f" % viagem_maior)
    
 
