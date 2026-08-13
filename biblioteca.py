import csv

ARQUIVO = "livros.csv"

def carregar_livros():
    livros = []

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for livro in leitor:
                livros.append(livro)
    except FileNotFoundError:
        pass

    return livros

def salvar_livros(livros):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["título", "autor", "ano", "código", "status"]

        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(livros)

def cadastrar_livro(livros):
    print("\n===CADASTRAR LIVROS===")

    titulo=input("Digite o título: ")
    autor=input("Digite o nome do autor: ")
    ano=input("Digite o ano de publicação: ")
    codigo=input("Digite o código/ISBN: ")

    livro = {
        "Título": titulo,
        "Autor": autor,
        "Ano": ano,
        "Código": codigo,
        "Status": "Disponivel"

    }

    livros.append(livro)
    salvar_livros(livros)

    print("\nLivro cadastro com sucesso!")
    return livro