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
        "título": titulo,
        "autor": autor,
        "ano": ano,
        "código": codigo,
        "status": "Disponivel"

    }

    livros.append(livro)
    salvar_livros(livros)

    print("\nlivro cadastrado com sucesso!")
    return livro

def listar_livros(livros):
    print("\n===LISTA DE LIVROS===")

    if len(livros)==0:
        print("Nenhum livro cadastrado.")
        return False

    for livro in livros:
        print("------------------------")
        print("título: ", livro["título"])
        print("autor: ", livro["autor"])
        print("ano: ", livro["ano"])
        print("código: ", livro["código"])
        print("status: ", livro["status"])

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
            print("título: ", livro["título"])
            print("autor: ", livro["autor"])
            print("ano: ", livro["ano"])
            print("código: ", livro["código"])
            print("status: ", livro["status"])

    return encontrados

def emprestar_livro(livros):
    codigo = input("\n Digite o código/ISBN do livro: ")

    for livro in livros:
        if livro["código"] == codigo:

            if livro["status"] == "emprestado":
                print("Esse livro já está emprestado.")
                return False

            livro["status"] = "emprestado"
            salvar_livros(livros)

        print("Empréstimo registrado com sucesso!")
        return True

    print("Livro não encontrado.")
    return False

def devolver_livro(livros):
    codigo = input("\nDigite o código/ISBN do livro: ")

    for livro in livros:
        if livro["código"] == codigo:

            if livro["status"] == "disponível":
                print("Esse livro já está disponível.")
                return False

            livro["status"] = "disponivel"
            salvar_livros(livros)

            print("Devolução registrada com sucesso!")
            return True

    print("Livro não encontrado.")
    return False

def ordenar_livros(livros):
    print("\n===ORDENAR LIVROS===")
    print("1 - Por título")
    print("2 - Por autor")
    print("3 - Por ano")

    opcao = input("\nEscolha uma opção: ")

    if opcao=="1":
        livros.sort(key=lambda livro: livro["titulo"].lower())
        print("\nlivros ordenados por título.")

    elif opcao=="2":
        livros.sort(key=lambda livro: livro["autor"].lower())
        print("\nlivros ordenados por autor.")

    elif opcao=="3":
        livros.sort(key=lambda livro: livro["ano"].lower())
        print("\nlivros ordenados por ano.")

    else:
        print("\nOpção inválida.")
        return False

    listar_livros(livros)
    return True

def main():
    livros=carregar_livros()

    while True:
        print("\n========================================")
        print("      MENU PRINCIPAL: BIBLIOTECA")
        print("========================================")
        print("1- Cadastrar livro")
        print("2- Emprestar livro")
        print("3- Devolver livro")
        print("4- Listar livros")
        print("5- Buscar livro")
        print("6- Ordenar livros")
        print("7- Sair")

        opcao = input("\n Escolha uma opção: ")

        if opcao=="1":
            cadastrar_livro(livros)

        elif opcao=="2":
            emprestar_livro(livros)

        elif opcao=="3":
            devolver_livro(livros)

        elif opcao=="4":
            listar_livros(livros)

        elif opcao=="5":
            buscar_livros(livros)

        elif opcao=="6":
            ordenar_livros(livros)

        elif opcao=="7":
            print("\nPrograma encerrado.")
            break

        else:
            print("\nOpção inválida.")

main()