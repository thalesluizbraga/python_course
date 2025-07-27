#%%
# 1- Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista_numeros = []
for i in range(1,11,1):
    lista_numeros.append(i)

for n in lista_numeros:
    print(n**2)

#%%

# 2- Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
lista_linguagens: list = ["Python", "Java", "C++", "JavaScript"]

# Usando o loop
for linguagem in range(len(lista_linguagens)): # Pass o for linguagem in range da lista pra transformar os elementosz da lista em indices
    if lista_linguagens[linguagem] == 'C++': # Se o elemento for c++, substitui por ruby
        lista_linguagens[linguagem] = 'Ruby'
print(lista_linguagens)

# Usando enumerate (que retornar o index e o elemento da lista... ideal pra automatizar alteraçoes baseadas na posicao do elemento)
for index, linguagem in enumerate(lista_linguagens): # o enumerate ja traz os indices e elementos da lista
    if linguagem == 'C++': # se o elemento por c++, substitui por ruby no index dela... entao primeiro acha o elemento e depois subistitui no index dele
        lista_linguagens[index] = 'Ruby'
print(lista_linguagens)

#%%
# 3- Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de 
# publicação. Imprima cada informação.

nome_livro = ['Senhor dos aneis', 'Vida pequena', 'Torto Arado']
ano_publicacao = [1980, 2000, 2010]

dict_livros = dict(zip(nome_livro, ano_publicacao))
dict_livros

# como criar uma lista de dicionarios?

#%%
# 4- Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando
#  um dicionário.

# planejamento
# criar dicionario vazio para contagem
# iterar para cada caractere na frase
# se o caractere ja existir no dicionario += 1 para aumentar a contagem em 1
# se o caractere nao existir no dicionario = 1 para abrir contagem 

frase = 'um gato, dois gatos, tres gatos, 4 gatos' # cada caractere é uma posicao nessa string
contagem_caracteres = {}

for f in frase:
    if f in contagem_caracteres:
        contagem_caracteres[f] += 1
    else:
        contagem_caracteres[f] = 1
print(contagem_caracteres)


#%%
# 5- Dada a lista ["maçã", "banana", "cereja"] e o
# dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_frutas = ['maca', 'banana', 'cereja']
dicionario_frutas = {"maca": 0.45, "banana": 0.30, "cereja": 0.65}
total_compras = []
# planejamento
# preciso iterar nos chaves do dicionario e ver se a chave = elemento da lista
# se for, jogar o valor para uma lista vazia
# somar os valores da lista

for key, value in dicionario_frutas.items():
    if key in lista_frutas:
        total_compras.append(value)
sum(total_compras)

#%% 

#6. Eliminação de Duplicatas
#Objetivo: Dada uma lista de emails, remover todos os duplicados.

emails = ["user@example.com", "admin@example.com", "user@example.com"]
#emails.remove('user@example.com')
emails_unicos = list(set(emails)) # O set tira as duplicacoes
emails_unicos 

#$$

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou 
# iguais a 18.

# com lambda 
idades = [14,15,17,30,45,98]
idade_maior_ou_igual_18 = filter(lambda x: x >= 18, idades)
print(list(idade_maior_ou_igual_18))

# com loop for
idades_filtradas = []
for idade in idades:
    if idade >= 18:
        idades_filtradas.append(idade)
print(idades_filtradas)

#%%

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.

dicionario_nomes = {'Thales': '30', 'Thaian': '28', 'Maria Lais': '27', 'Mari': '32'}
sorted(dicionario_nomes.keys(), reverse=True) # sorted é a funcao para ordernar chaves ou valores de um dicionario


#%%

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

numeros_para_calculo_media = [10,20,30,50,78]
sum(numeros_para_calculo_media) / len(numeros_para_calculo_media)

#%%

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares
#  e outra para ímpares.

lista_valores = [33,49,58,72,57]
valores_pares = []
valores_impares = []

for valor in lista_valores:
    if valor % 2 == 0:
        valores_pares.append(valor)
    else:
        valores_impares.append(valor)

print(valores_pares)
print(valores_impares)

#%%

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de
#  um produto específico.

dicionario_produtos = {'bola':50, 'luvas': 40, 'chuteira':190}
dicionario_produtos['luvas'] = 70
dicionario_produtos

#%%

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dicionario_1 = {'thales': 1.7, 'thaian':1.68 }
dicionario_2 = {'mari': 1.60, 'maria lais': 1.58}
dicionario_merged = dicionario_1 | dicionario_2 # para concatenar listas é + e dicionarios | (quase que nem no sql)
dicionario_merged

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com 
# quantidade maior que 50.

dicionario_produtos = {'bola':50, 'luvas': 40, 'chuteira':190}
produtos_com_mais_de_50_em_estoque = {}

for key, value in dicionario_produtos.items():
    if value > 50:
        produtos_com_mais_de_50_em_estoque[key] = value

produtos_com_mais_de_50_em_estoque

#%%
# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas chaves e valores.

dicionario_produtos = {'bola':50, 'luvas': 40, 'chuteira':190}
produtos = []
valores_produtos = []

for key, value in dicionario_produtos.items():
    produtos.append(key)
    valores_produtos.append(value)

print(produtos)
print(valores_produtos)


#%%
# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere usando um dicionário.

lista_caracteres = 'um gato, dois gatos, tres gatos, quatro gatos'
dicionario_caracteres = {}

for caractere in lista_caracteres:
    if caractere in dicionario_caracteres:
        dicionario_caracteres[caractere] += 1
    else:
        dicionario_caracteres[caractere] = 1

dicionario_caracteres


