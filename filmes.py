filmes = ["Forrest Gump","Harry Potter","Os vingadores","O senhor dos anéis","Em ritmo de fuga"]
print(filmes)
'''
filmes.append("De volta para o futuro")
print(filmes)
a = []
b = input("Digite um filme:\n")
a.append(b)
print(a)
'''
filmes_novos = ["O hibbit","Um lugar silencioso"]

filmes.extend(filmes_novos)
# print(filmes)

for filme in filmes:
    print(filme)

filmes.insert(2,"king Kong vs Godzilla")
filmes.sort()
print(filmes)
print(filmes)
for filme in filmes:
    print(filme)

del filmes[2]
print(filmes)

print(len(filmes))

