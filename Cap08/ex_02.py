# Exercício 2 - 
# Crie uma classe chamada Pessoa() com os atributos: nome, cidade, telefone e e-mail. 
# Use pelo menos 2 métodos especiais na sua classe. 
# Crie um objeto da sua classe e faça uma chamada a pelo menos um dos seus métodos especiais.

class Pessoa():

    def __init__(self, nome:str, cidade:str, telefone:str, e_mail:str):
        self.nome = nome
        self.cidade = cidade
        self.telefone = telefone
        self.e_mail = e_mail
        pass
    
    def print_nome(self):
        print(self.nome)
        pass

    def print_cidade(self):
        print(self.cidade)
        pass

    def print_dados_contato(self):
        print(f"O telefone da pessoa fisica {self.nome} é {self.telefone} e seu contato de e-mail é {self.e_mail}, e ele(a) é um residente da cidade de {self.cidade}")
        pass

obj_01 = Pessoa("Guilherme", "Mumbai", "(48) 9 9999-9999", "Mumbai.Exterior@gmail.com")

obj_01.print_cidade()
obj_01.print_nome()
obj_01.print_dados_contato()

teste = obj_01.cidade

print(teste)