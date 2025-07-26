#%%

# Etapa 1
# Escreva um programa em Python que solicita ao usuário para 
# digitar seu nome, o valor do seu salário mensal e o valor 
# do bônus que recebeu. O programa deve, então, imprimir uma
#  mensagem saudando o usuário pelo nome e informando o valor
#  do salário em comparação com o bônus recebido.


# Etapa 2
# Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

#%%

while True:
    name = str(input('Insira o seu nome:'))
    if name.isalpha():
        monthly_salary = float(input('Insira seu salario:'))
        if isinstance(monthly_salary,float) and monthly_salary > 0:
            bonus_rate = float(input('Insira o bonus rate:'))
            if isinstance(bonus_rate, float) and bonus_rate > 0:
                bonus = monthly_salary * bonus_rate
                print(f'Seu bonus sera de {bonus}')
                break


