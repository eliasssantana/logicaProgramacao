import datetime
#Exércicio nº1
'''
def numero(n1,n2):
    min = n1
    if n2 < min:
        min = n2
        print(f"O menor número é: {min}")
    elif n1 == n2:
        print("Os números são iguais")
    else:
        print(f"O menor número é: {min}")

n1 = int(input("Digite o primeiro número:\n "))
n2 = int(input("Digite o segundo número:\n"))

numero(n1,n2)

#Exercício nº 2

from typing import ByteString


def rcbNum(n1,n2,lim):
    if (n1 + n2) > lim:
        return "True"
    else:
        return "False"

n1 = int(input("Digite um número:\n"))
n2 = int(input("Digite outro número:\n"))
lim = int(input("Digite um valor limite:\n"))

print(rcbNum(6,7,9))

#Exercício nº 3

def toUpper(sting):
    return string.upper()


string = input("Digite uma mensagem:\n")

print(toUpper(string))

#Exercício nº 4

def voto(ano):
    data = datetime.datetime.now()
    idade = data.year - ano
    if (idade) > 18:
        print("Seu voto é OBRIGATÓRIO")
    elif (idade >= 16 and idade < 18):
        print("Seu voto é OPCIONAL")
    else:
        print("Voto NEGADO")

ano = int(input("Digite o ano de seu nascimento:\n"))

voto(ano)


#Exercício nº 5

ficha = lambda nome, gols: print(f"JOGADOR: {nome}\nGOLS NA CARREIRA: {gols}.")

nome = input("Digite o nome do jogador:\n")
gols = int(input("Digite o números marcados pelo jogado:\n"))

ficha(nome,gols)

#Exercício nº 6

def notasProva(nota1,nota2,nota3):
    media_total = (nota1 + nota2 + nota3) / 3
    if (nota1 < nota2 and nota1 < nota3):
        nota_menor = nota1
        nota_maior1 = nota2
        nota_maior2 = nota3
    elif ( nota2 < nota3 and nota2 < nota1):
        nota_menor = nota2
        nota_maior1 = nota1
        nota_maior2 = nota3
    elif ( nota3 < nota1 and nota3 < nota2):
        nota_menor = nota3
        nota_maior1 = nota2
        nota_maior2 = nota1
    elif (nota1 == nota2 and nota1 < nota3):
        nota_menor = nota1
        nota_maior1 = nota3
        nota_maior2 = nota3
    elif (nota1 == nota2 and nota1 > nota3):
        nota_menor = nota3
        nota_maior1 = nota1
        nota_maior2 = nota1
    elif ( nota2 == nota3 and nota2 < nota1):
        nota_menor = nota2
        nota_maior1 = nota1
        nota_maior2 = nota1
    elif ( nota2 == nota3 and nota2 > nota1):
        nota_menor = nota1
        nota_maior1 = nota2
        nota_maior2 = nota2
    elif ( nota3 == nota1 and nota3 < nota2):
        nota_menor = nota3
        nota_maior1 = nota2
        nota_maior2 = nota2
    elif ( nota3 == nota1 and nota3 > nota2):
        nota_menor = nota2
        nota_maior1 = nota3
        nota_maior2 = nota3
    elif (nota1 == nota2 and nota1 == nota3):
        nota_menor = nota1
        nota_maior1 = nota1
        nota_maior2 = nota1
    elif ( nota2 == nota3 and nota2 == nota1):
        nota_menor = nota2
        nota_maior1 = nota2
        nota_maior2 = nota2
    elif ( nota3 == nota1 and nota3 == nota2):
        nota_menor = nota3
        nota_maior1 = nota3
        nota_maior2 = nota3
    media_alta = (nota_maior1 + nota_maior2) / 2
    print(f"Média coma as três provas: {media_total:.1f}")
    print(f"Média das maiores notas obtidas: {media_alta:.1f}")
    print(f"Suas nota maior é de {nota_maior2} e nota menor {nota_menor}")


nota1 = float(input("Digite a primeira nota:\n"))
nota2 = float(input("Digite a segunda nota:\n"))
nota3 = float(input("Digite a terceira nota:\n"))

notasProva(nota1,nota2,nota3)
'''

# DESAFIO 

'''
Hospedagem
1 - Crie uma função chamada 'custo_hotel' que receba um parâmetro (argumento) chamado 'noites' e retorne o custo total do hotel, sendo que 1 noite custa R$ 140,00.

'''
custo_hotel = lambda noites: print(f"Ok! então o custo total do hotel será de:\nR${(noites * 140):.2f}")
'''
noites = int(input("Quantas noite você passará no hotel:\n"))


custo_hotel(noites)

Passagem
2 - Crie uma função chamada 'custo_aviao' que receba o nome da cidade e retorne o custo da passagem de avião, sendo que passagem para:
- São Paulo custa R$ 312,00;
- Porto Alegre custa R$ 447,00;
- Recife custa R$ 831,00;
- Manaus custa R$ 986,00.


'''
def custo_aviao(cidade):
    cidad = cidade.upper()
    if (cidad == "SÃO PAULO"):
        print("O custo total da passagem é de R$312,00")
    elif (cidad == "PORTO ALEGRE"):
        print("O custo total da passagem é de R$447,00")
    elif (cidad == "RECIFE"):
        print("O custo total da passagem é de R$831,00")
    elif (cidad == "MANAUS"):
        print("O custo total da passagem é de R$986,00")
'''
cidade = input("Informe a cidade de destino:\n")

custo_aviao(cidade)

3 - Crie uma função chamada 'custo_carro' que receba um parâmetro chamado 'dias'.
- Calcule o custo do aluguel do carro sendo que:
- A cada dia o carro custa R$ 40,00;
- Alugando 7 dias ou +: R$ 50,00 de desconto;
- Alugando 3 dias ou +: R$ 20,00 de desconto;
- Você pode receber apenas um desconto;
- Retorne o custo.
'''
def custo_carro(dias):
    custo_do_carro = dias * 40
    if (dias >= 7 ):
        custo_com_desconto = custo_do_carro - 50
        print(f"O custo do alugue do carro por {dias} dias é de R${custo_com_desconto:.2f}")
    elif (dias >= 3 and dias < 7):
        custo_com_desconto = custo_do_carro - 20
        print(f"O custo do alugue do carro por {dias} dias é de R${custo_do_carro:.2f}")
'''
dias = int(input("Por quantos dias você quer alugar o carro?\n"))

custo_carro(dias)


Cálculo Total
4 - Agora com essas três funções criadas, declare uma função que receba a cidade e quantidade de dias e retorne o custo total da viagem.
- Reutilize as funções já criadas.
- Exiba o total da viagem chamando apenas a nova função declarada!

'''
cidade = input("Informe a cidade de destino:\n")
dias = int(input("Por quantos dias você quer alugar o carro?\n"))
noites = int(input("Quantas noite você passará no hotel:\n"))
def custoTotal(cidade, dias):
    custo_aviao(cidade)
    custo_carro(dias)
    custo_hotel(dias)

custoTotal(cidade,dias)

