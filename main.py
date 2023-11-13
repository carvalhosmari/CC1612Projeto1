from biblioteca import *
    
def main():

    # Carrega os clientes do arquivo
    clientes = carrega_clientes()

    while (True):
        # Exibe o menu principal
        imprime_menu()
        
        # Solicita a opção do usuário
        inputUsuario = int(input("Opcao desejada: "))
        print()

        # Realiza a ação correspondente à opção escolhida
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
            gera_extrato(clientes)
        elif (inputUsuario == 7):
            transfere_valor(clientes)
        elif (inputUsuario == 8):
            while (True):
                # Exibe o menu de cartões
                imprime_menu_cartao()

                # Solicita a opção do usuário
                inputUsuario = int(input("Opcao desejada: "))
                print()

                # Realiza a ação correspondente à opção escolhida no menu de cartões
                if inputUsuario == 1:
                    lista_cartoes(clientes)
                elif inputUsuario == 2:
                    emite_cartao(clientes)
                elif inputUsuario == 3:
                    cancela_cartao(clientes)
                elif inputUsuario == 4:
                    break
                else:
                    print("opcao invalida")    
        elif (inputUsuario == 9):
            # Encerra o programa
            break
        else:
            print("Opcao invalida!")

if __name__ == "__main__":
    main()