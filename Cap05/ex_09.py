# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra "a" no nome
palavras = ["maça", "coiote", "banana", "terreno", "Python"]

# nova_lista = [valor_caso_seja_modificado for cada_item_pertencente_a_lista_a_seguir in de_onde_se_esta_pegando_valor if condicao_caso_necessario]
# nova_lista = [expressao for elemento in iteravel]
lista = [x for x in palavras if "a" in x]

print(list(lista))
