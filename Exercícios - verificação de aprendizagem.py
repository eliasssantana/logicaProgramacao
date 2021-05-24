print("=-" * 30)
e = 'Exercícios'
print(e.center(50))
print("=-" * 30)

# 01)
'''
- Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
•	A soma deles;
•	A multiplicação entre eles;
•	A divisão  inteira deles;
•	Mostre na tela qual é o maior;
•	Verifique se o resultado da soma é par ou ímpar e mostre na tela;
•	Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
'''
def doisNum(x,y):
    soma = x + y
    multiplicacao = x * y
    divisao = x / y
    divisaoInt = x // y
    print(soma)
    print(multiplicacao)
    print(f'{divisao:.1f}')
    if x > y:
        print(f"{x} é o maior.")
    elif y > x:
        print(f"{y} é o maior.")
    else:
        print(f"{x} e {y} são iguais.")

    if soma % 2 == 0:
        print("O resultado da soma é par")
    else:
        print("O resultado da soma é ímpar")
    
    if multiplicacao > 40:
        res = multiplicacao / divisaoInt
        print(res)
    else:
        print("resultado da multiplicação não foi maior que 40")

# 02)
'''
- Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela. Depois mostre na tela essa mesma frase sem nenhuma vogal.
'''
def vogais():
    palavra = input("Digite uma palavar ou frase:\n").upper()
    vogais = 0
    p = list(palavra)
    for i in palavra:
        if i in 'AEIOU':
            vogais += 1
            p.remove(i)
    print(vogais)
    print(p)

# vogais()

# 03)
'''
- Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento. Não deixe o usuário continuar se a senha estiver incorreta, após entrar d-vindas a seuê as boas usuário e apresente a ele o jogo da adivinhação, onde o computador vai pensar em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até  acertar, a cada palpite do usuário  diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou. No final mostre quantos palpites foram necessários para vencer.
'''
from random import randint as rand
def advinhacao():
    senha = 12345
    password = int(input("Digite a senha:\n"))
    while password != senha:
        print("SENHA INCORRETA")
        password = int(input("Digite a senha:\n"))
    sbv = "Seja bem-vindo ao jogo de advinhação!"
    print("=-" * 25)
    print(sbv.center(50))
    print("=-" * 25)

    num = rand(0,10)
    palpites = 1
    tentativa = int(input("Advinhe o número:\n"))
    while tentativa != num:
        if tentativa > num:
            print('O número é menor que isso')
        else:
            print("O número é maior que isso:")
        print("Mais uma vez...")
        tentativa = int(input("Advinhe o número:\n"))
        palpites += 1
    sb = f"Parabéns! você venceu a maquina em {palpites} tentativas."
    print("=-" * 25)
    print(sb.center(50))
    print("=-" * 25)

# 04)
'''
- Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato escrito por extenso. Valide a data e retorne NULL caso a data seja inválida.
'''

meses =["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Desembro"]
data = str(input("Digite uma data no seguinte formato:\n[DD/MM/AAAA]\n"))

def dataPorExtenso(data):
    data1 = data.split('/')
    dia = data1[0]
    dia_int = int(dia)
    mes = data1[1]
    mes_int = int(mes)
    ano = data1[2]
    ano_int = int(ano)
    if (mes_int != 0 and ano_int != 0 and dia_int != 0):
        if (ano_int % 4 == 0 and ano_int % 100 != 0) or (ano_int % 400 == 0):
            print(ano_int)
            for m in meses:
                month = meses.index(m)
                if ( mes_int == (month + 1)):
                    print(f"{dia}/{m}/{ano_int}")
        else:
            if(mes_int == 2 and dia_int > 28):
                print("Null")
            else:
                for m in meses:
                    month = meses.index(m)
                    if ( mes_int == (month + 1)):
                        print(f"{dia}/{m}/{ano_int}")

# 05)
'''
- Refatore o exercício2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras que foram retiradas da frase original.
'''
def vogais2():
    palavra = input("Digite uma palavar ou frase:\n").upper().strip()
    vogais = 0
    p = list(palavra)
    for i in palavra:
        if i in 'AEIOU':
            vogais += 1
            p.remove(i)
    ''.join(p)
    p2 = str(p).strip('[]')
    print(vogais)
    print(p2)
# vogais2()

# 6)
'''
- Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
 As perguntas são:
•"Telefonou para a vítima?"
•"Esteve no local do crime?"
•"Mora perto da vítima?"
•"Devia para a vítima?"
•"Já trabalhou com a vítima?"
 O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se   a   pessoa   responder   positivamente   a   2   questões   ela   deve   ser   classificada   como "Suspeita",entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
def investigacao():
    tel = input("Telefonou para a vítima?\n[S/N]\n").upper().strip()
    loc = input("Esteve no local do crime?\n[S/N]\n").upper().strip()
    mrv = input("Mora perto da vítima?\n[S/N]\n").upper().strip()
    dva = input("Devia para a vítima?\n[S/N]\n").upper().strip()
    tbl = input("Já trabalhou com vítima?\n[S/N]\n").upper().strip()
    respostas = [tel,loc,mrv,dva,tbl]
    qtdSim = respostas.count('S')

    suspeito =  qtdSim == 2
    cumplice = qtdSim == 3 or qtdSim == 4
    assassino = qtdSim == 5
    inocente = qtdSim == 1

    niveis = {suspeito:'suspeito',cumplice:'cúmplice',assassino:'assassino',inocente:'inocente'}

    for k,v in niveis.items():
        if k == True:
            print(f"O indivíduo é o {v}.")
        
# 7) 
'''
- Crie um programa onde o usuário possa digitar sete valores numéricos  e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares  em ordem crescente.
'''
def valores():
    par = []
    impar = []
    todos = []
    print("Digite sete valores numéricos:\n")
    for i in range(1,8):
        v = int(input(f"Digite o {i}º valor:\n"))
        if v % 2 == 0:
            par.append(v)
        else:
            impar.append(v)
    todos.append(par)
    todos.append(impar)
    for i,v in enumerate(todos):
        if i == 0:
            print('Valores pares:') 
            print(v)
        else:
            print("Valores ímpares:")
            print(v) 
valores()

# 8)
''' 
- Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar. 
'''
def aposentadoria():
    pessoa = {}
    nome = input("Digite o seu nome:\n")
    ano_nascimento = int(input("Digite o ano de seu nascimento:\n"))
    carteira_trabalho = int(input("Digite o número da sua carteira de trabalho:\n"))
    pessoa['nome'] = nome
    pessoa['nascimento'] = ano_nascimento
    if carteira_trabalho != 0:
        pessoa['ano de contratação'] = int(input("Digite o ano de sua contratação:\n"))
        pessoa['salário'] = float(input('Digite o seu salário:\n'))
        pessoa['CTPS'] = carteira_trabalho
    else:
        pass
    idade = 2021 - ano_nascimento
    aposentadoria = idade + 35
    pessoa['idade'] = idade
    pessoa['aposentadoria'] = aposentadoria
    for k,v in pessoa.items():
        print(f'{k} - {v}')

aposentadoria()