from helper import functions 
from time import sleep


acao = 11
while( acao != 0):

    functions.limparTela()
    functions.menuInicial()
    acao = int(input("digite a acao desejada: "))

    if(acao == 1):
        print("indo para o login de admin..")
        sleep(2)
        functions.loginAdmin()

    elif(acao == 2):
        print("entrando como usuario..")

    else:
        print("por favor, digite um numero valido!")
        sleep(2)

