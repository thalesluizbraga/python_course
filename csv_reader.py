#%%

# para ler um arquivo com a lib csv:
    # importar lib csv
    # passar na funcao open o nome do arquivo e encoding para um arquivo
    # criar um leitor com o csv.DictReader
    # iterar para cada linha do arquivo 
    # printar as linhas do arquivo

import csv

file_path = 'vendas.csv'

with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)

#%%

# escrevendo no arquivo com apped (mode='a'), se fosse pra sobrescrever seria mode='w'

import csv

file_path = 'vendas.csv'
new_data = {'Produto': 'luvas', 'Categoria': 'esportes', 'Quantidade': 10, 'Venda': 60}

# To append to existing file (keeping header if it exists)
with open(file_path, mode='a', newline='', encoding='utf-8') as file:
    fieldnames = new_data.keys()    
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
    
    if file.tell() == 0:
        writer.writeheader()
    
    writer.writerow(new_data) # writerows se tivesse mais de uma linha



# %%


import csv

file_path = 'vendas.csv'

with open(file_path, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)