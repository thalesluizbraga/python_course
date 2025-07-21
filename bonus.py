#%%
# Escreva um programa em Python que solicita ao usuário para 
# digitar seu nome, o valor do seu salário mensal e o valor 
# do bônus que recebeu. O programa deve, então, imprimir uma
#  mensagem saudando o usuário pelo nome e informando o valor
#  do salário em comparação com o bônus recebido.


#%%
# Function to define 
def bonus_calculation(name:str, monthly_salary:float, bonus_rate:float) -> float:
    return f'Hi {str(name)}, your bonus is {float(monthly_salary) * (float(bonus_rate))}'

# %%

# function call and result
name = 'Thales'
monthly_salary = 9750
bonus_rate = 0.5

bonus_total = bonus_calculation(name=name, monthly_salary=monthly_salary, bonus_rate=bonus_rate)
print(bonus_total)