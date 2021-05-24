print("=-" * 30)
e = 'Exercício'
print(e.center(50))
print("=-" * 30)

# 05)
'''
- Refatore o exercício2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras que foram retiradas da frase original.
'''
def vogais2():
    palavra = input("Digite uma palavar ou frase:\n").upper().strip()
    vogais = 0
    p = list(palavra)
    for i in palavra:
        if i in 'AEIOU':
            vogais += 1
            p.remove(i)
    ''.join(p)
    p2 = str(p).strip('[]')
    print(vogais)
    print(p2)
vogais2()