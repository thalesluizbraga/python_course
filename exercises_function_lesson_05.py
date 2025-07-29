#%%
# 1 Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def somar_numeros(lista_numeros: list) -> float:
    return sum(lista_numeros)

lista_numeros = [10,20,30]
somar_numeros(lista_numeros)

#%%
# 2 Crie uma função que receba um número como argumento e retorne 
# True se o número for primo e False caso contrário.

def is_prime(num: int) -> int:
    if int(num) <= 1:
        return False
    if int(num) == 2:
        return True
    if int(num) % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if int(num) % i == 0:
            return False
    return True

is_prime(9)




#%%
# 3 Desenvolva uma função que receba uma string como argumento e 
# retorne essa string revertida.

def reverter_string(frase: str) -> str:
    return frase[::-1]

frase = 'teste'
reverter_string(frase)


#%%
# 4 Implemente uma função que receba dois argumentos: uma lista de 
# números e um número. A função deve retornar todas as combinações de
#  pares na lista que somem ao número dado.

def encontrar_pares_soma(lista, alvo):
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                pares.append((lista[i], lista[j]))
    return pares


#%%

# 5 Escreva uma função que receba um dicionário e retorne uma lista de
#  chaves ordenadas

def retornar_lista_chaves_ordenadas(dicionario_para_transformacao: dict, lista_chaves_ordernadas: list) -> list:
    
    for key in dicionario_para_transformacao:
        lista_chaves_ordernadas.append(key)
    return sorted(lista_chaves_ordernadas)


dicionario_para_transformacao = {'futebol':1, 'basquete':2, 'ginastica':3}
lista_chaves_ordernadas = []
retornar_lista_chaves_ordenadas(dicionario_para_transformacao,lista_chaves_ordernadas
