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
    CNPJ = input("Digite o CNPJ do cliente que sera deletado: ")

    indice_cliente = retorna_indice_cliente(clientes, CNPJ)

    if indice_cliente == -1:
        print("\nCNPJ nao encontrado!")
    else:
        cliente = clientes[indice_cliente]

        clientes.remove(cliente)            
        
        print("\nCliente deletado com sucesso!")
        
def lista_clientes(clientes):
    for cliente in clientes:
        for chave, valor in cliente.items():
            print(f"{chave}: {valor}")
        
        print()

def debita_valor(clientes):
    CNPJ = input("Digite o CNPJ da conta que tera o valor debitado: ")
    
    indice_cliente = retorna_indice_cliente(clientes, CNPJ)

    if indice_cliente == -1:
        print("\nCNPJ nao encontrado")
    else:
        senha = input("Digite a senha:")
        cliente = clientes[indice_cliente]        
        
        if cliente['senha'] == senha:
            valor = float(input("Valor a ser debitado: "))

            if cliente['tipo_conta'] == "comum":
                valor_debitado = valor * 1.05
            else:
                valor_debitado = valor * 1.03
            
            cliente['saldo'] -= valor_debitado
            print("\nTransacao concluida com sucesso!")
        else:
            print("\nSenha incorreta!")

def deposita_valor(clientes):
    CNPJ = input("Digite o CNPJ da conta que o valor sera depositado: ")
    indice_cliente = retorna_indice_cliente(clientes, CNPJ)

    if indice_cliente == -1:
        print("\nCNPJ nao encontrado")
    else:
        cliente = clientes[indice_cliente]    

        valor = float(input("Valor a ser depositado: "))  

        cliente['saldo'] += valor
        print("\nTransacao concluida com sucesso!")       

def gera_extrato():
    CNPJ = input("Digite o CNPJ da conta: ")
    senha = input("Digite a senha: ")

    print(f"CNPJ: {CNPJ}")
    print(f"senha: {senha}")

def transfere_valor(clientes):
    CNPJ_origem = input("Digite o CNPJ da conta de origem: ")
    indice_cliente_origem = retorna_indice_cliente(clientes, CNPJ_origem)

    if indice_cliente_origem == -1:
        print("\nCNPJ nao encontrado!")
    else:
        cliente_origem = clientes[indice_cliente_origem]

        senha_origem = input("Digite a senha: ")

        if cliente_origem['senha'] == senha_origem:
            CNPJ_destino = input("Digite o CNPJ da conta de destino: ")
            indice_cliente_destino = retorna_indice_cliente(clientes, CNPJ_destino)

            if indice_cliente_destino == -1:
                print("\nCNPJ nao encontrado!")
            else:
                cliente_destino = clientes[indice_cliente_destino]
                valor = float(input("Valor a ser transferido: "))
            
                cliente_origem['saldo'] -= valor
                cliente_destino['saldo'] += valor

                print("\nTransacao concluida com sucesso!")
        else:
            print("\nSenha incorreta!")

def retorna_indice_cliente(clientes, cnpj):
    for cliente in clientes:
        if cliente['cnpj'] == cnpj:
            return clientes.index(cliente)
        
    return -1


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
        debita_valor(clientes)
    elif (inputUsuario == 5):
        deposita_valor(clientes)
    elif (inputUsuario == 6):
        gera_extrato()
    elif (inputUsuario == 7):
        transfere_valor(clientes)
    elif (inputUsuario == 8):
        print("Operacao livre")
    elif (inputUsuario == 9):
        print("Dentro da opcao sair (encerra o programa)\n")
        break
    else:
        print("Opcao invalida!")