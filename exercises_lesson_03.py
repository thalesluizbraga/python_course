#%%

# 1- Você está analisando um conjunto de dados de vendas e precisa 
# garantir que todos os registros tenham valores positivos para
#  quantidade e preço. Escreva um programa que verifique esses
#  campos e imprima "Dados válidos" se ambos forem positivos ou
#  "Dados inválidos" caso contrário.

preco = float(input("Digite o preço do produto: "))
if preco > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")

#%%

# 2- Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de
#  temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'.
#  Considerando que:Exercício 2: 
# Temperatura < 18°C é 'Baixa'
#Temperatura >= 18°C e <= 26°C é 'Normal'
#Temperatura > 26°C é 'Alta'

temperatura = float('Digite a temperatura:')
if temperatura > 26:
    print('alta')
elif temperatura < 18:
    print('baixa')
else:
    print('normal')


