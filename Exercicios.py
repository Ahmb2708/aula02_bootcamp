# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

numero_1 = int(input("Digite um número inteiro:"))
numero_2 = int(input("Digite outro número inteiro:"))
soma = numero_1 + numero_2

print(f"O resultado da soma foi: {soma}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero_user = int(input("Digite um número: "))
resto_div = numero_user%5

print(f"O resto da divisão foi: {resto_div:.2f}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

numero_user = int(input("Digite um número: "))
resto_div = numero_user%5

print(f"O resto da divisão foi: {resto_div:.2f}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))
mult = num_1 ** num_2

print(f"O resultado da multiplicação do número {num_1} x {num_2} é igual a {mult:.2f}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

num_1 = int(input("Digite um número: "))
num_2 = int(input("Digite outro número: "))
div = num_1//num_2

print(f"O resultado da divisão inteira do primeiro pelo segundo é {div}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

numero = int(input("Digite um número: "))
num_quad = numero ** 2

print(f"O número {numero} ao quadrado fica {num_quad}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

num_1 = float(input("Digite um número: "))
num_2 = float(input("Digite outro número: "))
soma_float = num_1 + num_2

print(f"O resultado da soma foi {soma_float}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

try:
    num_1 = float(input("Digite um número: "))
    num_2 = float(input("Digite outro número: "))
    media_float = (num_1 + num_2)/2

    print(f"O resultado da média foi {media_float}")
except:
    print("Algo deu errado, verifique se colocou números Reais corretamente")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

try:
    base = float(input("Digite um número para ser a base: "))
    expo = float(input("Digite um número para ser o expoente: "))
    calc_pot = base ** expo

    print(f"O calculo de potência da base {base} com o expoente {expo} foi {calc_pot}")
except:
    print("Algo deu errado, verifique se digitou um número flutuante")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

try:
    cel = float(input("Digite um valor de uma temperatura em celsius para ser convertido em Fahrenheit: "))
    fah = cel * 1.8 + 32

    print(f"A temperatura {cel} Celsius é equivalente à {fah} Fahrenheit")
except:
    print("Algo deu errado, digite uma temperatura válida")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

import math

try:
    raio = float(input("Digite o tamnho do raio: "))
    area_circ = math.pi * raio ** 2
    print (f"A área do cículo é {area_circ:.2f}")
except:
    print("Algo deu errado, digite um valor válido")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

string_upper = input("Digite uma frase para deixá-la em CAIXA ALTA: ").upper()

print(f"A frase em caixa alta ficou assim: \n{string_upper}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

nome_lower = input("Digite seu nome completo: ").lower()

print(f"Seu nome é: {nome_lower}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

frase_strip = input("Digite uma frase: ").strip()

print(f"A frase foi a seguinte: \n{frase_strip}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

try:
    lista = input("Digite uma data no seguinte formato 'dd/mm/aaaa':\n").split("/")

    print(f"A data é composta pelo dia {lista[0]}, o mês {lista[1]} e o ano {lista[2]}")
except:
    print("Coloque a data no formato indicado")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

s1 = input("Digite o nome de um carro: ")
s2 = input("Digite o nome de uma fruta: ")
s_concat = s1 + " " + s2

print(f"O nome do seu carro fruta é: {s_concat}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

bool_1 = input("Digite um valor booleano (True ou False): ")
bool_2 = input("Digite outro valor booleano (True ou False): ") 
if bool_1 == "True" and bool_2 == "True":
    print("O resultado da operação AND entre os dois valores booleanos é: True")
else:
    print("O resultado da operação AND entre os dois valores booleanos é: False")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

bool_1 = input("Digite um valor booleano (True ou False): ")
bool_2 = input("Digite outro valor booleano (True ou False): ")
if bool_1 == "True" or bool_2 == "True":
    print("O resultado da operação OR entre os dois valores booleanos é: True")
else:
    print("O resultado da operação OR entre os dois valores booleanos é: False")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

try:
    bool_user = input("Digite um valor booleano (True ou False): ")
    if bool_user == "True".lower():
        print("O valor booleano invertido é: False")
    elif bool_user == "False".lower():
        print("O valor booleano invertido é: True")
except:
    print("Valor booleano inválido, digite True ou False")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

try:
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite outro número: "))
    if num_1 == num_2:
        print("Os números são iguais")
    else:    
        print("Os números são diferentes")
except:
    print("Algo deu errado, verifique se digitou um número inteiro")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

try:
    num_1 = int(input("Digite um número: "))
    num_2 = int(input("Digite outro número: "))
    if num_1 != num_2:
        print("Os números são diferentes")
    else:    
        print("Os números são iguais")
except:
    print("Algo deu errado, verifique se digitou um número inteiro")


# #### try-except e if

# 21: Conversor de Temperatura

try:
    temp_celsius = float(input("Digite a temperatura em Celsius para converter para Fahrenheit: "))
    temp_fahrenheit = temp_celsius * 1.8 + 32
    print(f"A temperatura {temp_celsius}°C é equivalente a {temp_fahrenheit}°F")
except ValueError:
    print("Valor inválido, por favor digite um número para a temperatura.")

# 22: Verificador de Palíndromo

try:
    palavra = input("Digite uma palavra para verificar se é um palíndromo: ")
    palavra_limpa = palavra.replace(" ", "").lower()
    if palavra_limpa == palavra_limpa[::-1]:
        print(f"A palavra '{palavra}' é um palíndromo.")
    else:
        print(f"A palavra '{palavra}' não é um palíndromo.")
except:
    print("Algo deu errado, tente novamente.")

# 23: Calculadora Simples

try:
    num1 = float(input("Digite o primeiro número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            resultado = None
    else:
        print("Operador inválido. Use +, -, *, ou /.")
        resultado = None

    if resultado is not None:
        print(f"O resultado de {num1} {operador} {num2} é: {resultado}")
except ValueError:
    print("Valor inválido, por favor digite números para a calculadora.")

# 24: Classificador de Números

try:
    numero = float(input("Digite um número para classificar: "))
    if numero > 0:
        print(f"O número {numero} é positivo.")
    elif numero < 0:
        print(f"O número {numero} é negativo.")
    else:
        print("O número é zero.")
except ValueError:
    print("Valor inválido, por favor digite um número para classificar.")

# 25: Conversão de Tipo com Validação

try:
    valor = input("Digite um valor para converter para inteiro: ")
    valor_int = int(valor)
    print(f"O valor convertido para inteiro é: {valor_int}")
except ValueError:
    print("Valor inválido, por favor digite um número inteiro para a conversão.")