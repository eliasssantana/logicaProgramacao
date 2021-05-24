print("=-" * 30)
e = 'Exercícios - Extras'
print(e.center(50))
print("=-" * 30)

# 1)
'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
def listaOrdenada():
    valores = []
    for i in range(5):
        valor = int(input(f"Digite o {i + 1}º valor:"))
        if i == 0 or valor > valores[-1]:
            valores.append(valor)
        else:
            for v in range(len(valores)):
                if valor < valores[v]:
                    valores.insert(v,valor)
                    break
    print(valores)

# listaOrdenada()

# 2)
'''	
Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
def numeros():
    num_digitados = 0
    lista_valores = []
    for i in range(10):
        num = int(input("Digite um número:\n"))
        num_digitados += 1
        lista_valores.append(num)
    lista_valores.sort(reverse=True)
    print(lista_valores)
    if 5 in lista_valores:
        print('O número 5 está presente na lista.')
    else:
        print('O número 5 não está presente na lista.')
# numeros()


# 3)
'''	
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Palíndromo, do grego palin (novo) e dromo (percurso), é toda palavra ou frase que pode ser lida de trás para a frente e que, independentemente da direção, mantém o seu sentido. Ex: arara, asa, ovo, oco.
'''

def palindromo():
    frase = input('Digite uma frase para saber se é um palíndromo:\n').lower().replace(' ','').replace('-','').replace('-','').replace('ô','o').replace('é','e').strip()
    frase_lista = list(frase)
    ao_contrario = list(frase)
    ao_contrario.reverse()
    if frase_lista == ao_contrario:
        print("A palavra é um palíndromo.")
    else:
        print("Palavra não é um palíndromo.")
# palindromo()

# 4)	
'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
def contador(inicio = 1,fim = 11,passo = 1):
    for i in range(inicio,fim,passo):
        print(i, end='')
    for i in range(10, -1,-1):
        print(i)

contador(15,-1,-2)
