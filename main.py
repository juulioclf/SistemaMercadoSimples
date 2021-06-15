import functions

acaoDesejada = 0
functions.limparTela()
functions.menuInicial()
acaoDesejada = int(input("Digite a opcao desejada: "))


if(acaoDesejada == 1):
    print("opcao desejada: Login")
    functions.limparTela()
    functions.menuLogin()


elif(acaoDesejada == 2):
    print("opcao desejada: Cadastro de Usuario")
    functions.limparTela()
    functions.menuCadastro()


else:
    print("por favor, digite um numero valido")
    functions.limparTela()
    functions.menuInicial()
    acaoDesejada = int(input("Digite a opcao desejada: "))


