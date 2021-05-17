
# Exercício nº1

'''Exercício 1 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.  Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''

i = 1
alunos = []
prov = []
while i < 6:
    num_aluno = input("Digite o nome do aluno: \n")
    altura_aluno = float(input("Digite a altura do aluno:\n"))
    prov.append(num_aluno)
    prov.append(altura_aluno)
    alunos.append(prov)
    prov = []
    i += 1
mais_alto = alunos[0][1]
mais_baixo = alunos[1][1]
num_alto = 0
num_baixo = 0
for i in alunos:
    if i[1] >= mais_alto:
        mais_alto = i[1]
        num_alto += 1
        pessoa_alta = i[0]
for i in alunos:
    if i[1] <= mais_baixo:
        mais_baixo = i[1]
        num_baixo += 1
        pessoa_baixa = i[0]
print(f"O/A aluno/a mais alto/a é {pessoa_alta} com {mais_alto:.2f}\ne a pessoa mais baixa é {pessoa_baixa} com {mais_baixo:.2f}.")

# Exercício nº2 
'''
- Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha.
'''

def digitaSenha():
    password = 12345
    senha = int(input("Digite a senha:\n[senha numérica]\n"))
    while senha != password:
        print("SENHA INCORRETA")
        senha = int(input("Digite a senha:\n"))
    
    print("SENHA CORRETA")

digitaSenha()

# Exercício nº3 
'''
- Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código.

Os códigos utilizados são:
•	1 , 2, 3  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
•	5 - Voto Nulo
•	6 - Voto em Branco
Faça um programa que calcule e mostre:
•	O total de votos para cada candidato;
•	O total de votos nulos;
•	O total de votos em branco;
•	A percentagem de votos nulos sobre o total de votos;
•	A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

'''

candidatos = []
candidatos2 = []
for i in range(1,5):
    indice = f'{i} - '
    candidato = input(f"Digite o nome do {i}º candidato:\n")
    cand = indice + candidato
    candidatos.append(cand)
    candidatos2.append(candidato)

candidatos.append("5 - Voto Nulo")
candidatos.append("6 - Voto em Branco")
for pessoa in candidatos:
    print(pessoa)
cand1 = 0; cand2 = 0; cand3 = 0; cand4 = 0; nulos = 0; brancos = 0
votos = []
voto = int(input("Digite o número do candidato para votar:\n"))
while voto != 0:
    voto = int(input("Digite o número do candidato para votar:\n[0 para finalizar a votacão]\n"))
    if voto == 0:
        voto = 0
    elif voto > 6:
        voto = int(input("Digite o número do candidato para votar:\n[0 para finalizar a votacão]\n"))
    elif voto == 1:
        cand1 += 1
    elif voto == 2:
        cand2 += 1
    elif voto == 3:
        cand3 += 1
    elif voto == 4:
        cand4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
votos.append(cand1)
votos.append(cand2)
votos.append(cand3)
votos.append(cand4)
total_votos = sum(votos)
per_nulos = (nulos / total_votos) * 100 
per_brancos = (brancos / total_votos) * 100 
for i in range(4):
    print(f"O candidato {candidatos2[i]} recebeu {votos[i]} voto\s.")
print(f"O total de votos nulos é de: {nulos} voto\s")
print(f"O total de votos brancos é de: {brancos} voto\s")
print(f"A porcentagem de votos nulos é de: {per_nulos:.1f}%")
print(f"A porcentagem de votos brancos é de: {per_brancos:.1f}%")

# Exercício 4
'''
– Codifique um jogo da FORCA. A pessoa digita uma palavra e tem que acertar a palavra digitada.
'''

palavra = input("Digite a palavra para o jogo da forca:\n").lower().strip()
letras_certas = 0
palavra2 = list(palavra)
totalLetras = len(palavra2)
while palavra != 0:
    letra = input("Digite uma letra:\n")
    if letra in palavra2:
        palavra2.remove(letra)
        letras_certas += 1


#DESAFIO
'''  
- Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa).  Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:
•	Maior e Menor Acerto;
•	Total de Alunos que utilizaram o sistema;
•	MédA ia das Notas da Turma.
# Gabarito da Prova:
# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova # antes dos alunos usarem o programa.
'''
def prova():
    utilizando = True
    gabarito = ["A","B","C","D","E","E","D","C","B","A"]
    notas = []
    total_sistema = 0
    gabarito_prof = []
    for i in range(10):
        resp = input(f"Digite o gabarito da {i + 1}ª questão:\n").upper().strip()
        gabarito_prof.append(resp)
    print(gabarito_prof)
    while utilizando == True:
        pontos = 0
        respostas = []
        total_sistema += 1 
        for q in range(1,11):
            resp_aluno = input(f"Digite a resposta da {q}ª questão:\n").upper().strip()
            respostas.append(resp_aluno)
        for i in range(10):
            if gabarito_prof[i] == respostas[i]:
                pontos += 1
        notas.append(pontos)
        print(f"O aluno acertou {pontos} questões e recebeu uma nota {pontos}.")
        pontos = 0
        respostas = []
        prox_aluno = int(input("PRÓXIMO...\nQuer continuar utilizando o sistema?\n[1 - SIM, 0 - NÃO]\n"))
        if prox_aluno == 0:
            utilizando = False
    nota_maior = max(notas)
    nota_menor = min(notas)
    media = sum(notas) / len(notas)
    print(f"A maior nota foi {nota_maior} e a nota menor é {nota_menor}.")
    print(f"O total de alunos que utilizaram o sistemas é de {total_sistema} alunos.")
    print(f"A média das notas da turma é de: {media}.")

prova()