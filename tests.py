vetor = [{'nome' : "maca", 'preco' : "10"}, {'nome' : "uva", 'preco' : "10"}, {'nome' : "pera", 'preco' : "10"}]

def addVetor(**kwargs):
    vetor.append(kwargs)


for i in vetor:
    print(i['nome'])