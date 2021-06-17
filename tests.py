import json

def escrever_json(dados):
    with open("archives/users.txt", "a") as file:   
        file.write(",")
        json.dump(dados, file)
        file.close()

email = str(input("digite o seu email: "))
senha = str(input("digite a sua senha: "))

dictjson = {"email": email, "senha": senha}

escrever_json(dictjson)