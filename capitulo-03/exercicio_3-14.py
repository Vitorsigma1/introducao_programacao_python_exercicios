
km_percorrido = float(input("Digite quantos kilometros foram percorridos com o carro: "))
dias_alugado = float(input("Digite por quantos dias você alugou o carro: "))

preco_pagar = (km_percorrido * 0.15) + (dias_alugado * 60.00)

print("O preço pelo aluguel do carro é R$%2.2f" %preco_pagar)
