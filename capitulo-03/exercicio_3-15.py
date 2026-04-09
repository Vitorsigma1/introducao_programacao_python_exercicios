
cigarros_dia = int(input("Quantos cigarros você fuma por dia? "))
fuma_anos = int(input("Quantos anos você é fumante? "))

dias_fumados = cigarros_dia * (fuma_anos * 365)
total_cigarros = dias_fumados * 10
dias_perdidos = total_cigarros / 1440

print("O fumante já perdeu %2.2f" %dias_perdidos, "dias de vida!")
