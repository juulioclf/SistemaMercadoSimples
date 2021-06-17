import os
import classes 

def emailController(email):

    if ((email.find("@") > 0) and (email.find(".") > 0)):
        return True
    else:
        return False

def limparTela():
    os.system("CLS")

def menuInicial():

    print("Seja bem-vindo ao sistema de mercado\n")
    print("1- Login")
    print("2- Cadastrar um usuario")


def menuLogin(email, senha):
    pass
    

def menuCadastro(email, senha):
    
    file = open('archives/users.txt', 'w')
    
    if(emailController(email)):
        file.write(email)
        file.write(senha)
    else:
        print("email invalido")

    file.close()



