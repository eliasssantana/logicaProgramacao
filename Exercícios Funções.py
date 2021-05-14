#Exercício nº1

n1 = int(input("Digite o primeiro numero:\n"))
n2 = int(input("Digite o segundo número:\n"))
n3 = int(input("Digite o terceiro número:\n"))

def soma(n1,n2 ,n3):
    return n1 + n2 + n3

print(soma(n1, n2, n3))

#Exercício nº2

argumento = input("Digite um argumento:\n").upper()
def arg(argument):
    if (argumento == "P"):
        return "positivo"
    elif(argumento == "N"):
        return "negativo"
    else:
        return 0
print(arg(argumento))

#Exercício nº3

tax = float(input("Digite a taxa:\n"))
cust = float(input("Digite o custo:\n"))

def somaImposto(taxaImposto,custo):
    taxImposto = taxaImposto / 100
    custo_mais_taxa = custo + (custo * taxImposto)
    return custo_mais_taxa

print(somaImposto(tax, cust))

#Exercício nº4

slrio = float(input("Digite seu salário:\n"))
hrs = float(input("Digite as horas trabalhadas na empresa:\n"))
def calculaSalario(salario,horasTrabalhadas):
    horas = salario / horasTrabalhadas
    hrsAdicionais = salario + horas + (horas * 0.5)
    if( horasTrabalhadas < 40):
        print(f"O salário do funcionário da empresa XYZ é de: {salario:.2f}")
    else:
        print(f"O salário do funcionário da empresa XYZ é de: {hrsAdicionais:.2f}")

print(calculaSalario(slrio, hrs))


#Exercício nº5

peso = float(input("Informe seu peso:\n"))
altura = int(input("Agora, infome sua altura:(em centímetros)\n"))
def calculaImc(p, a):
    alt_metros = a / 100
    imc = p / (alt_metros ** 2)
    print(f"Pelo dados informados seu IMC é de: {imc:.2f}")

calculaImc(peso, altura)

#Exercício nº6

nota_aluno = float(input("Digite sua nota:\n"))

def converteNota(nota):
    if (nota >= 9):
        print("Parabéns! Você tirou um A!")
    elif (nota >= 8 and nota < 9):
        print("Parabéns! Você tirou um B!")
    elif (nota >= 7 and nota < 8):
        print("Parabéns! Você tirou um C!")
    elif (nota >= 6 and nota < 7):
        print("Parabéns! Você tirou um D!")
    elif (nota <= 4):
        print("Infelizmente você tirou um F. Estude mais!")

converteNota(nota_aluno)

#Exercício nº7

def comparador():
    n1 = int(input("Digite um número:\n"))
    n2 = int(input("Digite um outro número "))

    if (n1 < n2):
        print(f"O valor {n1} é menor do que {n2}")
    elif (n2 < n1):
        print(f"O valor {n2} é menor do que {n1}")
    else:
        print(f"O valores {n1} e {n2} são iguais")
comparador()
print("Hello")

# Desafio 
'''
DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.
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
dataPorExtenso(data)
