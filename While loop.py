'''
opc = 1
while opc == 1:
    num = float(input("Digite um número:\n"))
    if num == 0:
        print(f"O número digitado é: {num:.2f}.")
    elif num > 0:
        print(f"O número {num:.2f} é positivo.")
    else:
        print("O número é negativo.")

    resposta = input("Você quer finalizar?[s/n]\n")
    if resposta == "S" or resposta == "s":
        opc = 0
'''
'''
num_impares = int(input("Digite a quantidade de números ímpares: "))
cont = 0
while cont < num_impares * 2:
    if cont % 2 != 0:
        print(cont)
    cont += 1
'''

lista = [1,1,1,1,4]
'''
i = 0 
for cont in lista:
    i = i + lista.index(cont)
    i = i - 1
    if i == -0:
        print(lista[0])
    print(lista[i])
'''
'''
aux = len(lista)

for i in range(aux, 0, -1):
    print(lista[i - 1])
'''
'''
num = 1
cont = 1
cpo = 0
qtd = int(input('quantidade de elementos impares na lista: '))
array = []
'''
'''
while cpo == 0:
  while cont <= qtd:
    array.append(num)
    cont+=1
    num+=2

  print()
  print(f'lista de elementos: {array}')

  for eachNum in array:
    revertido = sorted(array, reverse= True)
  print(f'lista invertida: {revertido}',end=' ')

  resp = input('Deseja continuar?[s/n]: ').lower().trim()

  if resp == 's':
    cpo = 0
    qtd = int(input('quantidade de elementos impares na lista: '))
  elif resp == 'n':
    cpo = 1
  else:
    print('resposta invalida...')
    resp = input('Deseja continuar?[s/n]: ').lower().strip()[0]

print('fim do programa')
'''