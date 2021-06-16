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


def menuLogin():
    
    print("esse eh o menu login")

def menuCadastro():
    
    print("esse eh o menu cadastro")





