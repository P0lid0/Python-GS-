# Variáveis e Tipos de Dados
usuarios = ["ONG", "Investidor"]
mensagens = []


# Funções para o Chat
def enviar_mensagem(usuario, mensagem):
    """Função para enviar uma mensagem no chat"""
    if usuario in usuarios:
        mensagens.append((usuario, mensagem))
    else:
        print("Usuário não registrado")


def visualizar_mensagens():
    """Função para visualizar todas as mensagens no chat"""
    if mensagens:
        for usuario, mensagem in mensagens:
            print(f"{usuario}: {mensagem}")
    else:
        print("Nenhuma mensagem encontrada.")


def visualizar_mensagens_usuario(usuario):
    """Função para visualizar mensagens de um usuário específico"""
    encontrou_mensagem = False
    for u, mensagem in mensagens:
        if u == usuario:
            print(f"{u}: {mensagem}")
            encontrou_mensagem = True
    if not encontrou_mensagem:
        print("Nenhuma mensagem encontrada para este usuário.")


def remover_mensagem(indice):
    """Função para remover uma mensagem pelo índice"""
    if 0 <= indice < len(mensagens):
        del mensagens[indice]
        print("Mensagem removida com sucesso.")
    else:
        print("Índice inválido")


# Estruturas de Controle e Manipulação de Listas e Strings
while True:
    print("\nMenu do Chat")
    print("1. Enviar Mensagem")
    print("2. Visualizar Todas as Mensagens")
    print("3. Visualizar Mensagens de um Usuário")
    print("4. Remover Mensagem")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        usuario = input("Digite o nome do usuário: ")
        mensagem = input("Digite a mensagem: ")
        enviar_mensagem(usuario, mensagem)
    elif escolha == "2":
        visualizar_mensagens()
    elif escolha == "3":
        usuario = input("Digite o nome do usuário: ")
        visualizar_mensagens_usuario(usuario)
    elif escolha == "4":
        indice = int(input("Digite o índice da mensagem para remover: "))
        remover_mensagem(indice)
    elif escolha == "5":
        print("Saindo do chat.")
        break
    else:
        print("Opção inválida. Tente novamente.")
