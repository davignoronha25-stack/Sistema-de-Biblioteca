import csv

ARQUIVO = "livros.csv"

def carregar_livros():
    livros = []

    try:
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)
            for livros in leitor:
                livros.append(livros)
    except FileNotFoundError:
        pass

    return livros

def salvar_livros(livros):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["título", "autor", "ano", "código", "status"]