# Exercício 3 - 
# Crie a classe Smartphone com 2 atributos, tamanho e interface 
# Crie a classe MP3Player com os atributos capacidade. 
# A classe MP3player deve herdar os atributos da classe Smartphone.

class Smartphone():
    
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface
        pass
    def print_tamanho(self):
        print(self.tamanho)
        pass
    def print_interface(self):
        print(self.interface)
        pass

class MP3Player(Smartphone):
    def __init__(self, tamanho, interface):
        Smartphone.__init__(self, tamanho, interface)
        pass

meu_MP3 = MP3Player(1, 2)

meu_MP3.print_interface()
meu_MP3.print_tamanho()