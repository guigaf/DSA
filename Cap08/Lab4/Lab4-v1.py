# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random
import json
import os
from os import system, name

palavras = []

# Board (tabuleiro)
board = ['''
>>>>>>>>>>Hangman<<<<<<<<<<

 +---+
 |   |
 O   |
/|\  |
 |   |
/ \  |
=========''', '''


 +---+
 |   |
 O   |
/|\  |
 |   |
/    |
=========''', '''


 +---+
 |   |
 O   |
/|\  |
 |   |
     |
=========''', '''


 +---+
 |   |
 O   |
/|   |
 |   |
     |
=========''', '''


 +---+
 |   |
 O   |
 |   |
 |   |
     |
=========''', '''


 +---+
 |   |
 O   |
     |
     |
     |
=========''', '''


 +---+
 |   |
     |
     |
     |
     |
=========''']


# Classe
class Hangman():

     # Método Construtor
     def __init__(self):
          self.chances = 6
          self.palavra = " "
          self.rodando_vitoria_derrota = 0
          self.letras_descobertas = []
          self.letras_erradas = []
          pass

     # Limpa tela
     def limpa_tela(self):
          if name == "nt":
               _ = system("cls")
          else:
               _ = system("clear")
          pass

     # Método para adivinhar a letra
     def adivinha_letra(self):
          tentativa = input("\nDigite uma letra: ").lower()
          if tentativa in self.palavra:
               index = 0
               for letra in self.palavra:
                    if tentativa == letra:
                         self.letras_descobertas[index] = letra
                    index += 1
                    pass
               pass
          else:
               self.chances -= 1
               self.letras_erradas.append(tentativa)
               pass

	# Método para verificar se o jogo terminou
     def verifica_derrota(self):
          if "_" in self.letras_descobertas and self.chances <= 0:
               print("\nVocê perdeu, a palavra era:", self.palavra)
               print("\nParabéns. Você está aprendendo programação em python com a DSA. :)\n")
               self.rodando_vitoria_derrota = 2
               return self.rodando_vitoria_derrota
          return self.rodando_vitoria_derrota

	# Método para verificar se o jogador venceu
     def verifica_vitoria(self):
          if "_" not in self.letras_descobertas:
               print("\nVocê venceu, a palavra era:", self.palavra)
               print("\nParabéns. Você está aprendendo programação em python com a DSA. :)\n")
               self.rodando_vitoria_derrota = 1
               return self.rodando_vitoria_derrota
          return self.rodando_vitoria_derrota

     def verifica_palavra(self):
          # Obtém o diretório do script
          script_dir = "C:\Geral\DEV\DSA\Cap08\Lab4"

          # Caminho absoluto para o arquivo config.json
          config_path = os.path.join(script_dir, 'palavras.json')

          # Lê as credenciais do arquivo JSON
          with open(config_path) as config_file:
               config_data = json.load(config_file)

          # Obtem a lista de palavras do arquivo JSON
          palavras = list(config_data.values())
          
          # Escolhe pseudo-aleatóriamente uma das palavras
          self.palavra = random.choice(palavras)

          # Esconde a palavra em forma de "_"
          self.letras_descobertas = ["_" for letra in self.palavra]
          
          pass
     
	# Método para checar o status do game e imprimir o board na tela
     def verifica_board(self):
          print("\nBem-vindo(a) ao jogo da forca!")
          print("Advinhe a palavra abaixo:\n")
          print(board[self.chances])
          print(" ".join(self.letras_descobertas))
          print("Letras Erradas:", " ".join(self.letras_erradas))
          pass

# Bloco main
if __name__ == "__main__":
     jogador_01 = Hangman()
     while True:
          if jogador_01.palavra == " ":
               jogador_01.verifica_palavra()
               pass
          jogador_01.limpa_tela()
          jogador_01.verifica_board()
          jogador_01.adivinha_letra()
          if jogador_01.rodando_vitoria_derrota == 0:
               jogador_01.verifica_vitoria()
               if jogador_01.rodando_vitoria_derrota == 0:
                    jogador_01.verifica_derrota()
                    pass
               pass
          if jogador_01.rodando_vitoria_derrota != 0:
               jogador_01.limpa_tela()
               jogador_01.verifica_board()
               jogador_01.verifica_vitoria()
               jogador_01.verifica_derrota()
               break