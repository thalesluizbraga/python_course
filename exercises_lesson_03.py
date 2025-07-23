
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

temperatura = float(input('Digite a temperatura:'))
if temperatura > 26:
    print('alta')
elif temperatura < 18:
    print('baixa')
else:
    print('normal')

#%%

#Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa
#  filtrar mensagens com severidade 'ERROR'. Dado um
#  registro de log em formato de dicionário como
#  log = {'timestamp': '2021-06-23 10:00:00', 'level': 
# 'ERROR', 'message': 'Falha na conexão'}, 
# escreva um programa que imprima a mensagem se a 
# severidade for 'ERROR'.

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level'] == 'ERROR':
    print(log['message'])

#%%

#Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 
# anos e tenha fornecido um email válido.
#  Escreva um programa que valide essas condições e imprima 
# "Dados de usuário válidos" ou o
#  erro específico encontrado.

idade_usuario = 40
email_usuario = 'teste@gmail.com'

if email_usuario.endswith('@gmail.com'):
    if 18 < idade_usuario < 65:
        print('Dados de usuário válidos') 
    else:
        print('Idade invalida')
else:
    print('Email invalido')

#%%

#Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa
#  identificar transações suspeitas. Uma transação é considerada 
# suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do 
# horário comercial (antes das 9h ou depois das 18h). Dada uma
#  transação como transacao = {'valor': 12000, 'hora': 20}, verifique
#  se ela é suspeita.

valor_transacao = 5000
horario_transacao = 10

if valor_transacao > 10000 or horario_transacao < 9 or horario_transacao > 18:
    print('Transação suspeita')
else:
    print('Transação válida')

#%%

#6. Contagem de Palavras em Textos
#Objetivo: Dado um texto, contar quantas vezes cada palavra única
#  aparece nele.

texto = 'um gato dois gatos três gatos'
palavras = texto.split()
contagem_palavras = {} # dicionario vazio para receber a palavra de cada iteraçao

for p in palavras:
    if p in contagem_palavras:
        contagem_palavras[p] += 1
    else:
        contagem_palavras[p] = 1

print(contagem_palavras)

# splitar o texto
# criar lista de palavras
# criar dicionario vazio para receber iteraçoes
# iterar sobre a lista de palavras
# contar palavras repetidas no dicionario

#%%

# 7. Normalização de Dados
# Objetivo: Normalizar uma lista de números para que
#  fiquem na escala de 0 a 1.


# formula da normalizaçao (x - minimo) / (maximo - minimo)

numeros = [10,30,5,59]
min_numeros = min(numeros)
max_numeros = max(numeros)
numeros_normalizados = []

for n in numeros:
    numeros_normalizados.append((n - min_numeros) / (max_numeros - min_numeros))

numeros_normalizados.sort(reverse=False) 
numeros_normalizados

#%%
# 8. Filtragem de Dados Faltantes
# Objetivo: Dada uma lista de dicionários representando dados de
#  usuários, filtrar aqueles que nao têm  um campo específico faltando.


usuarios = [
{"nome": "Alice", "email": "alice@example.com"},
{"nome": "Bob", "email": ""},
{"nome": "Carol", "email": "carol@example.com"}
]
usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]
print(usuarios_validos)


#%%

#9. Extração de Subconjuntos de Dados
#Objetivo: Dada uma lista de números, extrair apenas aqueles que são 
# pares.

lista_numeros = [10,14,23,49,50]
lista_pares = []

for n in lista_numeros:
    if n%2 == 0:
        lista_pares.append(n)
lista_pares

# %%

# 10. Agregação de Dados por Categoria
# Objetivo: Dado um conjunto de registros de vendas, calcular o total
#  de vendas por categoria.

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]
# v1
#total_eletronicos = []
#total_livros = []
#
#for v in vendas:
    #if v['categoria'] == 'eletrônicos':
        #total_eletronicos.append(v['valor'])
    #if v['categoria'] == 'livros':
        #total_livros.append(v['valor'])
#
#print(sum(total_eletronicos))
#print(sum(total_livros))

total_por_categoria = {}

for v in vendas:
    categoria = v['categoria']
    valor = v['valor']
    if categoria in total_por_categoria:
        total_por_categoria[categoria] += valor
    else:
        total_por_categoria[categoria] = valor

total_por_categoria


# criar dicionario vazio para receber iteraçoes
# iterar cada elemento da lista de dicionario que vai ser um dicionario
# criar as chaves e valores do dicionario vazio baseado nas chaves e valores do dicionario existente
# verificar se a chave criada pro dicionario vazio ja estiver no dicionario vazio somar += o valor
# se nao estiver, == valor


#%%
