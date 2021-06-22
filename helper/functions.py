import os
from time import sleep

def limparTela():
    os.system("CLS")


def menuInicial():

    limparTela()
    print("Seja bem-vindo ao sistema de mercado\n")
    print("1- Login como admin")
    print("2- Entar como user")
    print("3- Sair do sistema")

def telaAdminLogado():

    limparTela()
    print("Digite o que voce deseja fazer")
    print("1- Adicionar item")
    print("2- Remover item")
    print("3- Adicionar promocao")
    acaoAdmin = int(input("Digite o que deseja fazer: "))
    
    if (acaoAdmin == 1):
        print("voce esta adicionando itens")
        sleep(2)

    elif (acaoAdmin == 2):
        print("voce esta removendo itens")
        sleep(2)
    
    elif(acaoAdmin == 3):
        print("voce esta adicionando uma promocao")
        sleep(2)

    else:
        print("digite um numero valido")
        sleep(2)


def verificaEmailAdmin(email, senha):

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

    else:
        limparTela()
        print("email ou senha informados estão incorretos!")
        sleep(2)
        acaoLogin = str(input("voce deseja sair? (sim/nao) ")).lower()
        
        if(acaoLogin == "sim"):
            print("voce esta sendo redirecionado para o menu inicial")
            sleep(2)
            menuInicial()
        elif(acaoLogin == "nao"):
            loginAdmin()
    
        else:
            print("por favor, digite uma entrada valida")
            sleep (2)





    
        
        


