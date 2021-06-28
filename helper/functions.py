import os
from time import sleep

produtoVetor = []


def limparTela():

    os.system("CLS")


def menuInicial():

    limparTela()
    print("Seja bem-vindo ao sistema de mercado")
    print("1- Login como admin")
    print("2- Entar como user")
    print("3- Sair do sistema")


def estaVazio(vetor):
    if produtoVetor == []:
        return True
    else:
        return False
    

def validaEntrada(*args):
    for i in args:
        if i:
            return True
        else:
            return False


def produtoJaExiste(produtoNome):
    
    if estaVazio(produtoVetor):
        return True

    for i in produtoVetor:
        if i['nome'] == produtoNome:
            return False

        else:
            return True


def addProdutoAdmin(**kwargs):
    produtoVetor.append(kwargs)


def processoProdutoAdmin():

    limparTela()
    produtoNome = input("Digite o nome do produto: ")
    produtoPreco = input("Digite o preco do produto: ")

    if validaEntrada(produtoNome, produtoPreco):
        pass
    else:
        print("por favor, digite uma entrada valida")
        sleep(2)
        processoProdutoAdmin()
    
    
    if(produtoJaExiste(produtoNome)):   

        addProdutoAdmin(nome = produtoNome, preco = produtoPreco, promocao = False)
        print(f"{produtoNome} adicionado com sucesso!")

        addProduto = input("Deseja adicionar mais produtos? (sim/nao) ").lower()
        processoProdutoAdmin() if (addProduto == "sim") else telaAdminLogado()

    else:
        print(f"{produtoNome} ja existe!")
        acao = input("digite SAIR caso deseje sair, caso contrario pressione ENTER: ").upper()

        telaAdminLogado() if (acao == "SAIR") else processoProdutoAdmin()


def popItemAdmin():

    print()


def addPromocaoAdmin():

    print()


def mostrarProdutos():

    for i in produtoVetor:
        print(f"o produto {i['nome']}, está custando R${i['preco']}")
    input("pressione ENTER para sair ")
    telaAdminLogado()


def telaAdminLogado():

    limparTela()
    print("Digite o que voce deseja fazer")
    print("1- Adicionar item")
    print("2- Remover item")
    print("3- Mostrar itens e seus detalhes")
    print("4- Adicionar promocao em um item")
    print("5- Voltar ao menu inicial")
    acaoAdmin = int(input("Digite o que deseja fazer: "))
    
    if (acaoAdmin == 1):
        limparTela()
        print("redirecionando para a pagina de ADICIONAR itens")
        sleep(2)
        processoProdutoAdmin()

    elif (acaoAdmin == 2):
        print("redirecionando para a pagina de REMOVER itens")
        sleep(2)
    
    elif(acaoAdmin == 3):
        limparTela()
        print("redirecionando para a pagina de MOSTRAR itens")
        sleep(2)
        mostrarProdutos()
    
    elif(acaoAdmin == 4):
        print("redirecionando para a pagina de ADICIONAR PROMOCAO itens")
        sleep(2)

    elif(acaoAdmin == 5):
        limparTela()
        print("voce esta sendo redirecionado para o menu inicial")
        sleep(2)
        menuInicial()

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
    email = input("email: ")
    senha = input("senha: ")

    if(verificaEmailAdmin(email, senha)):
        print("email e senha corretos!")
        sleep(2)
        telaAdminLogado()

    else:
        limparTela()
        print("email ou senha informados estão incorretos!")
        sleep(2)
        acaoLogin = input("voce deseja tentar novamente? (sim/nao) ").lower()
        
        if(acaoLogin == "nao"):
            print("voce esta sendo redirecionado para o menu inicial")
            sleep(2)
            menuInicial()

        elif(acaoLogin == "sim"):
            loginAdmin()
    
        else:
            print("por favor, digite uma entrada valida")
            sleep (2)

    





    
        
        


