"""
class Usuario():
    def __init__(self, nome, email, senha, tipo):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.tipo = tipo
"""

class Produto:

    

    def __init__(self: object, nome: str, preco: int) -> None:
        contador: int = 1000
        self.__codigo = contador
        self.__nome = nome
        self.__preco = preco
        contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def preco(self: object) -> float:
        return self.__preco


        








