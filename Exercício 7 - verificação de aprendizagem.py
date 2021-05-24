print("=-" * 30)
e = 'Exercício'
print(e.center(50))
print("=-" * 30)

# 7) 
'''
- Crie um programa onde o usuário possa digitar sete valores numéricos  e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares  em ordem crescente.
'''
def valores():
    par = []
    impar = []
    todos = []
    print("Digite sete valores numéricos:\n")
    for i in range(1,8):
        v = int(input(f"Digite o {i}º valor:\n"))
        if v % 2 == 0:
            par.append(v)
        else:
            impar.append(v)
    todos.append(par)
    todos.append(impar)
    for i,v in enumerate(todos):
        if i == 0:
            print('Valores pares:') 
            print(v)
        else:
            print("Valores ímpares:")
            print(v) 
    ordenado_par = sorted(par)
    ordenado_impar = sorted(impar)
    ordenado_par.extend(ordenado_impar)
    print('lista completa:')
    print(ordenado_par)
valores()