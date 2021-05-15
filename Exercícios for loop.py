print("=-" * 40)
print(" " * 30, "Exercícios", " " * 25)
print("=-" * 40)

# Exercício nº 1
'''
1. Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida imprima essa tabuada.
'''

def tabuada():
    num = int(input("Digite a tabuada que você quer:\n"))
    for i in range(1,11):
        print(f'{num} X {i} = {num * i}')

tabuada()

# Exercicio nº 2
'''
2. Elaborar um programa para imprimir os números de 1 (inclusive) até 10 (inclusive) em ordem decrescente. 
'''

for cont in range(10,0,-1):
    print(cont)

# Exercício nº 3

'''
3. Faça um programa que leia o estado civil de 15 pessoas (Solteiro / Casado) e mostre ao final a quantidade de pessoas de cada estado civil. 
'''

casado = 0
solteiro = 0

for cont in range(1,16):
    casado = 0
    solteiro = 0
    estado_civil = input("Digite seu estado civil:\n[casado ou solteiro]\n").lower()
    if estado_civil == 'casado':
        casado += 1
    else:
        solteiro += 1

print(f"A quantidade de casados é de {casado} e solteiros é de {solteiro}")

# Exercício nº 4
'''
4. Faça um algoritmo que imprima 10 vezes a frase: “Go Blue”. 
'''

for cont in range(10):
    print("Go Blue!")

# Exercício nº 5

'''
5. Faça um programa que mostre os valores numéricos inteiros ímpares situados na faixa de 0 a 20
'''

for cont in range(21):
    if (cont % 2 != 0):
        print(cont)

'''
6. O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo: 
'''

tabela_de_preco = []

for preco in range(1,51):
    preco_pao = float(input("Preço do pão:\n"))
    formatado = f'{preco} - {preco_pao}'
    tabela_de_preco.append(formatado)

for preco_pao in tabela_de_preco:
    print(preco_pao)

# Exercício nº 6

'''
7. O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo
'''

preco = float(input('Digite o preço do produto:\n(Digite 0 para sair)\n: '))
produto = input('Digite o nome do produto:\n ')

produtos = []
produtos.append(produto)

precos = []
precos.append(preco)

while preco != 0:
        preco = float(input('Digite o preço do produto:\n(Digite 0 para sair)\n'))
        if preco != 0:
            produto = input('Digite o nome do produto:\n')
            produtos.append(produto)
            precos.append(preco)
len_pro = len(produtos)
for i in range(len_pro):
    if precos[i] == 0:
        pass
    else:
        print(f'produto {i + 1}: {produtos[i]} : R${precos[i]:.2f}')

total_compra = sum(precos)
print(f"O total foi de R${total_compra:.2f}")
valor_pago = float(input("Digite o valor que vai pagar:\n"))
troco = valor_pago - total_compra
print(f'Total da Compra: R${total_compra:.2f}')
print(f'Total pago: R${valor_pago:.2f}')
print(f'Troco: R${troco:.2f}')
print("-=" * 40)
print(" " * 25 ,"Obigado pela preferência!", " " * 25)
print("-=" * 40)

# Exercício nº 8

telefonou = input("Telefonou para a vítima?[s/n]")
local = input("Esteve no local do crime?[s/n]")
mora = input("Mora perto da vítima?[s/n]")
devia = input("Devia a vítima?[s/n]")
trabalhou = input("Já trabalhou com a vítima?[s/n]")

respostas = [telefonou, local,mora,devia,trabalhou]
sim = 0
nao = 0
for resposta in respostas:
    if resposta == "s" or resposta =='S':
        sim += 1
    else:
        nao += 1
if sim == 2:
    print("Suspeita")
elif sim == 3 or sim == 4:
    print("Cúmplice")
elif sim == 5:
    print("Assassino")
else:
    print("Inocente")



# Exercício nº 9

for dez1 in range(1,61):
    for dez2 in range(1,61):
        for dez3 in range(1,61):
            for dez4 in range(1,61):
                for dez5 in range(1,61):
                    for dez6 in range(1,61):


# Desafio nº 1  


def duplaNumeros():
    for dupla in range(10,100):
        for dupla1 in range(1,100):
            if dupla1 < 10:
                num = str(dupla1).zfill(2)
                numero = str(dupla) + str(num)
                dupla2 = int(num)
                num_int = int(numero)
                soma = dupla + dupla2
                if soma ** 2 == num_int:
                  print(num_int)
            else:
              numero = str(dupla) + str(dupla1)
              num_int = int(numero)
              soma = dupla + dupla1
              if soma ** 2 == num_int:
                  print(num_int)
duplaNumeros()

'''ou'''

def duplaNumeros():
    for num  in range(1000,10000):
        dupla1 = num // 100
        dupla2 = num % 100
        soma = dupla1 + dupla2 
        if soma ** 2 == num:
            print(num)

duplaNumeros()

# Desafio nº 2

num_materias = int(input("Digite o seu número de matérias na escola:\n"))
notas = []
for num in range(1,num_materias + 1):
    nota_materia = float(input(f"Digite a sua nota na {num}ª matérias:"))
    notas.append(nota_materia)

# for nota in notas:
    #soma_notas += nota
soma_notas = sum(notas)
media = soma_notas / len(notas)
if num_materias == 1:
    print(f"A sua média geral na matéria é de {media:.1f}")
else:
    print(f"A sua média geral nas {num_materias} matérias é de {media:.1f}")


