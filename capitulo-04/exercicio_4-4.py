
sal_func = float(input("Digite o valor do seu salário: "))

if sal_func > 1250:
    dez_novo_salario = (sal_func * 0.10) + sal_func
    print("Seu novo salário será de R$%6.2f" % dez_novo_salario)

if sal_func <= 1250:
    quinze_novo_salario = (sal_func * 0.15) + sal_func
    print("Seu novo salário será de R$%6.2f" % quinze_novo_salario)

