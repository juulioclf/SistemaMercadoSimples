import os
from time import sleep

def limparTela():
    os.system("CLS")


def menuInicial():

    print("Seja bem-vindo ao sistema de mercado\n")
    print("1- Login como admin")
    print("2- Entar como user")
    print("0- Sair do sistema")

def telaAdminLogado():

    limparTela()
    print("Digite o que voce deseja fazer")
    print("1- Adicionar item")
    print("2- Remover item")
    print("0- Adicionar promocao")
    acaoAdmin = int(input("Digite o que deseja fazer: "))


def verificaEmailAdmin(email, senha):
    admin = [["@dm1n01"], ["m3rc4d0"]]
    if((email == "@dm1n01") and (senha == "m3rc4d0")):
        return True
    else:
        return False

    
def loginAdmin():
    limparTela()

    print("por favor, digite o email e a senha:")
    email = str(input("email: "))
    senha = str(input("senha: "))

    if(verificaEmailAdmin(email, senha)):
        print("email e senha corretos!")
        sleep(2)
        telaAdminLogado()
        print("apos o tela admin")

    else:
        print("email ou senha informados estão incorretos!")


        


