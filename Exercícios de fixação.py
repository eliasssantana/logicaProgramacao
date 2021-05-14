print("-=" * 20)
print(" " * 7,"Exercícios de fixação", " " * 7)
print("-=" * 20)

# Exercício nº 1

def temVogal():
    a = 0 ; e = 0 ; i = 0 ; o = 0 ; u = 0
    frase = input("Escreva uma frase:\n").lower()
    for letra in frase:
        if letra == "a":
            a += 1
        elif letra == "e":
            e += 1
        elif letra == "i":
            i += 1
        elif letra == "o":
            o += 1
        elif letra == "u":
            u += 1
    print(f"A frase tem {a} letras 'a', {e} 'e', {i} 'i', {o} 'o' e {u} 'u'.")


temVogal()

# Exercício nº 2

n = int(input("Digite um número:\n"))

for i in range(1,n + 1):
    if n % i == 0:
        print(i)

# Exercício nº 3



