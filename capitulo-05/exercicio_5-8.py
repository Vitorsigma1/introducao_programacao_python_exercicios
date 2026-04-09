
num1 = int(input("Digite o primeiro número: "))#É a primeira entrada de dados
num2 = int(input("Digite o segundo número: ")) #É a segunda entrada de dados

resultado = 0 #É o Acumulador deve começar do Zero

for _ in range(num1): #Cria uma sequência que vai de Zero até num1
                      #se num1 for 5 o Loop roda cinco vezes
                      #o _ underline no 'for' serve para não usar o valor do contador dentro do 'Loop'
    resultado = resultado + num2 #adiciona o num2 ao resultado

print("O resultado da multiplicação é:%6.2f" % resultado) #temos a Saída da nossa multiplicação
    
    
    

    

