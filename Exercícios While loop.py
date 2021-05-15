# Exercício nº1

'''Exercício 1 - Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros.  Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.'''
'''
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
'''
'''
def duplaNumeros():
    for dupla in range(10,100):
        for dupla1 in range(1,100):
            if dupla1 < 10:
                num = str(dupla1).zfill(2)
                numero = str(dupla) + str(num)
                dupla2 = int(num)
                num_int = int(numero)
                soma = dupla + num
                if soma ** 2 == num_int:
                  print(num_int)
            else:
              numero = str(dupla) + str(dupla1)
              num_int = int(numero)
              soma = dupla + dupla1
              if soma ** 2 == num_int:
                  print(num_int)
duplaNumeros()
'''
def duplaNumeros():
    for num  in range(1000,10000):
        dupla1 = num // 100
        dupla2 = num % 100
        soma = dupla1 + dupla2 
        if soma ** 2 == num:
            print(num)

duplaNumeros()