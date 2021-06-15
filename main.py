import os
import functions

acaoDesejada = 0
functions.menuInicial()
acaoDesejada = int(input("Digite a opcao desejada: "))


if(acaoDesejada == 1):
    print("opcao desejada: Login")
    os.system("CLS")
    functions.menuLogin()


elif(acaoDesejada == 2):
    print("opcao desejada: Cadastro de Usuario")
    os.system("CLS")
    functions.menuCadastro()


else:
    print("por favor, digite um numero valido")
    functions.menuLogin()

