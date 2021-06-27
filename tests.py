vetor = [{'nome' : "maca", 'preco' : "10"}, {'nome' : "uva", 'preco' : "10"}, {'nome' : "pera", 'preco' : "10"}]

def addVetor(**kwargs):
    vetor.append(kwargs)

valor1 = "aaa"

dic1 = dict(chave = f'{valor1}')
print(dic1)