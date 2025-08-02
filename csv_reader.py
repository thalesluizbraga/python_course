#%%

# para ler um arquivo com a lib csv:
    # importar lib csv
    # passar na funcao open o nome do arquivo e encoding para um arquivo
    # criar um leitor com o csv.DictReader
    # iterar para cada linha do arquivo 
    # printar as linhas do arquivo

# Ler arquivo csv com csv lib

import csv

file_path = 'vendas.csv'

def ler_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            return row

ler_csv(file_path)
#%%

# adicionar/appendar dados em um csv (mode='a'), se fosse pra sobrescrever seria mode='w'

import csv

file_path = 'vendas.csv'
new_data = {'Produto': 'luvas', 'Categoria': 'esportes', 'Quantidade': 10, 'Venda': 60}

def appendar_dados_no_arquivo(file_path, new_data):
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = new_data.keys()    
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        if file.tell() == 0:
            writer.writeheader()
        return writer.writerow(new_data) # writerows se tivesse mais de uma linha

appendar_dados_no_arquivo(file_path, new_data)


# %%

# filtrar dados no csv

file_path = 'vendas.csv'

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader: # o dictreader cria um dicioonario para cada linha, entao preciso iterar pra cada dicionario que é cada linha e depois iterar de novo pra achar os valores e chaves
        for key, value in row.items():
                print(key[0
                ])
