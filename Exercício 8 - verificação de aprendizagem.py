print("=-" * 30)
e = 'Exercício'
print(e.center(50))
print("=-" * 30)

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
    pessoa['idade'] = idade
    aposentadoria = pessoa['ano de contratação'] + 35
    pessoa['idade_aposentadoria'] =  (aposentadoria - 2021) + idade
    pessoa['aposentadoria'] = aposentadoria
    for k,v in pessoa.items():
        print(f'{k} - {v}')

aposentadoria()