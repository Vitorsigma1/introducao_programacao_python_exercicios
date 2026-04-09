
# Entrada de Dados
deposito_inicial = float(input("Qual é o valor do depósito inicial: R$ "))
taxa_juros = float(input("Qual é o valor da taxa de juros (ex: 0.5 para 0.5%): "))

# Inicialização de Variáveis
mes = 1 # Contador
saldo = deposito_inicial # Acumulador

# Imprimir cabeçalho dos valores mês a mês
print(f"\nEvolução da Poupança: ") # \n é para pular linha - O 'f' vem de format
# e o Python entende que não é só uma frase e sim um modelo que pode conter
# cálculos e variáveis
print("_" * 30) # Gera 30 hífens sublinhando o cabeçalho

# Estrutura de repetição para os 24 meses
while mes <= 24:
    # Cálculo dos juros do mês atual (Mostra o que é o juros do mês!)
    juros_do_mes = saldo * (taxa_juros / 100)
    # Atualização do saldo (Que é o Acumulador!)
    saldo = saldo + juros_do_mes
    
    print(f"Mês {mes:02d}: R$ {saldo:8.2f}") # O 'f' vem de format e o Python
    #entende que não é só uma frase e sim um modelo que pode conter cálculos e
    #variáveis

    # Incremento do contador
    mes = mes + 1

# Calculo do total de ganho apenas com juros
total_ganho_juros = saldo - deposito_inicial

print("_" * 30) # Gera 30 hífens sublinhando e separando o cabeçalho
print(f"Valor total ganho com juros no período: R$ {total_ganho_juros: 0.2f}")
# O 'f' vem de format e o Python entende que não é só uma frase e sim um modelo
# que pode conter cálculos e variáveis

print(f"Valor total acumulado: R$ {saldo: 0.2f}") # O 'f' vem de format e o
#Python entende que não é só uma frase e sim um modelo que pode conter cálculos e
#variáveis


