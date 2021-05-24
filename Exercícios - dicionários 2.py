print("=-" * 30)
e = 'Exercícios'
print(e.center(50))
print("=-" * 30)

# 1)
'''
Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas de um supermercado. Não esqueça de fazer as seguintes validações:
Produto Indisponível
Produto Inválido
Quantidade solicitada não disponível 
O programa deverá mostrar para o cliente a quantidade de itens comprados e o total
'''
from time import sleep

def compras():
    total = []
    quantidade = 0
    comprando = True
    estoque = {"Batata": [200, 2.00],"Macaxeira":[300,1.50],"Inhame":[100,2.50],'Tomate':[400,1.00] ,"Cebola":[200,0.60],"Alface":[100,1.50]}
    for k,v in estoque.items():
        print("-" * 30)
        print('|', k,f"R${v[1]:.2f}" )
        print("-" * 30)
    while comprando == True:
        compra = input("Digite o nome do produto:\n").capitalize()
        while compra not in estoque:
            print("PRODUTO INVÁLIDO")
            compra = input("Digite o nome do produto:\n").capitalize()
        if estoque[compra][0] == 0:
            print("PRODUTO INDISPONÍVEL")
            cont = input("Quer continuar comprando?[S \ N]\n").upper().strip()
            while cont not in "SN":
                print("RESPOSTA INVÁLIDA\n DIGITE NOVAMENTE...\n").upper().strip()
            if cont == "N":
                print(f" => Quantidade de itens comprados: {quantidade}\ntotal de: R${t:.2f}")
                print('=-' * 30)
                b = "VOLTE SEMPRE"
                print(b.center(50))
                print('=-' * 30)
                print()
                print("FINALIZANDO PROGRAMA...")
                sleep(2)
                break
            else:
                print("Aguarde...")
                sleep(2)
                print("Continuando.")
        else:
            pass
        qtd = int(input(f"Digite a quantidade de {compra}:\n"))
        if qtd > estoque[compra][0]:
            print("Quantidade solicitada não disponível")
        else:
            print("Processando sua solicitação...")
            sleep(2)
            print("Processado.")
            estoque[compra][0] -= qtd
            quantidade += qtd
            q = qtd * estoque[compra][1]
            total.append(q)
            t = sum(total)
        cont = input("Quer continuar comprando?[S \ N]\n").upper().strip()
        while cont not in "SN":
            print("RESPOSTA INVÁLIDA\n DIGITE NOVAMENTE...\n").upper().strip()
        if cont == "N":
            print(f"=> Quantidade de itens comprados: {quantidade}\ntotal de: R${t:.2f}")
            comprando = False
        else:
            print("Aguarde...")
            sleep(2)
            print("Continuando.")
# compras()

# 2)
'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feito em cada partida. No final tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
def jogador():
    jogador = {}
    nome = input("Digite o seu nome:\n").title().strip()
    jogador['nome'] = nome
    partidas = int(input("Quantas partidas você jogou?\n"))
    jogador['nº partidas'] = partidas
    if partidas > 0:
        for i in range(partidas):
            jogador[f'partida {i + 1}'] = input(f"Quantidade de gols na {i + 1}ª partida:\n") + " gols"
        print("=-" * 30)
        for k,v in jogador.items():
            print(f"{k}: {v}")
    else:
        print("=-" * 30)
        for k,v in jogador.items():
            print(f"{k}: {v}")

# jogador()

# 3)
'''
Uma escola te contratou para desenvolver um programa em Python para que o professor gerencie as notas de seus alunos. Seu programa deve apresentar o seguinte menu:
0. Sair
1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
2. Inserir aluno e nota
3. Alterar a nota de um aluno
4. Consultar nota de um aluno específico 
5. Apagar um aluno da lista
6. Exibir a média da turma
As notas e os nomes dos alunos serão fornecidos pelo professor. Implemente a sua solução utilizando dicionário.
'''
def notas():
    rodando = True
    alunos = []
    while rodando == True:
        aluno = {}
        print(
        '''0. Sair
            1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)
            2. Inserir aluno e nota
            3. Alterar a nota de um aluno
            4. Consultar nota de um aluno específico 
            5. Apagar um aluno da lista
            6. Exibir a média da turma''')
        opc = int(input("Digite a opção desejada:\n"))
        while opc > 6:
            print("Opção inválida!")
            opc = int(input("Digite a opção desejada:\n"))
        if opc == 2:
            aluno['aluno'] = input("Digite o nome do aluno:\n").title().strip()
            aluno['nota'] = float(input("Digite a nota do aluno:\n"))
            alunos.append(aluno)
        elif opc == 3:
            nome = input("Digite o nome do aluno cuja nota você quer alterar:\n").title().strip()
            altera_nota = float(input("Digite a nova nota do aluno:\n"))
            if nome in (i['aluno'] for i in alunos):
                for i,v in enumerate(alunos):
                    if v['aluno'] == nome:
                        v['nota'] = altera_nota
            else:
                print("Aluno não encontrado em nosso banco de dados.")   
        elif opc == 1:
            if alunos != []:
                for i in alunos:
                    print(f"{i['aluno']} tirou {i['nota']}")
            else:
                print("Ainda não há alunos cadastrados. Cadastre um aluno e tente novamente")
        elif opc == 0:
            rodando = False
        elif opc == 4:
            nome_aluno = input("Digite a nome do aluno que você quer ver a nota:\n").title().strip()
            if nome_aluno in (i['aluno'] for i in alunos):
                for i in alunos:
                    if i['aluno'] == nome_aluno:
                            print(f"nota do aluno/a: {i['nota']}")
            else:
                print("Aluno não encontrado")
        elif opc == 5:
            aluno_remove = input("Digite o nome do aluno que você deseja remover:\n").title().strip()
            if aluno_remove in (i['aluno'] for i in alunos):
                for i,v in enumerate(alunos):
                    if v['aluno'] == aluno_remove:
                        del alunos[i]
                        print("Aluno removido")
                        print(alunos)
            else:
                print("Aluno não encontrado")

        else:
            media = []
            for i in alunos:
                media.append(i['nota'])
            media = sum(media) / len(media)
            print(f"A média da turma é de: {media:.1f}.")
# notas()

# 4)
'''
Crie um programa onde você cadastre a data de nascimento (dd/mm/aa) de algumas celebridades em um dicionário. Ao escolher uma celebridade, seu programa deve retornar a data completa. Não esqueça de validar se a celebridade escolhida está presente em seu dicionário.
'''
def celebridades():
    celebridades = {'Albert Eistein':'14/03/1879','Benjamin Franklin':'17/01/1790','Chuck Norris':'10/03/1940','Donald Trump':'14/06/1946','Bruce Lee':'27/11/1940','Rowan Atkinson':'06/01/1955'}
    print("Seja bem-vindo ao nosso calendário!\nSabemos a data de nascimento das seguintes celebridades:\n")
    for k in celebridades.keys():
        print(k)

    celebridade = input("De quem você gostaria de saber a data de nascimento?\n").title().strip()
    trecho = celebridade[0:4]
    for celebe in celebridades.keys():
        if trecho == celebe[0:4]:
            print(f'você quis dixer {celebe}?')
    if celebridade in celebridades.keys():
        for k,v in celebridades.items():
            if k == celebridade:
                print(f"{k} nasceu nessa data: {v}")
    else:
        print("Celebridade não encontrada em nosso banco de dados.")