import sqlite3, time
from tabulate import tabulate

users = sqlite3.connect("users.db")
cursor_users = users.cursor()
cursor_users.execute("CREATE TABLE IF NOT EXISTS users (login TEXT, senha TEXT)")
prod = sqlite3.connect("prod.db")
cursor_prod = prod.cursor()
cursor_prod.execute("CREATE TABLE IF NOT EXISTS prod (name TEXT, ref INTEGER, price FLOAT, estoque INTEGER)")
client = sqlite3.connect("clients.db")
cursor_client = client.cursor()
cursor_client.execute("CREATE TABLE IF NOT EXISTS clients (name TEXT, id VARCHAR(11) NOT NULL, endereco TEXT, bairro TEXT, cep VARCHAR(8) NOT NULL, cidade TEXT, estado TEXT)")

def selecaoSistema():
    print("\033c")
    print("===== SISTEMA A2F ====\n")

    print("1 - Login")
    print("2 - Cadastrar novo usuário")
    print("3 - Sair")

    escolha = input("\nSua escolha: ")

    if escolha == '1':
        loginSystem()
    elif escolha == '2':
        cadastarUsuario()
    elif escolha == '3':
        sair()
    elif escolha != '1' and escolha != '2' and escolha != '3':
        print("\nOpção inválida.")
        time.sleep(1)
        selecaoSistema()

def loginSystem():

    print("\033c")
    print("===== TELA DE LOGIN ======\n")

    print("\nPara cadastrar um novo usuário, digite Voltar\n")

    login = input("Login: ")
    if login == 'voltar' or login == 'Voltar':
        selecaoSistema()
    senha = input("Senha: ")
    if senha == 'voltar' or senha == 'Voltar':
        selecaoSistema()

    cursor_users.execute("SELECT * FROM users WHERE login=? AND senha=?", (login, senha))

    if cursor_users.fetchall():
        print("\nLogado com sucesso.\n")
        time.sleep(1)
        sistemaInside()
    else:
        print("\nAcesso negado. Tente novamente.\n")
        time.sleep(1)
        loginSystem() 

    users.close()

def sistemaInside():
    print("\033c")

    print("===== SISTEMA A2F =====\n")
    
    print("1 - Cadastrar cliente")
    print("2 - Pesquisar cliente")
    print("3 - Cadastrar produto")
    print("4 - Pesquisar produto")
    print("5 - Listar produtos")
    print("6 - Sair")

    escolha = input("\nSua escolha: ")
            
    if escolha == '1':
        cadastrarCliente()
    elif escolha == '2':
        pesqCliente()
    elif escolha == '3':
        cadastrarProduto()
    elif escolha == '4':
        pesqProduto()
    elif escolha == '5':
        listarProdutos()
    elif escolha == '6':
        exit()
    elif escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4' and escolha != '5' and escolha != '6':
        print("\nOpção inválida.")
        time.sleep(1)
        sistemaInside()

def cadastarUsuario():
    
    print("\033c")

    print("===== CADASTRAR NOVO USUÁRIO =====\n")

    x1 = input("Digite um login: ")
    x2 = input("Digite um senha: ")
    cursor_users.execute("INSERT INTO users values(?,?)",(x1,x2))

    print("\nUsuário cadastrado com sucesso.")

    users.commit()
    time.sleep(1)
    selecaoSistema()
    users.close()

def cadastrarCliente():
    print("\033c")

    print("===== CADASTRAR NOVO CLIENTE =====\n")

    c1 = input("Nome: ")
    c2 = input("CPF/CNPJ: ")
    c3 = input("Endereço: ")
    c4 = input("Bairro: ")
    c5 = input("CEP: ")
    c6 = input("Cidade: ")
    c7 = input("Estado: ")

    cursor_client.execute("INSERT INTO clients VALUES(?,?,?,?,?,?,?)",(c1,c2,c3,c4,c5,c6,c7))

    print("\nUsuário cadastrado com sucesso.")

    client.commit()
    time.sleep(1)
    sistemaInside()
    client.close()

def cadastrarProduto():
    print("\033c")

    print("===== CADASTRAR NOVO PRODUTO =====\n")

    j1 = input("Nome: ")
    j2 = int(input("Referência: "))
    j3 = float(input("Preço: "))
    j4 = int(input("Quantidade: "))

    cursor_prod.execute("INSERT INTO prod values(?,?,?,?)",(j1,j2,j3,j4))

    print("\nProduto cadastrado com sucesso.")

    prod.commit()
    time.sleep(1)
    sistemaInside()
    prod.close()

def pesqCliente():
    print("\033c")

    print("===== PESQUISAR CLIENTE =====")
    p1 = input("\nDigite o CPF/CNPJ do cliente: ")
    
    cursor_client.execute("SELECT * FROM clients;")

    for linha in cursor_client.fetchall():  
        if linha[1] == p1:
            print("\033c")

            print("USER FOUND\n")

            print("\nNome: ", linha[0])
            print("CPF: ", linha[1])
            print("Endereço: ", linha[2])
            print("Bairro: ", linha[3])
            print("CEP: ", linha[4])
            print("Cidade: ", linha[5])
            print("Estado: ", linha[6])
            print("\n")
            time.sleep(2)

            while True:
                print("O que você deseja fazer?\n")

                print("1 - Nova pesquisa")    
                print("2 - Voltar ao menu anterior")
                print("3 - Sair")

                escolha = input("Sua escolha: ")
                                
                if escolha == '1':
                    pesqCliente()
                elif escolha == '2':
                    sistemaInside()
                elif escolha == '3':
                    sair()
                elif escolha != '1' and escolha != '2' and escolha != '3':
                    print("\nOpção inválida.")
                    time.sleep(1)
                    print("\033c")
                    continue       
        else:
            print("\nCliente não encontrado. Tente novamente.")
            time.sleep(1)
            pesqCliente()
        
    client.close()

def pesqProduto():
    print("\033c")

    print("===== PESQUISAR PRODUTO =====")
    p1 = int(input("\nDigite a referência do produto: "))

    cursor_prod.execute("SELECT * FROM prod;")

    for linha in cursor_prod.fetchall():  
        if linha[1] == p1:
            print("\033c")

            print("PRODUCT FOUND\n")

            print("\nNome: ", linha[0])
            print("Referência: ", linha[1])
            print("Preço: ", linha[2])
            print("Quantidade: ", linha[3])
            print("\n")
        
            time.sleep(2)

            while True:
                print("O que você deseja fazer?\n")

                print("1 - Nova pesquisa")    
                print("2 - Voltar ao menu anterior")
                print("3 - Sair")

                escolha = input("Sua escolha: ")
            
                if escolha == '1':
                    pesqProduto()
                elif escolha == '2':
                    sistemaInside()
                elif escolha == '3':
                    sair()
                elif escolha != '1' and escolha != '2' and escolha != '3':
                    print("\nOpção inválida.")
                    time.sleep(1)
                    print("\033c")
                    continue
        else:
            print("\nProduto não encontrado. Tente novamente.")
            time.sleep(1)
            pesqProduto()

    prod.close()

def listarProdutos():

    print("\033c")
    print("===== PRODUTOS CADASTRADOS NO SISTEMA =====\n\n")

    cursor_prod.execute("SELECT * FROM prod;")

    produtos = cursor_prod.fetchall()

    print(tabulate(produtos, headers=["Nome","Referência", "Preço", "Estoque"]))

    time.sleep(1)
    
    while True:
        print("\n\nO que você deseja fazer?\n")

        print("1 - Voltar ao menu anterior")  
        print("2 - Sair")

        escolha = input("Sua escolha: ")

        if escolha == '1':
            sistemaInside()
        elif escolha == '2':
            exit()
        elif escolha != '1' and escolha != '2':
            print("\nOpção inválida.")
            time.sleep(1)
            print("\033c")
            continue 
    
    prod.close()

def sair():
    exit()

selecaoSistema()

