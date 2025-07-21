#%%
# 1- Escreva um programa que soma dois números inteiros inseridos pelo usuário.
print(1+1)

# 2- Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
print(10%3)

# 3- Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
print(2*2)

# 4- Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
print(10//2)

# 5- Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#Números de Ponto Flutuante (float)
print(2**2)

# 6- Escreva um programa que receba dois números flutuantes e realize sua adição.
print(0.5+0.43)

# 7- Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print((0.5+0.43)/2)

# 8- Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
print(0.5**0.3)

# 9- Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = 10
fahrenheit = celsius * 33.8
print(fahrenheit)


# 10- Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#Strings (str)



# 11- Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
lower_word = 'thales'
upper_word = lower_word.upper()
print(upper_word) 


# 12- Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
complete_name = 'Thales Luiz Gomes Braga Dalmonica'
lower_complete_name = complete_name.lower()
print(lower_complete_name)

# 13- Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
complete_name_with_no_spaces = complete_name.replace(' ','')
print(complete_name_with_no_spaces)

# 14- Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
date = '13/05/2025'
day, month, year = date.split('/')
print(day)
print(month)
print(year)

# 15- Escreva um programa que concatene duas strings fornecidas pelo usuário.
#Booleanos (bool)
print('a' + 'b')

# 16- Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# 17- Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# Exemplo de entrada
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# 18- Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# Exemplo de entrada
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# 19- Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
print(2==2)

# 20- Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
print(2!=2)


