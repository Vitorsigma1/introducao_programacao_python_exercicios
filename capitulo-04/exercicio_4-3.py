
prim_numero = int(input("Digite um número: "))
secon_numero = int(input("Digite outro número: "))
terc_numero = int(input("Digite mais um número: "))

if prim_numero > secon_numero and prim_numero > terc_numero:
    print("O primeiro número é maior! %6.2f" % prim_numero)

if prim_numero < secon_numero and prim_numero < terc_numero:
    print("O primeiro número é menor! %6.2f" % prim_numero)

if secon_numero > prim_numero and secon_numero > terc_numero:
    print("O segundo número é maior! %6.2f" % secon_numero)

if secon_numero < prim_numero and secon_numero < terc_numero:
    print("O segundo número é menor! %6.2f" % secon_numero)

if terc_numero > prim_numero and terc_numero > secon_numero:
    print("O terceiro número é maior! %6.2f" % terc_numero)

if terc_numero < prim_numero and terc_numero < secon_numero:
    print("O terceiro número é menor! %6.2f" % terc_numero)

    
