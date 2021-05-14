casado = 0
solteiro = 0
for cont in range(1,16):
    estado_civil = input("Digite seu estado civil:[casado ou solteiro]").lower()
    if estado_civil == 'c':
        casado += 1
    else:
        solteiro += 1

print(f"A quantidade de casados é de {casado} e solteiros é de {solteiro}")

