a = [1,4,6,7,3,8,3,2]
b = [4,6,8,8,3,2,9]
c = a + b
c.sort()
print(c)

preco = float(input('Digite o preço do produto:\n(Digite 0 para sair)\n: '))
produto = input('Digite o nome do produto:\n ')

produtos = []
produtos.append(produto)

precos = []
precos.append(preco)

while preco != 0:
        preco = float(input('Digite o preço do produto:\n(Digite 0 para sair)\n'))
        if preco != 0:
            produto = input('Digite o nome do produto:\n')
            produtos.append(produto)
            precos.append(preco)
len_pro = len(produtos)
for i in range(len_pro):
    if precos[i] == 0:
        pass
    else:
        print(f'produto {i + 1}: {produtos[i]} : R${precos[i]:.2f}')

total_compra = sum(precos)
print(f"O total foi de R${total_compra:.2f}")
valor_pago = float(input("Digite o valor que vai pagar:\n"))
troco = valor_pago - total_compra
print(f'Total da Compra:{"" * 30} R${total_compra:.2f}')
print(f'Total pago:{"" * 30} R${valor_pago:.2f}')
print(f'Troco: R${troco:.2f:<40}')
print("-=" * 40)
print(" " * 25 ,"Obigado pela preferência!", " " * 25)
print("-=" * 40)

