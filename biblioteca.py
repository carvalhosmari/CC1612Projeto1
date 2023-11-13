from datetime import datetime
import uuid
import random
import json
import os

# Funcao que cadastra um novo cliente
def cadastra_cliente(clientes):
    # Solicita informações do cliente ao usuário
    razao_social = input("Digite a razao social: ")
    CNPJ = input("Digite o CNPJ: ")
    tipo_conta = int(input("Digite o tipo de conta: \n\t1 - comum;\n\t2 - plus.\n"))
    saldo_inicial = float(input("Digite o saldo inicial: "))
    senha = input("Digite uma senha: ")
    transacoes = []
    cartoes = []

    # Gera um cartão de débito para o cliente
    cartao = {
        "titular": razao_social,
        "tipo": "debito",
        "numero": uuid.uuid4().hex, # UUID convertido em string para ser o identificador do cliente
        "validade": int(datetime.now().year) + random.randint(3, 10), # Ano ficticio de validade do cartão
        "limite": 0, 
        "status": "ativo"
    }

    cartoes.append(cartao)

    # Cria um dicionário representando o cliente
    cliente = {
        "razao_social": razao_social,
        "cnpj": CNPJ,
        "tipo_conta": tipo_conta,
        "saldo": saldo_inicial,
        "senha": senha,
        "extrato": transacoes,
        "cartoes": cartoes
    }

    # Registra uma transação inicial de depósito no extrato do cliente
    registra_transacao(cliente, 2, saldo_inicial)

    # Adiciona o cliente à lista de clientes
    clientes.append(cliente)

    # Salva a lista atualizada de clientes no arquivo
    salva_clientes(clientes)

# Funcao que deleta um cliente atraves do CNPJ
def deleta_cliente(clientes):
    # Solicita o CNPJ do cliente a ser deletado
    CNPJ = input("Digite o CNPJ do cliente que sera deletado: ")

    # Obtém o índice do cliente na lista
    indice_cliente = retorna_indice_cliente(clientes, CNPJ)

    # Verifica se há clientes com o CNPJ informado
    if indice_cliente == -1:
        print("\nCNPJ nao encontrado!")
    else:
        cliente = clientes[indice_cliente]

        # Remove o cliente da lista
        clientes.remove(cliente)            
        
        # Salva a lista atualizada de clientes no arquivo
        salva_clientes(clientes)

        print("\nCliente deletado com sucesso!")

# Funcao que lista todos os clientes cadastrados       
def lista_clientes(clientes):
    # Verifica se há clientes cadastrados
    if len(clientes) == 0:
        print("Lista de clientes vazia.")
    else:
        tipo = ""
        for cliente in clientes:
            # Define o tipo de conta com base no valor em 'tipo_conta'
            if cliente['tipo_conta'] == 1:
                tipo = "comum"
            else:
                tipo = "plus"
            
            # Exibe informações do cliente
            print(f"nome: {cliente['razao_social']}")
            print(f"CNPJ: {cliente['cnpj']}")
            print(f"conta: {tipo}")
            print(f"saldo: R$ {(cliente['saldo']):.2f}\n")
            
# Funcao que debita um valor da conta do cliente
def debita_valor(clientes):
    # Solicita o CNPJ da conta
    CNPJ = input("Digite o CNPJ da conta que tera o valor debitado: ")

    # Obtém o índice do cliente na lista 
    indice_cliente = retorna_indice_cliente(clientes, CNPJ)

    # Verifica se há clientes com o CNPJ informado
    if indice_cliente == -1:
        print("\nCNPJ nao encontrado")
    else:
        # Solicita a senha do cliente
        senha = input("Digite a senha:")
        
        cliente = clientes[indice_cliente]
        limite = 0   

        # Verifica se a senha é correta
        if cliente['senha'] == senha:
            # Solicita o valor a ser debitado
            valor = float(input("Valor a ser debitado: "))

            # Atribui valor ao limite e calcula o valor debitado com base no tipo de conta
            if cliente['tipo_conta'] == 1:
                valor_debitado = valor * 1.05
                limite = -1000
            else:
                valor_debitado = valor * 1.03
                limite = -5000
            
            # Verifica se o saldo é suficiente para o débito
            if cliente['saldo'] - valor_debitado >= limite:
                # Debita valor + taxa da conta do cliente
                cliente['saldo'] -= valor_debitado

                # Registra a transacao no extrato do cliente
                registra_transacao(cliente, 1, valor_debitado)

                # Salva a lista atualizada de clientes no arquivo
                salva_clientes(clientes)

                print("\nTransacao concluida com sucesso!")
            else:
                # Caso não haja saldo
                print("\nSaldo insuficiente!")
        else:
            # Caso a senha esteja incorreta
            print("\nSenha incorreta!")

# Funcao que deposita valor na conta do cliente
def deposita_valor(clientes):
    # Solicita o CNPJ da conta
    CNPJ = input("Digite o CNPJ da conta que o valor sera depositado: ")

    # Obtém o índice do cliente na lista 
    indice_cliente = retorna_indice_cliente(clientes, CNPJ)

    # Verifica se há clientes com o CNPJ informado   
    if indice_cliente == -1:
        print("\nCNPJ nao encontrado")
    else:
        cliente = clientes[indice_cliente]    

        # Solicita o valor a ser depositado
        valor = float(input("Valor a ser depositado: "))  
        
        # Deposita o valor na conta do cliente
        cliente['saldo'] += valor

        # Registra a transacao no extrato do cliente
        registra_transacao(cliente, 2, valor)

        # Salva a lista atualizada de clientes no arquivo
        salva_clientes(clientes)

        print("\nTransacao concluida com sucesso!")       

# Funcao que gera o extrato do cliente
def gera_extrato(clientes):
    # Solicita o CNPJ da conta
    CNPJ = input("Digite o CNPJ da conta: ")

    # Obtém o índice do cliente na lista
    indice_cliente = retorna_indice_cliente(clientes, CNPJ)

    # Verifica se há clientes com o CNPJ informado
    if indice_cliente == -1:
        print("\nCNPJ nao encontrado")
    else:
        tipo = ""
        cliente = clientes[indice_cliente]    
        
        # Define o tipo de conta com base no valor em 'tipo_conta'
        if cliente['tipo_conta'] == 1:
            tipo = "comum"
        else: 
            tipo = "plus"

        # Solicita a senha do cliente
        senha = input("Digite a senha: ")  

        # Verifica se a senha é correta
        if cliente['senha'] == senha:
            print()
            print(f"nome: {cliente['razao_social']}")
            print(f"CNPJ: {cliente['cnpj']}")
            print(f"conta: {tipo}")
            print()

            # Exibe cada transação no extrato do cliente
            for transacao in cliente["extrato"]:
                print(f"{transacao['data']}\tvalor: R$ {(transacao['valor']):.2f}\ttarifa: {(transacao['tarifa']):.2f}\tsaldo: R$ {(transacao['saldo_atual']):.2f}")
        else:
            # Caso a senha esteja incorreta
            print("\nSenha incorreta!")

# Funcao que transfere valores entre contas 
def transfere_valor(clientes):
    limite = 0

    # Solicita o CNPJ da conta de origem
    CNPJ_origem = input("Digite o CNPJ da conta de origem: ")

    # Obtém o índice do cliente na lista
    indice_cliente_origem = retorna_indice_cliente(clientes, CNPJ_origem)

    # Verifica se há clientes com o CNPJ informado
    if indice_cliente_origem == -1:
        print("\nCNPJ nao encontrado!")
    else:
        cliente_origem = clientes[indice_cliente_origem]
        
        # Define o valor do limite com base no tipo de conta
        if cliente_origem['tipo_conta'] == "comum":
            limite == -1000
        else:
            limite == -5000

        # Solicita a senha do cliente
        senha_origem = input("Digite a senha: ")

        # Verifica se a senha é correta
        if cliente_origem['senha'] == senha_origem:
            # Solicita o CNPJ da conta de destino
            CNPJ_destino = input("Digite o CNPJ da conta de destino: ")
            
            
            # Obtém o índice do cliente na lista
            indice_cliente_destino = retorna_indice_cliente(clientes, CNPJ_origem)

            # Verifica se há clientes com o CNPJ informado
            if indice_cliente_destino == -1:
                print("\nCNPJ nao encontrado!")
            else:
                cliente_destino = clientes[indice_cliente_destino]

                # Solicita o valor a ser transferido
                valor = float(input("Valor a ser transferido: "))
            
                # Verifica se ha saldo suficiente
                if cliente_origem['saldo'] - valor >= limite:
                    # Debita o valor na conta da conta de origem e registra a transacao no extrato do cliente
                    cliente_origem['saldo'] -= valor
                    registra_transacao(cliente_origem, 3, valor)

                    # Deposita o valor na conta da conta de destino e registra a transacao no extrato do cliente
                    cliente_destino['saldo'] += valor
                    registra_transacao(cliente_destino, 4, valor)

                    print("\nTransacao concluida com sucesso!")

                    # Salva a lista atualizada de clientes no arquivo
                    salva_clientes(clientes)
                else:
                    # Caso não haja saldo
                    print("\nSaldo insuficiente!")
        else:
            # Caso a senha esteja incorreta
            print("\nSenha incorreta!")

# Funcao que retorna o indice de um determinado cliente na lista de clientes
def retorna_indice_cliente(clientes, cnpj):
    for cliente in clientes:
        # Retorna o indice do cliente caso haja correspondencia de CNPJ
        if cliente['cnpj'] == cnpj:
            return clientes.index(cliente)

    # Retorna -1 caso não haja correspondencia de CNPJ
    return -1

# Funcao que registra a transacao no extrato do cliente
def registra_transacao(cliente, tipo_op, valor):
    # Obtém a data e hora atual no formato dia/mes/ano hora:min:seg
    data_transacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    tipo_transacao = ""
    tarifa = 0

    # Determina o tipo de transação com base no tipo_op
    if tipo_op == 1:
        tipo_transacao = "debito"

        # Multiplica o valor por -1 para indicar saida no extrato
        valor = valor * (-1) 

        # Calcula a tarifa com base no tipo de conta
        if cliente["tipo_conta"] == 1:
            tarifa = 0.05
        else:
            tarifa = 0.03
    elif tipo_op == 2:
        tipo_transacao = "deposito"
    elif tipo_op == 3:
        tipo_transacao = "transferencia enviada"

        # Multiplica o valor por -1 para indicar saida no extrato
        valor = valor * (-1)
    else:
        tipo_transacao = "transferencia recebida"

    # Cria um dicionário representando a operação realizada
    operacao = {
        "data": data_transacao,
        "tipo": tipo_transacao,
        "valor": valor,
        "tarifa": tarifa,
        "saldo_atual": cliente["saldo"]
    }

    # Adiciona a operação no extrato do cliente
    cliente["extrato"].append(operacao)

# Funcao que imprime o menu principal
def imprime_menu():
    print()
    print("**********************")
    print("*** QUEM POUPA TEM ***")
    print("**********************")
    print(f"\nMenu principal:\n\n\t1 - Novo cliente\n\t2 - Apaga cliente\n\t3 - Listar clientes\n\t4 - Debito\n\t5 - Deposito\n\t6 - Extrato\n\t7 - Transferencia entre contas\n\t8 - Cartoes\n\t9 - Sair\n")

# Funcao que imprime o menu da seção cartões
def imprime_menu_cartao():
    print(f"Cartoes:\n\t1 - Consultar cartoes por cliente\n\t2 - Emitir novo cartao\n\t3 - Cancelar cartao\n\t4 - Sair\n")

# Funcao que lista os cartões cadastrados na conta do cliente
def lista_cartoes(clientes):
    # Solicita o CNPJ da conta que deseja ter os cartões listados
    CNPJ = input("Digite o CNPJ da conta: ")

    # Obtém o índice do cliente na lista
    indice_cliente = retorna_indice_cliente(clientes, CNPJ)

    # Verifica se há clientes com o CNPJ informado
    if indice_cliente == -1:
        print("\nCNPJ nao encontrado")
    else:
        cliente = clientes[indice_cliente]    
 
        # Lista os cartões cadastrados na conta 
        print()
        print(f"titular: {cliente['razao_social']}\nconta: {cliente['tipo_conta']}")     
        for cartao in cliente["cartoes"]:
            print(f"\ttipo: {cartao['tipo']}\tlimite: R$ {(cartao['limite']):.2f} \tnumero: {(cartao['numero'])}\tvalidade: {cartao['validade']}\tstatus: {cartao['status']}")
            
        print()

# Funcao que emite um novo cartao      
def emite_cartao(clientes):
   # Solicita o CNPJ da conta que deseja ter os cartões listados
    CNPJ = input("Digite o CNPJ da conta: ")

    # Obtém o índice do cliente na lista
    indice_cliente = retorna_indice_cliente(clientes, CNPJ)

    # Verifica se há clientes com o CNPJ informado
    if indice_cliente == -1:
        print("\nCNPJ nao encontrado")
    else:
        cliente = clientes[indice_cliente]
        tipoStr = ""
        limite = 0

        # Solicita o tipo de cartao a ser emitido (crédito ou débito)
        tipo = int(input("Tipo de cartao:\n\t1 - credito\n\t2 - debito\n\nopcao desejada:"))

        if tipo == 1:
            tipoStr = "credito"

            # No caso de cartão de crédito, solicita o valor do limite
            limite = float(input("Limite:"))            
        else:
            tipoStr = "debito"

        # Atribui valores ao novo cartão
        cartao = {
        "titular": cliente['razao_social'],
        "tipo": tipoStr,
        "numero": uuid.uuid4().hex, # UUID convertido em string para ser o identificador do cliente
        "validade": int(datetime.now().year) + random.randint(3, 10), # Ano ficticio de validade do cartão
        "limite": limite,
        "status": "ativo"
        }

        # Adiciona o novo cartão na lista de cartões do cliente
        cliente['cartoes'].append(cartao)

        # Salva a lista atualizada de clientes no arquivo
        salva_clientes(clientes)

        print("\nCartao emitido com sucesso!\n\n")

def cancela_cartao(clientes):
    # Solicita o CNPJ da conta que deseja ter os cartões listados
    CNPJ = input("Digite o CNPJ da conta: ")

    # Obtém o índice do cliente na lista
    indice_cliente = retorna_indice_cliente(clientes, CNPJ)

    # Verifica se há clientes com o CNPJ informado
    if indice_cliente == -1:
        print("\nCNPJ nao encontrado")
    else:
        cliente = clientes[indice_cliente]

        # Solicita o identificador do cartao que será cancelado
        numCartao = input("Digite o numero do cartao que sera cancelado:")
        
        for cartao in cliente['cartoes']:
            # Verifica se existe cartao com o identificador
            if cartao['numero'] == numCartao:
                # Altera o status do cartão para cancelado
                cartao['status'] = "cancelado"

                print("\nCartao cancelado com sucesso!\n")   

                # Salva a lista atualizada de clientes no arquivo
                salva_clientes(clientes)
            else:
                # Caso não haja cartão relacionado ao identificador
                print("\nCartao nao encontrado!\n")

# Funcao que persiste os dados no arquivo txt
def salva_clientes(clientes):
    # Abre o arquivo em modo de escrita
    arquivo = open("arquivoClientes.txt", "w")

    for cliente in clientes:
        # Converte as listas de extrato e cartões para strings JSON ao inves de string
        # para facilitar a leitura do txt posteriormente
        extrato_json = json.dumps(cliente['extrato'])
        cartoes_json = json.dumps(cliente['cartoes'])

        # Escreve os dados do cliente no arquivo
        arquivo.write(f"{cliente['razao_social']};{cliente['cnpj']};{cliente['tipo_conta']};{cliente['saldo']};{cliente['senha']};{extrato_json};{cartoes_json}\n")

    # Fecha o arquivo
    arquivo.close()

def carrega_clientes():
    # Inicializa uma lista de clientes vazia
    clientes = []

    # Path do arquivo txt
    arquivo = "arquivoClientes.txt"

    # Verifica se o arquivo existe
    if os.path.exists(arquivo):
        arquivo = open(arquivo, "r")

        for linha in arquivo:
            # Divide a linha em dados usando o ponto e vírgula como delimitador
            dados_cliente = linha.strip().split(";")
            razao_social, cnpj, tipo_conta, saldo, senha, extrato, cartoes = dados_cliente
            
            # Cria um dicionário representando o cliente
            cliente = {
                "razao_social": razao_social,
                "cnpj": cnpj,
                "tipo_conta": tipo_conta,
                "saldo": float(saldo),
                "senha": senha,
                "extrato": json.loads(extrato),
                "cartoes": json.loads(cartoes)
            }

            # Adiciona o cliente à lista de clientes
            clientes.append(cliente)
        
        # Fecha o arquivo
        arquivo.close()

    return clientes
