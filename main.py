def cadastra_cliente(clientes):
    razao_social = input("Digite a razao social: ")
    CNPJ = input("Digite o CNPJ: ")
    tipo_conta = input("Digite o tipo de conta: ")
    saldo_inicial = float(input("Digite o saldo inicial: "))
    senha = input("Digite uma senha: ")

    cliente = {
        "razao_social": razao_social,
        "cnpj": CNPJ,
        "tipo_conta": tipo_conta,
        "saldo": saldo_inicial,
        "senha": senha
    }

    clientes.append(cliente)

def deleta_cliente(clientes):
    cnpj_cliente = input("Digite o CNPJ do cliente que sera deletado: ")

    for cliente in clientes:
        if cliente['cnpj'] == cnpj_cliente:
            clientes.remove(cliente)
            print("cliente deletado com sucesso!")
        
def lista_clientes(clientes):
    print("dentro da funcao listar clientes:")
    for cliente in clientes:
        print()
        for chave, valor in cliente.items():
            print(f"{chave}: {valor}")

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


clientes = []

while (True):
    print(f"\nMenu principal:\n\n\t1 - Novo cliente\n\t2 - Apaga cliente\n\t3 - Listar clientes\n\t4 - Debito\n\t5 - Deposito\n\t6 - Extrato\n\t7 - Transferencia entre contas\n\t8 - Operacao livre\n\t9 - Sair\n")

    inputUsuario = int(input("Opcao desejada: "))
    print()

    if (inputUsuario == 1):
        cadastra_cliente(clientes)
    elif (inputUsuario == 2):
        deleta_cliente(clientes)
    elif (inputUsuario == 3):
        lista_clientes(clientes)
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