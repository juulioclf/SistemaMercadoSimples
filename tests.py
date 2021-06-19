import classes
import functions
from archives import users
import json

"""
so preciso dar o append na lista que esta em usuarios, 
mas como vou pegar o (pessoaLista) de usuarios??



julio = classes.Usuario("juli323o", "j@gmail.com", "123", "1")
dicPessoa = functions.criarUsuario(julio)
with open('archives/users.txt', "a") as f:
    f.write(str(dicPessoa) + ", ")



with open('archives/users.py', 'r') as f:
    arquivo = f.read()
    print(arquivo.split(",\n"))

"""



with open('archives/users.py', 'r') as f:
    arquivo = f.read()

    for elemento in arquivo:
        
    

