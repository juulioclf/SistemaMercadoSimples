def emailController(email):

    if ((email.find("@") > 0) and (email.find(".") > 0)):
        return True
    else:
        return False

def menuInicial():

    print("Seja bem-vindo ao sistema de mercado\n")
    print("1- Login")
    print("2- Cadastrar um usuario")



