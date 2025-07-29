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

