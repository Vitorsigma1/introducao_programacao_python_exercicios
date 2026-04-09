
#Quantos kWh você consimiu esse mês?#

#Qual o tipo de instalação você utiliza?#
#R - residências, I - indústrias, C - comércio#


#Calcular o preço a pagar conforme tabela:#

#Preço por Tipo e Faixa de consumo#

#*** Tipo ***    *** Faixa (kWh)***    *** Preço ***#

#Residencial_____até 500 acima 500_____R$0,40__R$0,65#

#Comercial_______até 1000 acima 1000___R$0,55__R$0,60#

#Industrial______até 5000 acima 5000___R$0,55__R$0,60#

quantidade_kwh = float(input("Digite a quantidade de kWh você consumiu esse mês?"))
instalacao = input("Que tipo de instalação utiliza (R)residencial, (C)comercial ou (I)industrial?")

if instalacao == "R":
    if quantidade_kwh < 500:
        preco = 0.40
        
    else:
        preco = 0.65
        
elif instalacao ==  "C":
    if quantidade_kwh < 1000:
        preco = 0.55

    else:
        preco = 0.60

elif instalacao == "I":
    if quantidade_kwh < 5000:
        preco = 0.55

    else:
        preco = 0.60

print("O valor da sua energia elétrica é R$%6.2f" %(quantidade_kwh * preco))




                   
                       
