import os

def limparTela():
    os.system("CLS")

def menuInicial():

    print("Seja bem-vindo ao sistema de mercado\n")
    print("1- Login como admin")
    print("2- Entar como user")
    print("0- Sair do sistema")

def telaAdmin():

    print("Digite o que voce deseja fazer")

def verificaAdmin(email, senha):
    admin = [["@dm1n01"], ["m3rc4d0"]]
    if((email == admin[0]) and (senha == admin[1])):
        return True
    else:
        return False

    
def loginAdmin():

    print("por favor, digite o email e a senha:")
    email = str(input("email: "))
    senha = str(input("senha: "))

    try:
        verificaAdmin(email, senha)
    except False:
        print("email ou senha inseridos estao errados")
    finally:
        telaAdmin():


        


