vetor = [{'nome' : "maca", 'preco' : "10"}, {'nome' : "uva", 'preco' : "10"}, {'nome' : "pera", 'preco' : "10"}]

def addVetor(**kwargs):
    vetor.append(kwargs)

vetor1 = []

def validaEntrada(*args):
    
    for i in args:
        if i == " ":
            auxiliar = True
        else:
            auxiliar = False

    return auxiliar

a = input(" ")
print(bool(a))

