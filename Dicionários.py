contatos = {"Gustavo":"1234-5678","Carlos":"2345-6789","Ana":"5373-9373","João":"7393-2882"}
contatos2 = {"gustavo":"1234-5678","Carlos":"2345-6789","Ana":"5373-9373","João":"7393-2882"}
#print(type(contatos[2][1]))
contatos3 = {"Joana":"1344-7463", "Marta":"6474-2665","Beto":"1673-6367"}
'''
print(contatos["Carlos"])

for k,v in zip(contatos.keys(),contatos2.values()):
    print(f"{k}-{v}")
c = contatos.clear()
print(c)
'''
'''
print(contatos.pop("gustavo","chave não encontrada"))

contatos.update(contatos2)
contatos.update(contatos3)
print(contatos)
'''
vigadores_lista = ["Miranha","Lóqui","Tânus","Bátima"]

for i,v in enumerate(vigadores_lista):
    print(f"{i} - {v}")