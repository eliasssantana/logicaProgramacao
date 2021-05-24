print("-=" * 30)
print("=-" * 11,"Exercícios","=-" * 11)
print("-=" * 30)
# Exercício nº1
'''
1.	Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.
{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}  
'''

chaves = [1,4,5,6,7,9]
quadrado = {}
for i in chaves:
    quadrado[i] = i ** 2

print(quadrado)

# Exercício nº 2

'''
2.	Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100} 
'''
quadrado2 = {}
for i in range(1,11):
    quadrado2[i] = i ** 2

print(quadrado2)
'''
3.	Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo sa estrutura na tela. A média para aprovação é 7. Se o aluno tirar entre 5 e 6.9 está de recuperação, caso contrário é reprovado.
'''
'''
def aluno():
    alunos = {}
    nome = input("Digite seu nome:\n")
    media = float(input("Digite sua média:\n"))
    alunos[nome] = media
    print(alunos)
    if alunos[nome] >= 7:
        alunos['situação'] = 'aprovado'
        print(f"O aluno está aprovado com média de {alunos[nome]}.")
    elif alunos[nome] >= 5 and alunos[nome] < 7:
        alunos['situação'] = 'recuperação'
        print(f"O aluno está em recuperação com média de {alunos[nome]}.")
    else:
        alunos['situação'] = 'reprovado'
        print("O aluno está reprovado.")

aluno()
'''
# Exercício nº 4

from random import randint
from operator import itemgetter
from time import sleep
'''
Crie um programa em que 4 jogadores, joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. Dicas: procure sobre a função randint(), sleep() e itemgetter da bliblioteca operator.
'''

dicionario = {}
jogadores = []
for i in range(1,5): 
    dicionario["dado"] = randint(0,6)
    sleep(2)
    print(dicionario)
    jogadores.append(dicionario)
    dicionario = {}
dict_ordenado = sorted(jogadores, key=itemgetter("dado"),reverse= True)
print('\033[0;33m-=\033[m'* 10,"\033[1;33;44mranking\033[m",'\033[0;33m=-\033[m' * 10)
for i,v in enumerate(dict_ordenado):
    a = f"Jogador nº{i + 1}: {v['dado']}"
    print(a.center(50))


# Exercício nº5

'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade , com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
'''
'''
def aposentadoria():
    dictionary = {}
    nome = input("Digite o seu nome:\n")
    dictionary["nome"] = nome
    ano_nascimento = int(input("Digite o seu ano de nascimento:\n"))
    ctps = int(input("Digite seu CTPS:\n"))
    idade = 2021 - ano_nascimento
    dictionary["idade"] = idade
    if ctps != 0:
        ano_contratacao = int(input("Digite o ano de sua contratação:\n"))
        dictionary["ano de contratação"] = ano_contratacao
        dictionary["salário"] = float(input("Digite o seu salário:\n"))
        ano_aposentadoria = ano_contratacao + 35
        dictionary["ano de aposentadoria"] = ano_aposentadoria
        print(dictionary)
    else:
        print(dictionary)

aposentadoria()
'''
# DESAFIO

'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas estão cadastradas.
B) A média da idade.
C) Uma lista com as mulheres.
D) Uma lista com as idades que estão acima da média.
OBS: O programa deve garantir que o sexo digitado seja válido, e que quando perguntar ao usuário se deseja continuar a resposta seja somente sim ou não.
'''
def dados():
    idades = 0
    resposta = True
    pessoas = []
    pessoa = {}
    mulheres = []
    while resposta == True:
        nome = input("Digite seu nome:\n")
        sexo = input("Digite seu sexo:\n[M/F]\n").upper().strip()
        while sexo not in "MF":
            print("Sexo inválido!")
            sexo = input("Digite seu sexo:\n[M/F]\n").upper().strip()
        idade = int(input("Digite sua idade:\n"))
        idades += idade
        pessoa['nome'] = nome
        pessoa['sexo'] = sexo
        pessoa['idade'] = idade
        if sexo == "F":
            mulheres.append(pessoa)
        pessoas.append(pessoa)
        pessoa = {}
        continuar = input("Deseja continuar?\n[S/N]\n").upper().strip()
        while continuar not in "SN":
            print("Resposta INVÁLIDA!")
            continuar = input("Deseja continuar?\n[S/N]\n").upper().strip()
        if continuar == "N":
            resposta = False
        else:
            print("Continuando...")
    num = len(pessoas)
    media = idades / num
    acima_media = []
    print(f"O número de pessoas cadastradas é de: {num} pessoa/as.")
    print(f"A média de idades é de: {media} anos.")
    if mulheres == []:
        print("Não há mulheres cadastradas.")
    else:
        print("Mulheres cadastradas:\n")
        for i in mulheres:
            print(i['nome'])
    for i in pessoas:
        if i['idade'] > media:
            acima_media.append(i['idade'])
    print("Idades acima da média:\n")
    for i in acima_media:
        print(i, end=" ")
            