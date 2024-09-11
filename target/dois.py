# Este programa calcula a aparição da letra 'a' ou 'A' em uma string inserida pelo usuário


def verificacao(string):
    # Converte a string para minúsculas e conta as ocorrências de 'a'
    cont = string.lower().count('a')

    # Verifica se 'a' foi encontrado
    if cont > 0:
        return f"A letra 'a' ocorre {cont} vezes na string."
    else:
        return "A letra 'a' não foi encontrada na string."

# Execução da função
print(verificacao(input("Digite algo:")))