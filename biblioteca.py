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

def listar_livros(livros):
    print("\n===LISTA DE LIVROS===")

    if len(livros)==0:
        print("Nenhum livro cadastrado.")
        return False

    for livro in livros:
        print("------------------------")
        print("Título: ", livro["título"])
        print("Autor: ", livro["autor"])
        print("Ano: ", livro["ano"])
        print("Código: ", livro["codigo"])
        print("Status: ", livro["status"])

    return True

def buscar_livros(livros):
    termo=input("\nDigite o título ou autor que deseja buscar: ")

    encontrados = []

    for livro in livros:
        if (termo.lower()in livro["título"].lower()or
                termo.lower()in livro["autor"].lower()):

            encontrados.append(livro)

    if len(encontrados) == 0:
        print("\nNenhum livro encontrado.")
    else:
        print("\n===Livros Encontrados===")

        for livro in encontrados:
            print("-----------------------")
            print("Título: ", livro["título"])
            print("Autor: ", livro["autor"])
            print("Ano: ", livro["ano"])
            print("Código: ", livro["código"])
            print("Status: ", livro["status"])

    return encontrados