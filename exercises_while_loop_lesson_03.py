#%%
# 11. Leitura de Dados até Flag
# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

while True:
    palavra_chave = input('Insira a palavra-chave aqui:')
    if palavra_chave == 'sair':
        break

#%%
# 12. Validação de Entrada
# Objetivo: Solicitar ao usuário um número dentro de um intervalo
#  específico até que a entrada seja válida.

   
while True:
    numero_usuario = float(input('digite um numero:'))
    if 20 < numero_usuario  <= 50:
        print('intervalo correto')
        break
    else:
        print('numero fora do intervalo')
    

#%%
# 13. Consumo de API Simulado
# Objetivo: Simular o consumo de uma API paginada, onde cada "página"
#  de dados é processada em loop até que não haja mais páginas.

pagina_atual = 1
total_paginas = 5

while pagina_atual <= total_paginas:

    print(f'processando pagina {pagina_atual} de {total_paginas}')
    pagina_atual += 1
print('todas as paginas foram processadas')

#%%

# 14. Tentativas de Conexão
# Objetivo: Simular tentativas de reconexão a um serviço com um
#  limite máximo de tentativas.

tentativa = 1
maximo_tentativas = 5

while tentativa <= maximo_tentativas:
    print(f'tentativa {tentativa} de acesso num maximo de {maximo_tentativas}')
     # Simulação de uma tentativa de conexão
    # Aqui iria o código para tentar conectar
    if True:
        print('tentativa bem sucedida')
        break
    
    tentativa += 1
else:
    print('tentativas esgotadas')

#%%

# 15. Processamento de Dados com Condição de Parada
# Objetivo: Processar itens de uma lista até encontrar um valor
#  específico que indica a parada.

lista_parada = [1,5,49,50,100,39,150]

i = 0 # para setar o inicio da contagem

# vai parar quando achar o numero 100 na lista
while i < len(lista_parada):
        if lista_parada[i] == 100:
            print(f'parou na posicao {i}')
            break
        else:
            print('fora do range')
        i += 1