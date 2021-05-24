print("=-" * 30)
e = 'Exercícios'
print(e.center(50))
print("=-" * 30)

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

advinhacao()