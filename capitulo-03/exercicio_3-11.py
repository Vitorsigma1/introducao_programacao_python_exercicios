
preco_mercadoria = float(input("Qual é o preço da mercadoria? "))
percent_desconto = float(input("Qual é o percentual de desconto? "))

desconto = (preco_mercadoria * percent_desconto) / 100
preco_pagar = preco_mercadoria - desconto

print("O valor de desconto R$%5.2f" % desconto, "e o preço da mercadoria R$%5.2f" % preco_pagar)
      
