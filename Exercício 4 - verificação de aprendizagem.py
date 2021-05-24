print("=-" * 30)
e = 'Exercício'
print(e.center(50))
print("=-" * 30)

# 04)
'''
- Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato escrito por extenso. Valide a data e retorne NULL caso a data seja inválida.
'''
meses =["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Desembro"]
data = str(input("Digite uma data no seguinte formato:\n[DD/MM/AAAA]\n"))

def dataPorExtenso(data):
    data1 = data.split('/')
    dia = data1[0]
    dia_int = int(dia)
    mes = data1[1]
    mes_int = int(mes)
    ano = data1[2]
    ano_int = int(ano)
    if (mes_int != 0 and ano_int != 0 and dia_int != 0):
        if ano_int % 4 == 0 and ano_int % 100 != 0 or ano_int % 400 == 0:
            print(ano_int)
            if(mes == '02' and dia_int > 29):
                print("Null")
            else:
                for m in meses:
                    month = meses.index(m)
                    if ( mes_int == (month + 1)):
                        print(f"{dia}/{m}/{ano}")
        else:
            if(mes == '02' and dia_int > 28):
                print("Null")
            else:
                for m in meses:
                    month = meses.index(m)
                    if ( mes_int == (month + 1)):
                        print(f"{dia}/{m}/{ano}")
    else:
        print("DATA INVÁLIDA!")
dataPorExtenso(data)
