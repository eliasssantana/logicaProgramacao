print("-=" * 30)
print("=-" * 11,"Exercícios","=-" * 11)
print("-=" * 30)
# Exercício nº1
'''
1.	Exercício Treino - Crie um dicionário em que suas chaves serão os números 1, 4, 5, 6, 7, e 9 (que podem ser armazenados em uma lista) e seus valores correspondentes aos quadrados desses números.
{1: 1, 4: 16, 5: 25, 6: 36, 7: 49, 9: 81}  
'''

chaves = [1,4,5,6,7,9]
quadrado = {}
for i in chaves:
    quadrado[i] = i ** 2

print(quadrado)

# Exercício nº 2

'''
2.	Exercício Treino - Crie um dicionário em que suas chaves correspondem a números inteiros entre [1, 10] e cada valor associado é o número ao quadrado.
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100} 
'''
