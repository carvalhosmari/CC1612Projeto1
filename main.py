def cadastra_cliente():
    razao_social = input("Digite a razao social: ")
    CNPJ = input("Digite o CNPJ: ")
    tipo_conta = input("Digite o tipo de conta: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))
    senha = input("Digite uma senha: ")

    print(f"razao social: {razao_social}")
    print(f"CNPJ: {CNPJ}")
    print(f"tipo de conta: {tipo_conta}")
    print(f"saldo inicial: {saldo_inicial}")
    print(f"senha: {senha}")

def deleta_cliente():
    print("Dentro da funcao apagar!\n")

def lista_clientes():
    print("Dentro da funcao listar clientes!\n")

def debita_valor():
    CNPJ = input("Digite o CNPJ da conta que tera o valor debitado: ")
    senha = input("Digite a senha: ")
    valor = float(input("Digite o valor: "))

    print(f"CNPJ: {CNPJ}")
    print(f"senha: {senha}")
    print(f"valor: {valor}")

def deposita_valor():
    CNPJ = input("Digite o CNPJ da conta que o valor sera depositado: ")
    valor = float(input("Digite o valor: "))

    print(f"CNPJ: {CNPJ}")
    print(f"valor: {valor}")

def gera_extrato():
    CNPJ = input("Digite o CNPJ da conta: ")
    senha = input("Digite a senha: ")

    print(f"CNPJ: {CNPJ}")
    print(f"senha: {senha}")

def transfere_valor():
    CNPJ_origem = input("Digite o CNPJ da conta de origem: ")
    senha_origem = input("Digite a senha: ")
    CNPJ_destino = input("Digite o CNPJ da conta de destino: ")
    senha_destino = input("Digite a senha: ")

    print(f"CNPJ conta origem: {CNPJ_origem}")
    print(f"senha conta origem: {senha_origem}")
    print(f"CNPJ conta destino: {CNPJ_destino}")
    print(f"senha conta destino: {senha_destino}")



while (True):
    print(f"\nMenu principal:\n\n\t1 - Novo cliente\n\t2 - Apaga cliente\n\t3 - Listar clientes\n\t4 - Debito\n\t5 - Deposito\n\t6 - Extrato\n\t7 - Transferencia entre contas\n\t8 - Operacao livre\n\t9 - Sair\n")

    inputUsuario = int(input("Opcao desejada: "))

    if (inputUsuario == 1):
        cadastra_cliente()
    elif (inputUsuario == 2):
        deleta_cliente()
    elif (inputUsuario == 3):
        lista_clientes()
    elif (inputUsuario == 4):
        debita_valor()
    elif (inputUsuario == 5):
        deposita_valor()
    elif (inputUsuario == 6):
        gera_extrato()
    elif (inputUsuario == 7):
        transfere_valor()
    elif (inputUsuario == 8):
        print("Operacao livre")
    elif (inputUsuario == 9):
        print("Dentro da opcao sair (encerra o programa)\n")
        break
    else:
        print("Opcao invalida!")