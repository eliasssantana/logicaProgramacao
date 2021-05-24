print("=-" * 30)
e = 'Exercícios'
print(e.center(50))
print("=-" * 30)

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

vogais()
