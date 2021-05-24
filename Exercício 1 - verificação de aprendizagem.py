print("=-" * 30)
e = 'Exercícios'
print(e.center(50))
print("=-" * 30)

# 01)
'''
- Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:
•	A soma deles;
•	A multiplicação entre eles;
•	A divisão  inteira deles;
•	Mostre na tela qual é o maior;
•	Verifique se o resultado da soma é par ou ímpar e mostre na tela;
•	Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40.
'''
def doisNum(x,y):
    soma = x + y
    multiplicacao = x * y
    divisao = x / y
    divisaoInt = x // y
    print(soma)
    print(multiplicacao)
    print(f'{divisao:.1f}')
    if x > y:
        print(f"{x} é o maior.")
    elif y > x:
        print(f"{y} é o maior.")
    else:
        print(f"{x} e {y} são iguais.")

    if soma % 2 == 0:
        print("O resultado da soma é par")
    else:
        print("O resultado da soma é ímpar")
    
    if multiplicacao > 40:
        res = multiplicacao / divisaoInt
        print(res)
    else:
        print("resultado da multiplicação não foi maior que 40")

doisNum(20,12)