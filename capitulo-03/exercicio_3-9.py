
quantidade_de_dias = int(input("Digite a quantidade de dias: "))
quantidade_de_horas = int(input("Digite a quantidade de horas: "))
quantidade_de_minutos = int(input("Digite a quantidade de minutos: "))
quantos_segundos = int(input("Digite os segundos: "))

dias = quantidade_de_dias * 86400
horas = quantidade_de_horas * 3600
minutos = quantidade_de_minutos * 60
segundos = quantos_segundos

total_em_segundos = (dias + horas + minutos + segundos)

print("Dias, horas, minutos e segundos do usuário em segundos é %5.2f" %total_em_segundos)
